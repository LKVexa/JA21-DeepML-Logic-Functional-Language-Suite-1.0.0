# Technical Corpus Guide

> **JA21 DeepML Logic/Functional Language Suite 1.0.0**  
> A normalized, air-gap-friendly evidence corpus for pure functional programming, symbolic logic, proof systems, planning, compiler transformations, and JA21 integration.

## Corpus at a glance

| Measure | Value |
|---|---:|
| Records | 10,000 |
| Topics | 46 |
| Proficiency tiers | 6 |
| Positive records | 7,875 |
| Negative records | 2,060 |
| Certification holdouts | 65 |
| Source hashes verified | 10,000 |
| Master format | gzip-compressed JSON Lines |
| Shards | 20 × 500 records |

## Record anatomy

A record combines seven evidence planes:

1. **Source plane** — a complete `deepml logic 0.3` program.
2. **Syntactic plane** — AST and parsed construct representation.
3. **Semantic plane** — interpretation, judgments, identities, effects, and proof obligations.
4. **Compiler plane** — lowering and optimization evidence, including R12 relations.
5. **Runtime plane** — execution or expected-failure representation, including MCRT relations.
6. **Validation plane** — expected stage, diagnostic, checks, class, and holdout status.
7. **Pedagogical plane** — topic, concepts, tier, difficulty, and technical explanation.

## Reading order

Start with `catalogs/CORPUS_INDEX.csv`, filter by `topic`, `tier_name`, or `example_class`, then retrieve the corresponding JSONL record. The 1,000-script pack offers source files for direct browsing; the textbook supplies guided sequences.

## Topic distribution

| Topic | Records |
|---|---:|
| `algebraic_data_type` | 125 |
| `ambiguous_instance` | 125 |
| `beta_reduction` | 188 |
| `certification_logic` | 417 |
| `constraint_solving` | 358 |
| `contradictory_facts` | 125 |
| `cse` | 187 |
| `deforestation` | 187 |
| `effect_declaration` | 166 |
| `expression` | 125 |
| `fact` | 125 |
| `fold` | 167 |
| `guard` | 167 |
| `higher_order_function` | 167 |
| `immutable_value` | 125 |
| `impure_effect` | 125 |
| `incomplete_match` | 125 |
| `inference_divergence` | 125 |
| `inference_strategy` | 357 |
| `knowledge_base` | 417 |
| `lambda` | 125 |
| `logic_graph_integration` | 357 |
| `memoization` | 357 |
| `module` | 167 |
| `nontermination` | 125 |
| `occurs_check` | 125 |
| `pattern_match` | 125 |
| `planning_system` | 417 |
| `predicate` | 125 |
| `proof_carrying_transform` | 416 |
| `proof_normalization` | 188 |
| `proof_term` | 357 |
| `pure_function` | 125 |
| `r12_mcrt_lowering` | 188 |
| `recursion` | 167 |
| `rule` | 166 |
| `rule_indexing` | 187 |
| `scene_timeline_rules` | 417 |
| `symbolic_neural_workflow` | 416 |
| `symbolic_reasoning` | 357 |
| `tabling` | 187 |
| `tail_call` | 188 |
| `theorem` | 357 |
| `trait` | 166 |
| `unification` | 167 |
| `unsound_proof` | 125 |

## Tier distribution

| Tier | Records |
|---|---:|
| `advanced_composition` | 2500 |
| `basic_syntax` | 1000 |
| `compiler_optimization` | 1500 |
| `intermediate_constructs` | 1500 |
| `large_integrated_examples` | 2500 |
| `validation_certification` | 1000 |

## Evidence cautions

- Smithson 8S Coupled Mechanics is carried as a proposed computational framework and provenance vocabulary, not as an established law of physics.
- `expected_stage`, `validation_result`, compiler, and runtime fields are corpus evidence. They do not prove native JA21 execution.
- Source hashes are verified against UTF-8 program text in this release.
