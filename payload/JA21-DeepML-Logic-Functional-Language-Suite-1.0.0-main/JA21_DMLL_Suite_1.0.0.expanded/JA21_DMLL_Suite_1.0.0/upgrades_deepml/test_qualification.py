"""Focused tests for audit authority and corruption boundaries, no source execution."""
import copy
import gzip
import json
from pathlib import Path
import unittest
from qualification import qualify
from validate_upgraded import load_validator, validate_record, refuse_external_references

ROOT = Path(__file__).resolve().parents[1]


class QualificationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        config = json.loads((ROOT / "upgrades_deepml" / "profile.json").read_text(encoding="utf-8"))
        cls.profile = config["profile"]
        cls.validator = load_validator(json.loads((ROOT / config["schema_path"]).read_text(encoding="utf-8")))
        with gzip.open(ROOT / "corpus" / "technical" / config["master"], "rt", encoding="utf-8") as stream:
            cls.record = json.loads(next(stream))

    def test_first_record_is_qualified_and_schema_valid(self):
        self.assertEqual([], validate_record(self.record, self.profile, self.validator))

    def test_forged_execution_eligibility_is_rejected(self):
        changed = copy.deepcopy(self.record)
        changed["_deepml_audit"]["native_execution_eligible"] = True
        self.assertTrue(validate_record(changed, self.profile, self.validator))

    def test_source_corruption_is_rejected(self):
        changed = copy.deepcopy(self.record)
        if isinstance(changed["source"], dict):
            changed["source"]["program"] += "\ncorruption"
        else:
            changed["source"] += "\ncorruption"
        self.assertTrue(validate_record(changed, self.profile, self.validator))

    def test_policy_removal_is_rejected_even_after_requalification(self):
        changed = copy.deepcopy(self.record)
        if isinstance(changed["source"], dict):
            changed["source"]["program"] = changed["source"]["program"].replace("policy no_network", "")
        else:
            changed["source"] = changed["source"].replace("policy no_network", "")
        changed["_deepml_audit"] = qualify(changed, self.profile)
        errors = validate_record(changed, self.profile, self.validator)
        self.assertIn("missing standalone no_network policy", errors)

    def test_remote_schema_reference_is_refused(self):
        with self.assertRaises(ValueError):
            refuse_external_references({"properties": {"x": {"$ref": "https://example.invalid/schema"}}})

    def test_local_schema_reference_is_allowed(self):
        refuse_external_references({"$defs": {"x": {"type": "string"}}, "$ref": "#/$defs/x"})


if __name__ == "__main__":
    unittest.main()
