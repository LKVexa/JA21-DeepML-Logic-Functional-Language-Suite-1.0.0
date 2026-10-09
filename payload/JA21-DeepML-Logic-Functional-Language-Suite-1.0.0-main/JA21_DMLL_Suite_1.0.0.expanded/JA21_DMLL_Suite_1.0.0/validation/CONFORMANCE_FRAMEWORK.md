# Conformance and Certification Framework

## Purpose

This framework separates **structural validation**, **modeled language conformance**, and **native execution evidence**. A toolchain may claim only the levels it has actually demonstrated.

## Levels

| Level | Name | Required evidence |
|---|---|---|
| C0 | Package Integrity | File counts, hashes, indexes, schemas, and deterministic archive verification |
| C1 | Lexical and Parse | Grammar acceptance/rejection with stable diagnostics |
| C2 | Type and Semantic | Types, exhaustiveness, purity, trait coherence, unification, and proof obligations |
| C3 | Compiler Preservation | Optimization identities and proof-carrying transformations |
| C4 | Runtime Replay | Deterministic evaluation, inference traces, and MCRT evidence |
| C5 | Certification | Holdout cases evaluated without tuning against their expected labels |

## Corpus partitions

- Positive: 7,875
- Negative: 2,060
- Certification holdout: 65

## Mandatory gates

1. UTF-8 source ingestion.
2. `deepml logic 0.3` version recognition.
3. Namespace and policy resolution.
4. Pure-by-default effect checking.
5. Exhaustive pattern analysis.
6. Trait coherence and ambiguity diagnostics.
7. Occurs-check and unification safety.
8. Termination or bounded-resource policy where required.
9. Proof-term and transformation validation.
10. Stable semantic, R12, and MCRT identity reporting.

## Claim discipline

The bundled validator checks release structure and source hashes. It is not a native compiler and must not be represented as one.
