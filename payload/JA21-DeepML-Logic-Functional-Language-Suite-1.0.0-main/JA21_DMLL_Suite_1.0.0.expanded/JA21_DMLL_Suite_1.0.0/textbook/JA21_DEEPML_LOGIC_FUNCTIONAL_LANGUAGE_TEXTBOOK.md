---
title: "JA21 DeepML Logic/Functional Language"
subtitle: "Technical Textbook, Corpus Reader, and Toolchain Laboratory"
version: "1.0.0"
language: "DeepML Logic 0.3"
suite: "JA21-DMLL"
record_count: 10000
script_pack_count: 1000
---

# JA21 DeepML Logic/Functional Language

## Technical Textbook, Corpus Reader, and Toolchain Laboratory

**Edition 1.0.0 · July 2026**

> Pure functions. Explicit logic. Proof-aware transformations. Deterministic evidence.

This textbook turns the 10,000-record Logic/Functional corpus into a complete learning path. It is designed for independent study, formal instruction, compiler implementation, and conformance engineering. The source corpus is authoritative for record identity; this book supplies narrative, sequence, laboratories, and review structure.

## How to use this book

Read Chapters 1–8 for the functional core, Chapters 9–15 for logic and proof systems, Chapters 16–18 for integrated applications, and Chapters 19–22 for compiler, runtime, certification, and capstone work. Every chapter names a source-faithful corpus record and uses its modeled evidence without claiming native execution.

## Contents

1. [Orientation: Logic, Function, and Evidence](#1-orientation-logic-function-and-evidence)
2. [Program Anatomy and Module Boundaries](#2-program-anatomy-and-module-boundaries)
3. [Types and Algebraic Data](#3-types-and-algebraic-data)
4. [Immutable Values and Expressions](#4-immutable-values-and-expressions)
5. [Pure Functions, Lambdas, and Closures](#5-pure-functions-lambdas-and-closures)
6. [Pattern Matching and Guards](#6-pattern-matching-and-guards)
7. [Recursion, Folds, and Termination](#7-recursion-folds-and-termination)
8. [Traits, Instances, Effects, and Capabilities](#8-traits-instances-effects-and-capabilities)
9. [Predicates, Facts, and Rules](#9-predicates-facts-and-rules)
10. [Unification and the Occurs Check](#10-unification-and-the-occurs-check)
11. [Inference Strategies and Search](#11-inference-strategies-and-search)
12. [Memoization, Tabling, and Rule Indexing](#12-memoization-tabling-and-rule-indexing)
13. [Constraints and Consistency](#13-constraints-and-consistency)
14. [Theorems, Proof Terms, and Soundness](#14-theorems-proof-terms-and-soundness)
15. [Symbolic Reasoning and Proof Normalization](#15-symbolic-reasoning-and-proof-normalization)
16. [Knowledge Bases and Planning Systems](#16-knowledge-bases-and-planning-systems)
17. [Scene and Timeline Rule Systems](#17-scene-and-timeline-rule-systems)
18. [Symbolic–Neural and Logic–Graph Integration](#18-symbolic-neural-and-logic-graph-integration)
19. [Functional Compiler Optimization](#19-functional-compiler-optimization)
20. [Proof-Carrying Transforms and R12/MCRT Lowering](#20-proof-carrying-transforms-and-r12-mcrt-lowering)
21. [Diagnostics, Safety, and Certification](#21-diagnostics-safety-and-certification)
22. [Smithson 8S Coupled Mechanics and the Capstone Toolchain](#22-smithson-8s-coupled-mechanics-and-the-capstone-toolchain)

## Notation and claim boundary

`deepml logic 0.3` denotes the modeled language version in the corpus. R12 and MCRT references are evidence identities and lowering relations represented by the source records. Smithson 8S Coupled Mechanics is presented as a proposed computational framework and provenance scheme, not an established physical law.

# 1. Orientation: Logic, Function, and Evidence

> **Corpus focus:** `expression`, `certification_logic`  
> **Representative record:** `EX-DMLL-00538` · tier `basic_syntax` · class `positive`

## Learning objectives

By the end of this chapter, the reader should be able to:

- Explain and apply **language identity**.
- Explain and apply **pure-by-default policy**.
- Explain and apply **corpus evidence planes**.
- Explain and apply **four-lens review**.

## Core idea

DeepML Logic/Functional treats source code as one layer of a larger evidence object. A construct is not complete merely because it parses: its type, purity, logical meaning, compiler identity, runtime behavior, diagnostics, and provenance must agree. In this chapter the key design space is language identity, pure-by-default policy, corpus evidence planes, and four-lens review. The practical discipline is to make each assumption explicit enough that another implementation can reproduce the same judgment without network access or hidden state.

The language's `pure_by_default` posture is architectural rather than decorative. It makes referential transparency the normal case, forces capabilities to appear at boundaries, and allows functions, rules, proofs, and compiler rewrites to be compared by semantic identity. Logic evaluation adds another dimension: operational search choices can affect termination and performance even when declarative meaning is stable. The corpus therefore records both denotational intent and operational evidence.

## Reading the evidence

A useful review separates four lenses:

- **SOPHIA:** Is the meaning coherent, typed, pure, and preserved?
- **CHARLOTTE:** Is the construct discoverable, consistently named, and represented across the corpus?
- **LANDON:** Can a compiler, validator, and runtime report deterministic evidence for it?
- **Professor + Podium:** Can a learner explain it, modify it, and diagnose its failure modes?

For `expression`, the source record explains: This beginner Logic Functional Language (DeepML) example teaches expression. It preserves the corpus-derived source → AST → typed/policy-verified semantic record → R12 → MCRT trace and uses deterministic IDs, hashes, provenance, and no-network safety. The example is expected to compile, lower, and produce deterministic runtime evidence.

## Worked corpus program

```deepml
deepml logic 0.3
module corpus.deepml_logic.example_00538
policy pure_by_default
policy no_network
type Option<T> = Some(T) | None
let value11: Int = 33
fn identity<T>(x: T) -> T = x
fn map_option<T,U>(f: T -> U, x: Option<T>) -> Option<U> = match x { Some(v) => Some(f(v)) None => None }
predicate even(x: Int) = x % 2 == 0
fact seed(538)
rule valid_seed(x) :- seed(x), even(x)
```

### What to inspect

- **Concepts:** expression, declare_expression, DEEPML_LOGIC_R12, R12, MCRT
- **Expected stage:** `runtime`
- **Expected result:** `pass`
- **Source identity:** `sha256:c1fbed46fc6dc03bcd5df8bc405cca881d433c157a9cbc92d754d637b46f4b08`
- **Semantic identity:** `sha256:8a88aa2f26dcce2dba113a46059e3082af73930aff644e75166dd83415f558fd`

Read the program top-down once for syntax, then bottom-up for obligations. The header establishes language identity; policies constrain effects; declarations introduce types, functions, relations, or proofs; and terminal operations expose evaluation, inference, transformation, or certification intent. A correct implementation should be able to explain not only whether the program succeeds, but why the reported stage is the first decisive stage.

## Engineering checklist

- [ ] The language version and module identity are explicit.
- [ ] All names resolve within declared namespace boundaries.
- [ ] Types and pattern alternatives are complete and coherent.
- [ ] Effects are absent or explicitly declared and authorized.
- [ ] Recursive definitions have a termination or bounded-resource argument.
- [ ] Logic search strategy is explicit where operational behavior matters.
- [ ] Compiler transformations carry preservation evidence.
- [ ] Expected diagnostics identify the earliest responsible stage.
- [ ] R12 and MCRT identities can be traced without network access.
- [ ] Certification claims are separated from ordinary training examples.

## Laboratory 1

1. Locate `EX-DMLL-00538` in the technical corpus and verify its source hash.
2. Copy the program into a local air-gapped workspace and annotate every declaration.
3. Create one valid variation that preserves the `expression` invariant.
4. Create one intentionally invalid variation and specify its expected failure stage.
5. Record the semantic identity, expected diagnostic, and replay evidence in a lab notebook.

### Deliverable

Submit the original record ID, the valid variation, the invalid variation, a one-page semantic comparison, and a validation table containing expected stage, result, diagnostic, source hash, and semantic hash.

## Review questions

1. Which semantic invariant is most important in `expression`?
2. What evidence would distinguish modeled behavior from native execution?
3. Which negative case should be added before certifying an implementation?
4. How do purity, determinism, and policy interact in this chapter?

## Further corpus study

Filter `catalogs/CORPUS_INDEX.csv` for: expression, certification_logic. Compare at least one positive, one negative, and—where available—one certification record. Identify which fields remain invariant across the three classes and which fields encode the expected failure.


# 2. Program Anatomy and Module Boundaries

> **Corpus focus:** `module`, `expression`  
> **Representative record:** `EX-DMLL-00634` · tier `basic_syntax` · class `positive`

## Learning objectives

By the end of this chapter, the reader should be able to:

- Explain and apply **version headers**.
- Explain and apply **modules**.
- Explain and apply **namespaces**.
- Explain and apply **policies**.
- Explain and apply **visibility**.

## Core idea

DeepML Logic/Functional treats source code as one layer of a larger evidence object. A construct is not complete merely because it parses: its type, purity, logical meaning, compiler identity, runtime behavior, diagnostics, and provenance must agree. In this chapter the key design space is version headers, modules, namespaces, policies, and visibility. The practical discipline is to make each assumption explicit enough that another implementation can reproduce the same judgment without network access or hidden state.

The language's `pure_by_default` posture is architectural rather than decorative. It makes referential transparency the normal case, forces capabilities to appear at boundaries, and allows functions, rules, proofs, and compiler rewrites to be compared by semantic identity. Logic evaluation adds another dimension: operational search choices can affect termination and performance even when declarative meaning is stable. The corpus therefore records both denotational intent and operational evidence.

## Reading the evidence

A useful review separates four lenses:

- **SOPHIA:** Is the meaning coherent, typed, pure, and preserved?
- **CHARLOTTE:** Is the construct discoverable, consistently named, and represented across the corpus?
- **LANDON:** Can a compiler, validator, and runtime report deterministic evidence for it?
- **Professor + Podium:** Can a learner explain it, modify it, and diagnose its failure modes?

For `expression`, the source record explains: This beginner Logic Functional Language (DeepML) example teaches expression. It preserves the corpus-derived source → AST → typed/policy-verified semantic record → R12 → MCRT trace and uses deterministic IDs, hashes, provenance, and no-network safety. The example is expected to compile, lower, and produce deterministic runtime evidence.

## Worked corpus program

```deepml
deepml logic 0.3
module corpus.deepml_logic.example_00634
policy pure_by_default
policy no_network
type Option<T> = Some(T) | None
let value5: Int = 28
fn identity<T>(x: T) -> T = x
fn map_option<T,U>(f: T -> U, x: Option<T>) -> Option<U> = match x { Some(v) => Some(f(v)) None => None }
predicate even(x: Int) = x % 2 == 0
fact seed(634)
rule valid_seed(x) :- seed(x), even(x)
```

### What to inspect

- **Concepts:** expression, declare_expression, DEEPML_LOGIC_R12, R12, MCRT
- **Expected stage:** `runtime`
- **Expected result:** `pass`
- **Source identity:** `sha256:97a50490a89b93d888ab103f1ec9f50e51a3779a1ab2a3d4cdc7990f9670cc53`
- **Semantic identity:** `sha256:389dababe48f88da30cf011ddad113544fb08ea7ec56c16d7e0e550436aab0e3`

Read the program top-down once for syntax, then bottom-up for obligations. The header establishes language identity; policies constrain effects; declarations introduce types, functions, relations, or proofs; and terminal operations expose evaluation, inference, transformation, or certification intent. A correct implementation should be able to explain not only whether the program succeeds, but why the reported stage is the first decisive stage.

## Engineering checklist

- [ ] The language version and module identity are explicit.
- [ ] All names resolve within declared namespace boundaries.
- [ ] Types and pattern alternatives are complete and coherent.
- [ ] Effects are absent or explicitly declared and authorized.
- [ ] Recursive definitions have a termination or bounded-resource argument.
- [ ] Logic search strategy is explicit where operational behavior matters.
- [ ] Compiler transformations carry preservation evidence.
- [ ] Expected diagnostics identify the earliest responsible stage.
- [ ] R12 and MCRT identities can be traced without network access.
- [ ] Certification claims are separated from ordinary training examples.

## Laboratory 2

1. Locate `EX-DMLL-00634` in the technical corpus and verify its source hash.
2. Copy the program into a local air-gapped workspace and annotate every declaration.
3. Create one valid variation that preserves the `expression` invariant.
4. Create one intentionally invalid variation and specify its expected failure stage.
5. Record the semantic identity, expected diagnostic, and replay evidence in a lab notebook.

### Deliverable

Submit the original record ID, the valid variation, the invalid variation, a one-page semantic comparison, and a validation table containing expected stage, result, diagnostic, source hash, and semantic hash.

## Review questions

1. Which semantic invariant is most important in `expression`?
2. What evidence would distinguish modeled behavior from native execution?
3. Which negative case should be added before certifying an implementation?
4. How do purity, determinism, and policy interact in this chapter?

## Further corpus study

Filter `catalogs/CORPUS_INDEX.csv` for: module, expression. Compare at least one positive, one negative, and—where available—one certification record. Identify which fields remain invariant across the three classes and which fields encode the expected failure.


# 3. Types and Algebraic Data

> **Corpus focus:** `algebraic_data_type`, `trait`  
> **Representative record:** `EX-DMLL-00652` · tier `basic_syntax` · class `positive`

## Learning objectives

By the end of this chapter, the reader should be able to:

- Explain and apply **sum types**.
- Explain and apply **product types**.
- Explain and apply **generics**.
- Explain and apply **constructors**.
- Explain and apply **type identity**.

## Core idea

DeepML Logic/Functional treats source code as one layer of a larger evidence object. A construct is not complete merely because it parses: its type, purity, logical meaning, compiler identity, runtime behavior, diagnostics, and provenance must agree. In this chapter the key design space is sum types, product types, generics, constructors, and type identity. The practical discipline is to make each assumption explicit enough that another implementation can reproduce the same judgment without network access or hidden state.

The language's `pure_by_default` posture is architectural rather than decorative. It makes referential transparency the normal case, forces capabilities to appear at boundaries, and allows functions, rules, proofs, and compiler rewrites to be compared by semantic identity. Logic evaluation adds another dimension: operational search choices can affect termination and performance even when declarative meaning is stable. The corpus therefore records both denotational intent and operational evidence.

## Reading the evidence

A useful review separates four lenses:

- **SOPHIA:** Is the meaning coherent, typed, pure, and preserved?
- **CHARLOTTE:** Is the construct discoverable, consistently named, and represented across the corpus?
- **LANDON:** Can a compiler, validator, and runtime report deterministic evidence for it?
- **Professor + Podium:** Can a learner explain it, modify it, and diagnose its failure modes?

For `algebraic_data_type`, the source record explains: This beginner Logic Functional Language (DeepML) example teaches algebraic data type. It preserves the corpus-derived source → AST → typed/policy-verified semantic record → R12 → MCRT trace and uses deterministic IDs, hashes, provenance, and no-network safety. The example is expected to compile, lower, and produce deterministic runtime evidence.

## Worked corpus program

```deepml
deepml logic 0.3
module corpus.deepml_logic.example_00652
policy pure_by_default
policy no_network
type Option<T> = Some(T) | None
let value6: Int = 46
fn identity<T>(x: T) -> T = x
fn map_option<T,U>(f: T -> U, x: Option<T>) -> Option<U> = match x { Some(v) => Some(f(v)) None => None }
predicate even(x: Int) = x % 2 == 0
fact seed(652)
rule valid_seed(x) :- seed(x), even(x)
```

### What to inspect

- **Concepts:** algebraic_data_type, declare_algebraic_data_type, DEEPML_LOGIC_R12, R12, MCRT
- **Expected stage:** `runtime`
- **Expected result:** `pass`
- **Source identity:** `sha256:1324509fa9377cc2f0f15cc2d6c2e218568321b190e4bac28eeb504a3f39451f`
- **Semantic identity:** `sha256:b6480d50461d60bf8290357b514d1df0b7bd0f682b6c89b64eb50f0754f8fb4a`

Read the program top-down once for syntax, then bottom-up for obligations. The header establishes language identity; policies constrain effects; declarations introduce types, functions, relations, or proofs; and terminal operations expose evaluation, inference, transformation, or certification intent. A correct implementation should be able to explain not only whether the program succeeds, but why the reported stage is the first decisive stage.

## Engineering checklist

- [ ] The language version and module identity are explicit.
- [ ] All names resolve within declared namespace boundaries.
- [ ] Types and pattern alternatives are complete and coherent.
- [ ] Effects are absent or explicitly declared and authorized.
- [ ] Recursive definitions have a termination or bounded-resource argument.
- [ ] Logic search strategy is explicit where operational behavior matters.
- [ ] Compiler transformations carry preservation evidence.
- [ ] Expected diagnostics identify the earliest responsible stage.
- [ ] R12 and MCRT identities can be traced without network access.
- [ ] Certification claims are separated from ordinary training examples.

## Laboratory 3

1. Locate `EX-DMLL-00652` in the technical corpus and verify its source hash.
2. Copy the program into a local air-gapped workspace and annotate every declaration.
3. Create one valid variation that preserves the `algebraic_data_type` invariant.
4. Create one intentionally invalid variation and specify its expected failure stage.
5. Record the semantic identity, expected diagnostic, and replay evidence in a lab notebook.

### Deliverable

Submit the original record ID, the valid variation, the invalid variation, a one-page semantic comparison, and a validation table containing expected stage, result, diagnostic, source hash, and semantic hash.

## Review questions

1. Which semantic invariant is most important in `algebraic_data_type`?
2. What evidence would distinguish modeled behavior from native execution?
3. Which negative case should be added before certifying an implementation?
4. How do purity, determinism, and policy interact in this chapter?

## Further corpus study

Filter `catalogs/CORPUS_INDEX.csv` for: algebraic_data_type, trait. Compare at least one positive, one negative, and—where available—one certification record. Identify which fields remain invariant across the three classes and which fields encode the expected failure.


# 4. Immutable Values and Expressions

> **Corpus focus:** `immutable_value`, `expression`  
> **Representative record:** `EX-DMLL-00195` · tier `basic_syntax` · class `positive`

## Learning objectives

By the end of this chapter, the reader should be able to:

- Explain and apply **bindings**.
- Explain and apply **operators**.
- Explain and apply **referential transparency**.
- Explain and apply **evaluation order**.

## Core idea

DeepML Logic/Functional treats source code as one layer of a larger evidence object. A construct is not complete merely because it parses: its type, purity, logical meaning, compiler identity, runtime behavior, diagnostics, and provenance must agree. In this chapter the key design space is bindings, operators, referential transparency, and evaluation order. The practical discipline is to make each assumption explicit enough that another implementation can reproduce the same judgment without network access or hidden state.

The language's `pure_by_default` posture is architectural rather than decorative. It makes referential transparency the normal case, forces capabilities to appear at boundaries, and allows functions, rules, proofs, and compiler rewrites to be compared by semantic identity. Logic evaluation adds another dimension: operational search choices can affect termination and performance even when declarative meaning is stable. The corpus therefore records both denotational intent and operational evidence.

## Reading the evidence

A useful review separates four lenses:

- **SOPHIA:** Is the meaning coherent, typed, pure, and preserved?
- **CHARLOTTE:** Is the construct discoverable, consistently named, and represented across the corpus?
- **LANDON:** Can a compiler, validator, and runtime report deterministic evidence for it?
- **Professor + Podium:** Can a learner explain it, modify it, and diagnose its failure modes?

For `immutable_value`, the source record explains: This beginner Logic Functional Language (DeepML) example teaches immutable value. It preserves the corpus-derived source → AST → typed/policy-verified semantic record → R12 → MCRT trace and uses deterministic IDs, hashes, provenance, and no-network safety. The example is expected to compile, lower, and produce deterministic runtime evidence.

## Worked corpus program

```deepml
deepml logic 0.3
module corpus.deepml_logic.example_00195
policy pure_by_default
policy no_network
type Option<T> = Some(T) | None
let value8: Int = 94
fn identity<T>(x: T) -> T = x
fn map_option<T,U>(f: T -> U, x: Option<T>) -> Option<U> = match x { Some(v) => Some(f(v)) None => None }
predicate even(x: Int) = x % 2 == 0
fact seed(195)
rule valid_seed(x) :- seed(x), even(x)
```

### What to inspect

- **Concepts:** immutable_value, declare_immutable_value, DEEPML_LOGIC_R12, R12, MCRT
- **Expected stage:** `runtime`
- **Expected result:** `pass`
- **Source identity:** `sha256:71aa1d8a1e32861d452d6f287f8fc3f07321dbc10941ab1f624723df5f3edb06`
- **Semantic identity:** `sha256:19026a7ed43970df128920ecc20c96632e1ce136a07703f51563865f6ab8a828`

Read the program top-down once for syntax, then bottom-up for obligations. The header establishes language identity; policies constrain effects; declarations introduce types, functions, relations, or proofs; and terminal operations expose evaluation, inference, transformation, or certification intent. A correct implementation should be able to explain not only whether the program succeeds, but why the reported stage is the first decisive stage.

## Engineering checklist

- [ ] The language version and module identity are explicit.
- [ ] All names resolve within declared namespace boundaries.
- [ ] Types and pattern alternatives are complete and coherent.
- [ ] Effects are absent or explicitly declared and authorized.
- [ ] Recursive definitions have a termination or bounded-resource argument.
- [ ] Logic search strategy is explicit where operational behavior matters.
- [ ] Compiler transformations carry preservation evidence.
- [ ] Expected diagnostics identify the earliest responsible stage.
- [ ] R12 and MCRT identities can be traced without network access.
- [ ] Certification claims are separated from ordinary training examples.

## Laboratory 4

1. Locate `EX-DMLL-00195` in the technical corpus and verify its source hash.
2. Copy the program into a local air-gapped workspace and annotate every declaration.
3. Create one valid variation that preserves the `immutable_value` invariant.
4. Create one intentionally invalid variation and specify its expected failure stage.
5. Record the semantic identity, expected diagnostic, and replay evidence in a lab notebook.

### Deliverable

Submit the original record ID, the valid variation, the invalid variation, a one-page semantic comparison, and a validation table containing expected stage, result, diagnostic, source hash, and semantic hash.

## Review questions

1. Which semantic invariant is most important in `immutable_value`?
2. What evidence would distinguish modeled behavior from native execution?
3. Which negative case should be added before certifying an implementation?
4. How do purity, determinism, and policy interact in this chapter?

## Further corpus study

Filter `catalogs/CORPUS_INDEX.csv` for: immutable_value, expression. Compare at least one positive, one negative, and—where available—one certification record. Identify which fields remain invariant across the three classes and which fields encode the expected failure.


# 5. Pure Functions, Lambdas, and Closures

> **Corpus focus:** `pure_function`, `lambda`, `higher_order_function`  
> **Representative record:** `EX-DMLL-00414` · tier `basic_syntax` · class `positive`

## Learning objectives

By the end of this chapter, the reader should be able to:

- Explain and apply **function types**.
- Explain and apply **lexical scope**.
- Explain and apply **higher-order values**.
- Explain and apply **composition**.

## Core idea

DeepML Logic/Functional treats source code as one layer of a larger evidence object. A construct is not complete merely because it parses: its type, purity, logical meaning, compiler identity, runtime behavior, diagnostics, and provenance must agree. In this chapter the key design space is function types, lexical scope, higher-order values, and composition. The practical discipline is to make each assumption explicit enough that another implementation can reproduce the same judgment without network access or hidden state.

The language's `pure_by_default` posture is architectural rather than decorative. It makes referential transparency the normal case, forces capabilities to appear at boundaries, and allows functions, rules, proofs, and compiler rewrites to be compared by semantic identity. Logic evaluation adds another dimension: operational search choices can affect termination and performance even when declarative meaning is stable. The corpus therefore records both denotational intent and operational evidence.

## Reading the evidence

A useful review separates four lenses:

- **SOPHIA:** Is the meaning coherent, typed, pure, and preserved?
- **CHARLOTTE:** Is the construct discoverable, consistently named, and represented across the corpus?
- **LANDON:** Can a compiler, validator, and runtime report deterministic evidence for it?
- **Professor + Podium:** Can a learner explain it, modify it, and diagnose its failure modes?

For `lambda`, the source record explains: This beginner Logic Functional Language (DeepML) example teaches lambda. It preserves the corpus-derived source → AST → typed/policy-verified semantic record → R12 → MCRT trace and uses deterministic IDs, hashes, provenance, and no-network safety. The example is expected to compile, lower, and produce deterministic runtime evidence.

## Worked corpus program

```deepml
deepml logic 0.3
module corpus.deepml_logic.example_00414
policy pure_by_default
policy no_network
type Option<T> = Some(T) | None
let value6: Int = 10
fn identity<T>(x: T) -> T = x
fn map_option<T,U>(f: T -> U, x: Option<T>) -> Option<U> = match x { Some(v) => Some(f(v)) None => None }
predicate even(x: Int) = x % 2 == 0
fact seed(414)
rule valid_seed(x) :- seed(x), even(x)
```

### What to inspect

- **Concepts:** lambda, declare_lambda, DEEPML_LOGIC_R12, R12, MCRT
- **Expected stage:** `runtime`
- **Expected result:** `pass`
- **Source identity:** `sha256:3d461b3ef358b5fdeab10db4c8b36e7898086c7def956a67e47d32aad29c8455`
- **Semantic identity:** `sha256:9027f3c2e7747d385df8f1d90b9ee66c2a234c7ba670005387e2a7b7655fc5f8`

Read the program top-down once for syntax, then bottom-up for obligations. The header establishes language identity; policies constrain effects; declarations introduce types, functions, relations, or proofs; and terminal operations expose evaluation, inference, transformation, or certification intent. A correct implementation should be able to explain not only whether the program succeeds, but why the reported stage is the first decisive stage.

## Engineering checklist

- [ ] The language version and module identity are explicit.
- [ ] All names resolve within declared namespace boundaries.
- [ ] Types and pattern alternatives are complete and coherent.
- [ ] Effects are absent or explicitly declared and authorized.
- [ ] Recursive definitions have a termination or bounded-resource argument.
- [ ] Logic search strategy is explicit where operational behavior matters.
- [ ] Compiler transformations carry preservation evidence.
- [ ] Expected diagnostics identify the earliest responsible stage.
- [ ] R12 and MCRT identities can be traced without network access.
- [ ] Certification claims are separated from ordinary training examples.

## Laboratory 5

1. Locate `EX-DMLL-00414` in the technical corpus and verify its source hash.
2. Copy the program into a local air-gapped workspace and annotate every declaration.
3. Create one valid variation that preserves the `lambda` invariant.
4. Create one intentionally invalid variation and specify its expected failure stage.
5. Record the semantic identity, expected diagnostic, and replay evidence in a lab notebook.

### Deliverable

Submit the original record ID, the valid variation, the invalid variation, a one-page semantic comparison, and a validation table containing expected stage, result, diagnostic, source hash, and semantic hash.

## Review questions

1. Which semantic invariant is most important in `lambda`?
2. What evidence would distinguish modeled behavior from native execution?
3. Which negative case should be added before certifying an implementation?
4. How do purity, determinism, and policy interact in this chapter?

## Further corpus study

Filter `catalogs/CORPUS_INDEX.csv` for: pure_function, lambda, higher_order_function. Compare at least one positive, one negative, and—where available—one certification record. Identify which fields remain invariant across the three classes and which fields encode the expected failure.


# 6. Pattern Matching and Guards

> **Corpus focus:** `pattern_match`, `guard`, `incomplete_match`  
> **Representative record:** `EX-DMLL-00681` · tier `basic_syntax` · class `positive`

## Learning objectives

By the end of this chapter, the reader should be able to:

- Explain and apply **destructuring**.
- Explain and apply **exhaustiveness**.
- Explain and apply **guards**.
- Explain and apply **incomplete matches**.

## Core idea

DeepML Logic/Functional treats source code as one layer of a larger evidence object. A construct is not complete merely because it parses: its type, purity, logical meaning, compiler identity, runtime behavior, diagnostics, and provenance must agree. In this chapter the key design space is destructuring, exhaustiveness, guards, and incomplete matches. The practical discipline is to make each assumption explicit enough that another implementation can reproduce the same judgment without network access or hidden state.

The language's `pure_by_default` posture is architectural rather than decorative. It makes referential transparency the normal case, forces capabilities to appear at boundaries, and allows functions, rules, proofs, and compiler rewrites to be compared by semantic identity. Logic evaluation adds another dimension: operational search choices can affect termination and performance even when declarative meaning is stable. The corpus therefore records both denotational intent and operational evidence.

## Reading the evidence

A useful review separates four lenses:

- **SOPHIA:** Is the meaning coherent, typed, pure, and preserved?
- **CHARLOTTE:** Is the construct discoverable, consistently named, and represented across the corpus?
- **LANDON:** Can a compiler, validator, and runtime report deterministic evidence for it?
- **Professor + Podium:** Can a learner explain it, modify it, and diagnose its failure modes?

For `pattern_match`, the source record explains: This beginner Logic Functional Language (DeepML) example teaches pattern match. It preserves the corpus-derived source → AST → typed/policy-verified semantic record → R12 → MCRT trace and uses deterministic IDs, hashes, provenance, and no-network safety. The example is expected to compile, lower, and produce deterministic runtime evidence.

## Worked corpus program

```deepml
deepml logic 0.3
module corpus.deepml_logic.example_00681
policy pure_by_default
policy no_network
type Option<T> = Some(T) | None
let value1: Int = 75
fn identity<T>(x: T) -> T = x
fn map_option<T,U>(f: T -> U, x: Option<T>) -> Option<U> = match x { Some(v) => Some(f(v)) None => None }
predicate even(x: Int) = x % 2 == 0
fact seed(681)
rule valid_seed(x) :- seed(x), even(x)
```

### What to inspect

- **Concepts:** pattern_match, declare_pattern_match, DEEPML_LOGIC_R12, R12, MCRT
- **Expected stage:** `runtime`
- **Expected result:** `pass`
- **Source identity:** `sha256:e2fa84acc71516656754ce35e6b701c46fd696e41f5322843687ebcf63d4bddd`
- **Semantic identity:** `sha256:dda7c2e4100c95458b640533199c742b55b237d67493e27e2be0c5066c9ffc96`

Read the program top-down once for syntax, then bottom-up for obligations. The header establishes language identity; policies constrain effects; declarations introduce types, functions, relations, or proofs; and terminal operations expose evaluation, inference, transformation, or certification intent. A correct implementation should be able to explain not only whether the program succeeds, but why the reported stage is the first decisive stage.

## Engineering checklist

- [ ] The language version and module identity are explicit.
- [ ] All names resolve within declared namespace boundaries.
- [ ] Types and pattern alternatives are complete and coherent.
- [ ] Effects are absent or explicitly declared and authorized.
- [ ] Recursive definitions have a termination or bounded-resource argument.
- [ ] Logic search strategy is explicit where operational behavior matters.
- [ ] Compiler transformations carry preservation evidence.
- [ ] Expected diagnostics identify the earliest responsible stage.
- [ ] R12 and MCRT identities can be traced without network access.
- [ ] Certification claims are separated from ordinary training examples.

## Laboratory 6

1. Locate `EX-DMLL-00681` in the technical corpus and verify its source hash.
2. Copy the program into a local air-gapped workspace and annotate every declaration.
3. Create one valid variation that preserves the `pattern_match` invariant.
4. Create one intentionally invalid variation and specify its expected failure stage.
5. Record the semantic identity, expected diagnostic, and replay evidence in a lab notebook.

### Deliverable

Submit the original record ID, the valid variation, the invalid variation, a one-page semantic comparison, and a validation table containing expected stage, result, diagnostic, source hash, and semantic hash.

## Review questions

1. Which semantic invariant is most important in `pattern_match`?
2. What evidence would distinguish modeled behavior from native execution?
3. Which negative case should be added before certifying an implementation?
4. How do purity, determinism, and policy interact in this chapter?

## Further corpus study

Filter `catalogs/CORPUS_INDEX.csv` for: pattern_match, guard, incomplete_match. Compare at least one positive, one negative, and—where available—one certification record. Identify which fields remain invariant across the three classes and which fields encode the expected failure.


# 7. Recursion, Folds, and Termination

> **Corpus focus:** `recursion`, `fold`, `tail_call`, `nontermination`  
> **Representative record:** `EX-DMLL-01472` · tier `intermediate_constructs` · class `positive`

## Learning objectives

By the end of this chapter, the reader should be able to:

- Explain and apply **structural recursion**.
- Explain and apply **folds**.
- Explain and apply **tail position**.
- Explain and apply **decreasing measures**.
- Explain and apply **nontermination**.

## Core idea

DeepML Logic/Functional treats source code as one layer of a larger evidence object. A construct is not complete merely because it parses: its type, purity, logical meaning, compiler identity, runtime behavior, diagnostics, and provenance must agree. In this chapter the key design space is structural recursion, folds, tail position, decreasing measures, and nontermination. The practical discipline is to make each assumption explicit enough that another implementation can reproduce the same judgment without network access or hidden state.

The language's `pure_by_default` posture is architectural rather than decorative. It makes referential transparency the normal case, forces capabilities to appear at boundaries, and allows functions, rules, proofs, and compiler rewrites to be compared by semantic identity. Logic evaluation adds another dimension: operational search choices can affect termination and performance even when declarative meaning is stable. The corpus therefore records both denotational intent and operational evidence.

## Reading the evidence

A useful review separates four lenses:

- **SOPHIA:** Is the meaning coherent, typed, pure, and preserved?
- **CHARLOTTE:** Is the construct discoverable, consistently named, and represented across the corpus?
- **LANDON:** Can a compiler, validator, and runtime report deterministic evidence for it?
- **Professor + Podium:** Can a learner explain it, modify it, and diagnose its failure modes?

For `fold`, the source record explains: This intermediate Logic Functional Language (DeepML) example teaches fold. It preserves the corpus-derived source → AST → typed/policy-verified semantic record → R12 → MCRT trace and uses deterministic IDs, hashes, provenance, and no-network safety. The example is expected to compile, lower, and produce deterministic runtime evidence.

## Worked corpus program

```deepml
deepml logic 0.3
module corpus.deepml_logic.example_01472
policy pure_by_default
policy no_network
trait Monoid<T> { fn empty() -> T fn combine(a:T,b:T)->T }
fn fold<T,U>(f: (U,T)->U, init: U, xs: List<T>) -> U = match xs { [] => init [h|t] => fold(f, f(init,h), t) }
fn factorial(n:Int)->Int = if n <= 1 then 1 else n * factorial(n-1)
predicate parent(A,B)
rule ancestor(A,B) :- parent(A,B)
rule ancestor(A,C) :- parent(A,B), ancestor(B,C)
query ancestor("node2", X) strategy tabled
effect IO declared but not used
```

### What to inspect

- **Concepts:** fold, compose_fold, DEEPML_LOGIC_R12, R12, MCRT
- **Expected stage:** `runtime`
- **Expected result:** `pass`
- **Source identity:** `sha256:f31eb856dab6d8e0596e1c4f2d734adac80ab23e2a4ff5926e7006102f4fef32`
- **Semantic identity:** `sha256:b19b98bb885975226b0ec2207c0c352b7049535b1e40a3cfb0c3962280c213c8`

Read the program top-down once for syntax, then bottom-up for obligations. The header establishes language identity; policies constrain effects; declarations introduce types, functions, relations, or proofs; and terminal operations expose evaluation, inference, transformation, or certification intent. A correct implementation should be able to explain not only whether the program succeeds, but why the reported stage is the first decisive stage.

## Engineering checklist

- [ ] The language version and module identity are explicit.
- [ ] All names resolve within declared namespace boundaries.
- [ ] Types and pattern alternatives are complete and coherent.
- [ ] Effects are absent or explicitly declared and authorized.
- [ ] Recursive definitions have a termination or bounded-resource argument.
- [ ] Logic search strategy is explicit where operational behavior matters.
- [ ] Compiler transformations carry preservation evidence.
- [ ] Expected diagnostics identify the earliest responsible stage.
- [ ] R12 and MCRT identities can be traced without network access.
- [ ] Certification claims are separated from ordinary training examples.

## Laboratory 7

1. Locate `EX-DMLL-01472` in the technical corpus and verify its source hash.
2. Copy the program into a local air-gapped workspace and annotate every declaration.
3. Create one valid variation that preserves the `fold` invariant.
4. Create one intentionally invalid variation and specify its expected failure stage.
5. Record the semantic identity, expected diagnostic, and replay evidence in a lab notebook.

### Deliverable

Submit the original record ID, the valid variation, the invalid variation, a one-page semantic comparison, and a validation table containing expected stage, result, diagnostic, source hash, and semantic hash.

## Review questions

1. Which semantic invariant is most important in `fold`?
2. What evidence would distinguish modeled behavior from native execution?
3. Which negative case should be added before certifying an implementation?
4. How do purity, determinism, and policy interact in this chapter?

## Further corpus study

Filter `catalogs/CORPUS_INDEX.csv` for: recursion, fold, tail_call, nontermination. Compare at least one positive, one negative, and—where available—one certification record. Identify which fields remain invariant across the three classes and which fields encode the expected failure.


# 8. Traits, Instances, Effects, and Capabilities

> **Corpus focus:** `trait`, `ambiguous_instance`, `effect_declaration`, `impure_effect`  
> **Representative record:** `EX-DMLL-01270` · tier `intermediate_constructs` · class `positive`

## Learning objectives

By the end of this chapter, the reader should be able to:

- Explain and apply **trait resolution**.
- Explain and apply **coherence**.
- Explain and apply **ambiguous instances**.
- Explain and apply **effect declarations**.
- Explain and apply **policy gates**.

## Core idea

DeepML Logic/Functional treats source code as one layer of a larger evidence object. A construct is not complete merely because it parses: its type, purity, logical meaning, compiler identity, runtime behavior, diagnostics, and provenance must agree. In this chapter the key design space is trait resolution, coherence, ambiguous instances, effect declarations, and policy gates. The practical discipline is to make each assumption explicit enough that another implementation can reproduce the same judgment without network access or hidden state.

The language's `pure_by_default` posture is architectural rather than decorative. It makes referential transparency the normal case, forces capabilities to appear at boundaries, and allows functions, rules, proofs, and compiler rewrites to be compared by semantic identity. Logic evaluation adds another dimension: operational search choices can affect termination and performance even when declarative meaning is stable. The corpus therefore records both denotational intent and operational evidence.

## Reading the evidence

A useful review separates four lenses:

- **SOPHIA:** Is the meaning coherent, typed, pure, and preserved?
- **CHARLOTTE:** Is the construct discoverable, consistently named, and represented across the corpus?
- **LANDON:** Can a compiler, validator, and runtime report deterministic evidence for it?
- **Professor + Podium:** Can a learner explain it, modify it, and diagnose its failure modes?

For `trait`, the source record explains: This intermediate Logic Functional Language (DeepML) example teaches trait. It preserves the corpus-derived source → AST → typed/policy-verified semantic record → R12 → MCRT trace and uses deterministic IDs, hashes, provenance, and no-network safety. The example is expected to compile, lower, and produce deterministic runtime evidence.

## Worked corpus program

```deepml
deepml logic 0.3
module corpus.deepml_logic.example_01270
policy pure_by_default
policy no_network
trait Monoid<T> { fn empty() -> T fn combine(a:T,b:T)->T }
fn fold<T,U>(f: (U,T)->U, init: U, xs: List<T>) -> U = match xs { [] => init [h|t] => fold(f, f(init,h), t) }
fn factorial(n:Int)->Int = if n <= 1 then 1 else n * factorial(n-1)
predicate parent(A,B)
rule ancestor(A,B) :- parent(A,B)
rule ancestor(A,C) :- parent(A,B), ancestor(B,C)
query ancestor("node3", X) strategy tabled
effect IO declared but not used
```

### What to inspect

- **Concepts:** trait, compose_trait, DEEPML_LOGIC_R12, R12, MCRT
- **Expected stage:** `runtime`
- **Expected result:** `pass`
- **Source identity:** `sha256:db931371cfefca5094f9403672d2760b8506e9d32a0c40356d4b365b92887640`
- **Semantic identity:** `sha256:e156ab86c7aac21ba84adf9b5c7fea2b04df2d61fa239d0cae124b50697e1ff7`

Read the program top-down once for syntax, then bottom-up for obligations. The header establishes language identity; policies constrain effects; declarations introduce types, functions, relations, or proofs; and terminal operations expose evaluation, inference, transformation, or certification intent. A correct implementation should be able to explain not only whether the program succeeds, but why the reported stage is the first decisive stage.

## Engineering checklist

- [ ] The language version and module identity are explicit.
- [ ] All names resolve within declared namespace boundaries.
- [ ] Types and pattern alternatives are complete and coherent.
- [ ] Effects are absent or explicitly declared and authorized.
- [ ] Recursive definitions have a termination or bounded-resource argument.
- [ ] Logic search strategy is explicit where operational behavior matters.
- [ ] Compiler transformations carry preservation evidence.
- [ ] Expected diagnostics identify the earliest responsible stage.
- [ ] R12 and MCRT identities can be traced without network access.
- [ ] Certification claims are separated from ordinary training examples.

## Laboratory 8

1. Locate `EX-DMLL-01270` in the technical corpus and verify its source hash.
2. Copy the program into a local air-gapped workspace and annotate every declaration.
3. Create one valid variation that preserves the `trait` invariant.
4. Create one intentionally invalid variation and specify its expected failure stage.
5. Record the semantic identity, expected diagnostic, and replay evidence in a lab notebook.

### Deliverable

Submit the original record ID, the valid variation, the invalid variation, a one-page semantic comparison, and a validation table containing expected stage, result, diagnostic, source hash, and semantic hash.

## Review questions

1. Which semantic invariant is most important in `trait`?
2. What evidence would distinguish modeled behavior from native execution?
3. Which negative case should be added before certifying an implementation?
4. How do purity, determinism, and policy interact in this chapter?

## Further corpus study

Filter `catalogs/CORPUS_INDEX.csv` for: trait, ambiguous_instance, effect_declaration, impure_effect. Compare at least one positive, one negative, and—where available—one certification record. Identify which fields remain invariant across the three classes and which fields encode the expected failure.


# 9. Predicates, Facts, and Rules

> **Corpus focus:** `predicate`, `fact`, `rule`  
> **Representative record:** `EX-DMLL-00431` · tier `basic_syntax` · class `positive`

## Learning objectives

By the end of this chapter, the reader should be able to:

- Explain and apply **relations**.
- Explain and apply **ground facts**.
- Explain and apply **Horn-style rules**.
- Explain and apply **queries**.

## Core idea

DeepML Logic/Functional treats source code as one layer of a larger evidence object. A construct is not complete merely because it parses: its type, purity, logical meaning, compiler identity, runtime behavior, diagnostics, and provenance must agree. In this chapter the key design space is relations, ground facts, Horn-style rules, and queries. The practical discipline is to make each assumption explicit enough that another implementation can reproduce the same judgment without network access or hidden state.

The language's `pure_by_default` posture is architectural rather than decorative. It makes referential transparency the normal case, forces capabilities to appear at boundaries, and allows functions, rules, proofs, and compiler rewrites to be compared by semantic identity. Logic evaluation adds another dimension: operational search choices can affect termination and performance even when declarative meaning is stable. The corpus therefore records both denotational intent and operational evidence.

## Reading the evidence

A useful review separates four lenses:

- **SOPHIA:** Is the meaning coherent, typed, pure, and preserved?
- **CHARLOTTE:** Is the construct discoverable, consistently named, and represented across the corpus?
- **LANDON:** Can a compiler, validator, and runtime report deterministic evidence for it?
- **Professor + Podium:** Can a learner explain it, modify it, and diagnose its failure modes?

For `predicate`, the source record explains: This beginner Logic Functional Language (DeepML) example teaches predicate. It preserves the corpus-derived source → AST → typed/policy-verified semantic record → R12 → MCRT trace and uses deterministic IDs, hashes, provenance, and no-network safety. The example is expected to compile, lower, and produce deterministic runtime evidence.

## Worked corpus program

```deepml
deepml logic 0.3
module corpus.deepml_logic.example_00431
policy pure_by_default
policy no_network
type Option<T> = Some(T) | None
let value6: Int = 27
fn identity<T>(x: T) -> T = x
fn map_option<T,U>(f: T -> U, x: Option<T>) -> Option<U> = match x { Some(v) => Some(f(v)) None => None }
predicate even(x: Int) = x % 2 == 0
fact seed(431)
rule valid_seed(x) :- seed(x), even(x)
```

### What to inspect

- **Concepts:** predicate, declare_predicate, DEEPML_LOGIC_R12, R12, MCRT
- **Expected stage:** `runtime`
- **Expected result:** `pass`
- **Source identity:** `sha256:1879a3b78075dfd635d3aa7917c1ebb31033bbc93c273f760edb71ead5665aaf`
- **Semantic identity:** `sha256:c50fd176ca8eaaeb43d6e75c405e10e097862517dcd81bc061b257392a7049e6`

Read the program top-down once for syntax, then bottom-up for obligations. The header establishes language identity; policies constrain effects; declarations introduce types, functions, relations, or proofs; and terminal operations expose evaluation, inference, transformation, or certification intent. A correct implementation should be able to explain not only whether the program succeeds, but why the reported stage is the first decisive stage.

## Engineering checklist

- [ ] The language version and module identity are explicit.
- [ ] All names resolve within declared namespace boundaries.
- [ ] Types and pattern alternatives are complete and coherent.
- [ ] Effects are absent or explicitly declared and authorized.
- [ ] Recursive definitions have a termination or bounded-resource argument.
- [ ] Logic search strategy is explicit where operational behavior matters.
- [ ] Compiler transformations carry preservation evidence.
- [ ] Expected diagnostics identify the earliest responsible stage.
- [ ] R12 and MCRT identities can be traced without network access.
- [ ] Certification claims are separated from ordinary training examples.

## Laboratory 9

1. Locate `EX-DMLL-00431` in the technical corpus and verify its source hash.
2. Copy the program into a local air-gapped workspace and annotate every declaration.
3. Create one valid variation that preserves the `predicate` invariant.
4. Create one intentionally invalid variation and specify its expected failure stage.
5. Record the semantic identity, expected diagnostic, and replay evidence in a lab notebook.

### Deliverable

Submit the original record ID, the valid variation, the invalid variation, a one-page semantic comparison, and a validation table containing expected stage, result, diagnostic, source hash, and semantic hash.

## Review questions

1. Which semantic invariant is most important in `predicate`?
2. What evidence would distinguish modeled behavior from native execution?
3. Which negative case should be added before certifying an implementation?
4. How do purity, determinism, and policy interact in this chapter?

## Further corpus study

Filter `catalogs/CORPUS_INDEX.csv` for: predicate, fact, rule. Compare at least one positive, one negative, and—where available—one certification record. Identify which fields remain invariant across the three classes and which fields encode the expected failure.


# 10. Unification and the Occurs Check

> **Corpus focus:** `unification`, `occurs_check`  
> **Representative record:** `EX-DMLL-01282` · tier `intermediate_constructs` · class `positive`

## Learning objectives

By the end of this chapter, the reader should be able to:

- Explain and apply **substitution**.
- Explain and apply **term structure**.
- Explain and apply **most-general unifiers**.
- Explain and apply **infinite terms**.

## Core idea

DeepML Logic/Functional treats source code as one layer of a larger evidence object. A construct is not complete merely because it parses: its type, purity, logical meaning, compiler identity, runtime behavior, diagnostics, and provenance must agree. In this chapter the key design space is substitution, term structure, most-general unifiers, and infinite terms. The practical discipline is to make each assumption explicit enough that another implementation can reproduce the same judgment without network access or hidden state.

The language's `pure_by_default` posture is architectural rather than decorative. It makes referential transparency the normal case, forces capabilities to appear at boundaries, and allows functions, rules, proofs, and compiler rewrites to be compared by semantic identity. Logic evaluation adds another dimension: operational search choices can affect termination and performance even when declarative meaning is stable. The corpus therefore records both denotational intent and operational evidence.

## Reading the evidence

A useful review separates four lenses:

- **SOPHIA:** Is the meaning coherent, typed, pure, and preserved?
- **CHARLOTTE:** Is the construct discoverable, consistently named, and represented across the corpus?
- **LANDON:** Can a compiler, validator, and runtime report deterministic evidence for it?
- **Professor + Podium:** Can a learner explain it, modify it, and diagnose its failure modes?

For `unification`, the source record explains: This intermediate Logic Functional Language (DeepML) example teaches unification. It preserves the corpus-derived source → AST → typed/policy-verified semantic record → R12 → MCRT trace and uses deterministic IDs, hashes, provenance, and no-network safety. The example is expected to compile, lower, and produce deterministic runtime evidence.

## Worked corpus program

```deepml
deepml logic 0.3
module corpus.deepml_logic.example_01282
policy pure_by_default
policy no_network
trait Monoid<T> { fn empty() -> T fn combine(a:T,b:T)->T }
fn fold<T,U>(f: (U,T)->U, init: U, xs: List<T>) -> U = match xs { [] => init [h|t] => fold(f, f(init,h), t) }
fn factorial(n:Int)->Int = if n <= 1 then 1 else n * factorial(n-1)
predicate parent(A,B)
rule ancestor(A,B) :- parent(A,B)
rule ancestor(A,C) :- parent(A,B), ancestor(B,C)
query ancestor("node1", X) strategy tabled
effect IO declared but not used
```

### What to inspect

- **Concepts:** unification, compose_unification, DEEPML_LOGIC_R12, R12, MCRT
- **Expected stage:** `runtime`
- **Expected result:** `pass`
- **Source identity:** `sha256:9772328d71ff32072f99875d14b7a83518bbfa342c5f0914ec4105fc3e6f5cf4`
- **Semantic identity:** `sha256:696a3a4de9bccf53ee9c6adfcbd96c6d05f0b7068bc3a6675d8c5cf5e28312be`

Read the program top-down once for syntax, then bottom-up for obligations. The header establishes language identity; policies constrain effects; declarations introduce types, functions, relations, or proofs; and terminal operations expose evaluation, inference, transformation, or certification intent. A correct implementation should be able to explain not only whether the program succeeds, but why the reported stage is the first decisive stage.

## Engineering checklist

- [ ] The language version and module identity are explicit.
- [ ] All names resolve within declared namespace boundaries.
- [ ] Types and pattern alternatives are complete and coherent.
- [ ] Effects are absent or explicitly declared and authorized.
- [ ] Recursive definitions have a termination or bounded-resource argument.
- [ ] Logic search strategy is explicit where operational behavior matters.
- [ ] Compiler transformations carry preservation evidence.
- [ ] Expected diagnostics identify the earliest responsible stage.
- [ ] R12 and MCRT identities can be traced without network access.
- [ ] Certification claims are separated from ordinary training examples.

## Laboratory 10

1. Locate `EX-DMLL-01282` in the technical corpus and verify its source hash.
2. Copy the program into a local air-gapped workspace and annotate every declaration.
3. Create one valid variation that preserves the `unification` invariant.
4. Create one intentionally invalid variation and specify its expected failure stage.
5. Record the semantic identity, expected diagnostic, and replay evidence in a lab notebook.

### Deliverable

Submit the original record ID, the valid variation, the invalid variation, a one-page semantic comparison, and a validation table containing expected stage, result, diagnostic, source hash, and semantic hash.

## Review questions

1. Which semantic invariant is most important in `unification`?
2. What evidence would distinguish modeled behavior from native execution?
3. Which negative case should be added before certifying an implementation?
4. How do purity, determinism, and policy interact in this chapter?

## Further corpus study

Filter `catalogs/CORPUS_INDEX.csv` for: unification, occurs_check. Compare at least one positive, one negative, and—where available—one certification record. Identify which fields remain invariant across the three classes and which fields encode the expected failure.


# 11. Inference Strategies and Search

> **Corpus focus:** `inference_strategy`, `inference_divergence`  
> **Representative record:** `EX-DMLL-03003` · tier `advanced_composition` · class `positive`

## Learning objectives

By the end of this chapter, the reader should be able to:

- Explain and apply **depth-first search**.
- Explain and apply **best-first search**.
- Explain and apply **goal ordering**.
- Explain and apply **divergence**.

## Core idea

DeepML Logic/Functional treats source code as one layer of a larger evidence object. A construct is not complete merely because it parses: its type, purity, logical meaning, compiler identity, runtime behavior, diagnostics, and provenance must agree. In this chapter the key design space is depth-first search, best-first search, goal ordering, and divergence. The practical discipline is to make each assumption explicit enough that another implementation can reproduce the same judgment without network access or hidden state.

The language's `pure_by_default` posture is architectural rather than decorative. It makes referential transparency the normal case, forces capabilities to appear at boundaries, and allows functions, rules, proofs, and compiler rewrites to be compared by semantic identity. Logic evaluation adds another dimension: operational search choices can affect termination and performance even when declarative meaning is stable. The corpus therefore records both denotational intent and operational evidence.

## Reading the evidence

A useful review separates four lenses:

- **SOPHIA:** Is the meaning coherent, typed, pure, and preserved?
- **CHARLOTTE:** Is the construct discoverable, consistently named, and represented across the corpus?
- **LANDON:** Can a compiler, validator, and runtime report deterministic evidence for it?
- **Professor + Podium:** Can a learner explain it, modify it, and diagnose its failure modes?

For `inference_strategy`, the source record explains: This advanced Logic Functional Language (DeepML) example teaches inference strategy. It preserves the corpus-derived source → AST → typed/policy-verified semantic record → R12 → MCRT trace and uses deterministic IDs, hashes, provenance, and no-network safety. The example is expected to compile, lower, and produce deterministic runtime evidence.

## Worked corpus program

```deepml
deepml logic 0.3
module corpus.deepml_logic.example_03003
policy pure_by_default
policy no_network
theorem identity_composition<T>(f:T->T) : compose(identity,f) == f
proof identity_composition { extensionality x simplify identity qed }
constraint schedule(X,Y) { X >= 0 Y >= X + 4 }
predicate reachable(A,B)
rule reachable(A,B) :- edge(A,B)
rule reachable(A,C) :- edge(A,B), reachable(B,C)
infer reachable("start", Goal) strategy best_first memoize true
integrate graph Knowledge03003 from facts and rules
```

### What to inspect

- **Concepts:** inference_strategy, compose_inference_strategy, DEEPML_LOGIC_R12, R12, MCRT
- **Expected stage:** `runtime`
- **Expected result:** `pass`
- **Source identity:** `sha256:fce046b77cc2ea1798bc9fb907143bfcd4c13c98d8a5b2b5d0df6ebe5be905e1`
- **Semantic identity:** `sha256:a5c2dabe2944e5e3bb0f39883454536a188004b16ee1a1214dfed35ab4ea0ed0`

Read the program top-down once for syntax, then bottom-up for obligations. The header establishes language identity; policies constrain effects; declarations introduce types, functions, relations, or proofs; and terminal operations expose evaluation, inference, transformation, or certification intent. A correct implementation should be able to explain not only whether the program succeeds, but why the reported stage is the first decisive stage.

## Engineering checklist

- [ ] The language version and module identity are explicit.
- [ ] All names resolve within declared namespace boundaries.
- [ ] Types and pattern alternatives are complete and coherent.
- [ ] Effects are absent or explicitly declared and authorized.
- [ ] Recursive definitions have a termination or bounded-resource argument.
- [ ] Logic search strategy is explicit where operational behavior matters.
- [ ] Compiler transformations carry preservation evidence.
- [ ] Expected diagnostics identify the earliest responsible stage.
- [ ] R12 and MCRT identities can be traced without network access.
- [ ] Certification claims are separated from ordinary training examples.

## Laboratory 11

1. Locate `EX-DMLL-03003` in the technical corpus and verify its source hash.
2. Copy the program into a local air-gapped workspace and annotate every declaration.
3. Create one valid variation that preserves the `inference_strategy` invariant.
4. Create one intentionally invalid variation and specify its expected failure stage.
5. Record the semantic identity, expected diagnostic, and replay evidence in a lab notebook.

### Deliverable

Submit the original record ID, the valid variation, the invalid variation, a one-page semantic comparison, and a validation table containing expected stage, result, diagnostic, source hash, and semantic hash.

## Review questions

1. Which semantic invariant is most important in `inference_strategy`?
2. What evidence would distinguish modeled behavior from native execution?
3. Which negative case should be added before certifying an implementation?
4. How do purity, determinism, and policy interact in this chapter?

## Further corpus study

Filter `catalogs/CORPUS_INDEX.csv` for: inference_strategy, inference_divergence. Compare at least one positive, one negative, and—where available—one certification record. Identify which fields remain invariant across the three classes and which fields encode the expected failure.


# 12. Memoization, Tabling, and Rule Indexing

> **Corpus focus:** `memoization`, `tabling`, `rule_indexing`  
> **Representative record:** `EX-DMLL-03484` · tier `advanced_composition` · class `positive`

## Learning objectives

By the end of this chapter, the reader should be able to:

- Explain and apply **semantic caching**.
- Explain and apply **tabled resolution**.
- Explain and apply **indexes**.
- Explain and apply **termination support**.

## Core idea

DeepML Logic/Functional treats source code as one layer of a larger evidence object. A construct is not complete merely because it parses: its type, purity, logical meaning, compiler identity, runtime behavior, diagnostics, and provenance must agree. In this chapter the key design space is semantic caching, tabled resolution, indexes, and termination support. The practical discipline is to make each assumption explicit enough that another implementation can reproduce the same judgment without network access or hidden state.

The language's `pure_by_default` posture is architectural rather than decorative. It makes referential transparency the normal case, forces capabilities to appear at boundaries, and allows functions, rules, proofs, and compiler rewrites to be compared by semantic identity. Logic evaluation adds another dimension: operational search choices can affect termination and performance even when declarative meaning is stable. The corpus therefore records both denotational intent and operational evidence.

## Reading the evidence

A useful review separates four lenses:

- **SOPHIA:** Is the meaning coherent, typed, pure, and preserved?
- **CHARLOTTE:** Is the construct discoverable, consistently named, and represented across the corpus?
- **LANDON:** Can a compiler, validator, and runtime report deterministic evidence for it?
- **Professor + Podium:** Can a learner explain it, modify it, and diagnose its failure modes?

For `memoization`, the source record explains: This advanced Logic Functional Language (DeepML) example teaches memoization. It preserves the corpus-derived source → AST → typed/policy-verified semantic record → R12 → MCRT trace and uses deterministic IDs, hashes, provenance, and no-network safety. The example is expected to compile, lower, and produce deterministic runtime evidence.

## Worked corpus program

```deepml
deepml logic 0.3
module corpus.deepml_logic.example_03484
policy pure_by_default
policy no_network
theorem identity_composition<T>(f:T->T) : compose(identity,f) == f
proof identity_composition { extensionality x simplify identity qed }
constraint schedule(X,Y) { X >= 0 Y >= X + 5 }
predicate reachable(A,B)
rule reachable(A,B) :- edge(A,B)
rule reachable(A,C) :- edge(A,B), reachable(B,C)
infer reachable("start", Goal) strategy best_first memoize true
integrate graph Knowledge03484 from facts and rules
```

### What to inspect

- **Concepts:** memoization, compose_memoization, DEEPML_LOGIC_R12, R12, MCRT
- **Expected stage:** `runtime`
- **Expected result:** `pass`
- **Source identity:** `sha256:aa94e36100ee3e6f98c5ca44e95d3a0b8af0dae94438122cdb280d60d4402bea`
- **Semantic identity:** `sha256:5d797f325bf494b24841aa67a18a010fac7ff1f8810a3071e927cbb116f4d056`

Read the program top-down once for syntax, then bottom-up for obligations. The header establishes language identity; policies constrain effects; declarations introduce types, functions, relations, or proofs; and terminal operations expose evaluation, inference, transformation, or certification intent. A correct implementation should be able to explain not only whether the program succeeds, but why the reported stage is the first decisive stage.

## Engineering checklist

- [ ] The language version and module identity are explicit.
- [ ] All names resolve within declared namespace boundaries.
- [ ] Types and pattern alternatives are complete and coherent.
- [ ] Effects are absent or explicitly declared and authorized.
- [ ] Recursive definitions have a termination or bounded-resource argument.
- [ ] Logic search strategy is explicit where operational behavior matters.
- [ ] Compiler transformations carry preservation evidence.
- [ ] Expected diagnostics identify the earliest responsible stage.
- [ ] R12 and MCRT identities can be traced without network access.
- [ ] Certification claims are separated from ordinary training examples.

## Laboratory 12

1. Locate `EX-DMLL-03484` in the technical corpus and verify its source hash.
2. Copy the program into a local air-gapped workspace and annotate every declaration.
3. Create one valid variation that preserves the `memoization` invariant.
4. Create one intentionally invalid variation and specify its expected failure stage.
5. Record the semantic identity, expected diagnostic, and replay evidence in a lab notebook.

### Deliverable

Submit the original record ID, the valid variation, the invalid variation, a one-page semantic comparison, and a validation table containing expected stage, result, diagnostic, source hash, and semantic hash.

## Review questions

1. Which semantic invariant is most important in `memoization`?
2. What evidence would distinguish modeled behavior from native execution?
3. Which negative case should be added before certifying an implementation?
4. How do purity, determinism, and policy interact in this chapter?

## Further corpus study

Filter `catalogs/CORPUS_INDEX.csv` for: memoization, tabling, rule_indexing. Compare at least one positive, one negative, and—where available—one certification record. Identify which fields remain invariant across the three classes and which fields encode the expected failure.


# 13. Constraints and Consistency

> **Corpus focus:** `constraint_solving`, `contradictory_facts`  
> **Representative record:** `EX-DMLL-03005` · tier `advanced_composition` · class `positive`

## Learning objectives

By the end of this chapter, the reader should be able to:

- Explain and apply **constraint domains**.
- Explain and apply **scheduling relations**.
- Explain and apply **contradictory facts**.
- Explain and apply **failure evidence**.

## Core idea

DeepML Logic/Functional treats source code as one layer of a larger evidence object. A construct is not complete merely because it parses: its type, purity, logical meaning, compiler identity, runtime behavior, diagnostics, and provenance must agree. In this chapter the key design space is constraint domains, scheduling relations, contradictory facts, and failure evidence. The practical discipline is to make each assumption explicit enough that another implementation can reproduce the same judgment without network access or hidden state.

The language's `pure_by_default` posture is architectural rather than decorative. It makes referential transparency the normal case, forces capabilities to appear at boundaries, and allows functions, rules, proofs, and compiler rewrites to be compared by semantic identity. Logic evaluation adds another dimension: operational search choices can affect termination and performance even when declarative meaning is stable. The corpus therefore records both denotational intent and operational evidence.

## Reading the evidence

A useful review separates four lenses:

- **SOPHIA:** Is the meaning coherent, typed, pure, and preserved?
- **CHARLOTTE:** Is the construct discoverable, consistently named, and represented across the corpus?
- **LANDON:** Can a compiler, validator, and runtime report deterministic evidence for it?
- **Professor + Podium:** Can a learner explain it, modify it, and diagnose its failure modes?

For `constraint_solving`, the source record explains: This advanced Logic Functional Language (DeepML) example teaches constraint solving. It preserves the corpus-derived source → AST → typed/policy-verified semantic record → R12 → MCRT trace and uses deterministic IDs, hashes, provenance, and no-network safety. The example is expected to compile, lower, and produce deterministic runtime evidence.

## Worked corpus program

```deepml
deepml logic 0.3
module corpus.deepml_logic.example_03005
policy pure_by_default
policy no_network
theorem identity_composition<T>(f:T->T) : compose(identity,f) == f
proof identity_composition { extensionality x simplify identity qed }
constraint schedule(X,Y) { X >= 0 Y >= X + 1 }
predicate reachable(A,B)
rule reachable(A,B) :- edge(A,B)
rule reachable(A,C) :- edge(A,B), reachable(B,C)
infer reachable("start", Goal) strategy best_first memoize true
integrate graph Knowledge03005 from facts and rules
```

### What to inspect

- **Concepts:** constraint_solving, compose_constraint_solving, DEEPML_LOGIC_R12, R12, MCRT
- **Expected stage:** `runtime`
- **Expected result:** `pass`
- **Source identity:** `sha256:a215a0b29a548aef7c983e4ef53d8e127f3efba6d28593ba16962d2aa849c760`
- **Semantic identity:** `sha256:1147f5aa643809a17371328707bdbcbbd5bfa04d7f28d6fad0665692a2df682e`

Read the program top-down once for syntax, then bottom-up for obligations. The header establishes language identity; policies constrain effects; declarations introduce types, functions, relations, or proofs; and terminal operations expose evaluation, inference, transformation, or certification intent. A correct implementation should be able to explain not only whether the program succeeds, but why the reported stage is the first decisive stage.

## Engineering checklist

- [ ] The language version and module identity are explicit.
- [ ] All names resolve within declared namespace boundaries.
- [ ] Types and pattern alternatives are complete and coherent.
- [ ] Effects are absent or explicitly declared and authorized.
- [ ] Recursive definitions have a termination or bounded-resource argument.
- [ ] Logic search strategy is explicit where operational behavior matters.
- [ ] Compiler transformations carry preservation evidence.
- [ ] Expected diagnostics identify the earliest responsible stage.
- [ ] R12 and MCRT identities can be traced without network access.
- [ ] Certification claims are separated from ordinary training examples.

## Laboratory 13

1. Locate `EX-DMLL-03005` in the technical corpus and verify its source hash.
2. Copy the program into a local air-gapped workspace and annotate every declaration.
3. Create one valid variation that preserves the `constraint_solving` invariant.
4. Create one intentionally invalid variation and specify its expected failure stage.
5. Record the semantic identity, expected diagnostic, and replay evidence in a lab notebook.

### Deliverable

Submit the original record ID, the valid variation, the invalid variation, a one-page semantic comparison, and a validation table containing expected stage, result, diagnostic, source hash, and semantic hash.

## Review questions

1. Which semantic invariant is most important in `constraint_solving`?
2. What evidence would distinguish modeled behavior from native execution?
3. Which negative case should be added before certifying an implementation?
4. How do purity, determinism, and policy interact in this chapter?

## Further corpus study

Filter `catalogs/CORPUS_INDEX.csv` for: constraint_solving, contradictory_facts. Compare at least one positive, one negative, and—where available—one certification record. Identify which fields remain invariant across the three classes and which fields encode the expected failure.


# 14. Theorems, Proof Terms, and Soundness

> **Corpus focus:** `theorem`, `proof_term`, `unsound_proof`  
> **Representative record:** `EX-DMLL-02995` · tier `advanced_composition` · class `positive`

## Learning objectives

By the end of this chapter, the reader should be able to:

- Explain and apply **propositions**.
- Explain and apply **proof objects**.
- Explain and apply **obligations**.
- Explain and apply **unsound evidence**.

## Core idea

DeepML Logic/Functional treats source code as one layer of a larger evidence object. A construct is not complete merely because it parses: its type, purity, logical meaning, compiler identity, runtime behavior, diagnostics, and provenance must agree. In this chapter the key design space is propositions, proof objects, obligations, and unsound evidence. The practical discipline is to make each assumption explicit enough that another implementation can reproduce the same judgment without network access or hidden state.

The language's `pure_by_default` posture is architectural rather than decorative. It makes referential transparency the normal case, forces capabilities to appear at boundaries, and allows functions, rules, proofs, and compiler rewrites to be compared by semantic identity. Logic evaluation adds another dimension: operational search choices can affect termination and performance even when declarative meaning is stable. The corpus therefore records both denotational intent and operational evidence.

## Reading the evidence

A useful review separates four lenses:

- **SOPHIA:** Is the meaning coherent, typed, pure, and preserved?
- **CHARLOTTE:** Is the construct discoverable, consistently named, and represented across the corpus?
- **LANDON:** Can a compiler, validator, and runtime report deterministic evidence for it?
- **Professor + Podium:** Can a learner explain it, modify it, and diagnose its failure modes?

For `theorem`, the source record explains: This advanced Logic Functional Language (DeepML) example teaches theorem. It preserves the corpus-derived source → AST → typed/policy-verified semantic record → R12 → MCRT trace and uses deterministic IDs, hashes, provenance, and no-network safety. The example is expected to compile, lower, and produce deterministic runtime evidence.

## Worked corpus program

```deepml
deepml logic 0.3
module corpus.deepml_logic.example_02995
policy pure_by_default
policy no_network
theorem identity_composition<T>(f:T->T) : compose(identity,f) == f
proof identity_composition { extensionality x simplify identity qed }
constraint schedule(X,Y) { X >= 0 Y >= X + 1 }
predicate reachable(A,B)
rule reachable(A,B) :- edge(A,B)
rule reachable(A,C) :- edge(A,B), reachable(B,C)
infer reachable("start", Goal) strategy best_first memoize true
integrate graph Knowledge02995 from facts and rules
```

### What to inspect

- **Concepts:** theorem, compose_theorem, DEEPML_LOGIC_R12, R12, MCRT
- **Expected stage:** `runtime`
- **Expected result:** `pass`
- **Source identity:** `sha256:fe5a0867528f24720aa092c56f24e20e10a5b093a6b21dacf4198ec5e65d10bb`
- **Semantic identity:** `sha256:ab3320311d8538e746359c1e0a4dcf084145579dcf1ab7a81a3c45e8bad2f382`

Read the program top-down once for syntax, then bottom-up for obligations. The header establishes language identity; policies constrain effects; declarations introduce types, functions, relations, or proofs; and terminal operations expose evaluation, inference, transformation, or certification intent. A correct implementation should be able to explain not only whether the program succeeds, but why the reported stage is the first decisive stage.

## Engineering checklist

- [ ] The language version and module identity are explicit.
- [ ] All names resolve within declared namespace boundaries.
- [ ] Types and pattern alternatives are complete and coherent.
- [ ] Effects are absent or explicitly declared and authorized.
- [ ] Recursive definitions have a termination or bounded-resource argument.
- [ ] Logic search strategy is explicit where operational behavior matters.
- [ ] Compiler transformations carry preservation evidence.
- [ ] Expected diagnostics identify the earliest responsible stage.
- [ ] R12 and MCRT identities can be traced without network access.
- [ ] Certification claims are separated from ordinary training examples.

## Laboratory 14

1. Locate `EX-DMLL-02995` in the technical corpus and verify its source hash.
2. Copy the program into a local air-gapped workspace and annotate every declaration.
3. Create one valid variation that preserves the `theorem` invariant.
4. Create one intentionally invalid variation and specify its expected failure stage.
5. Record the semantic identity, expected diagnostic, and replay evidence in a lab notebook.

### Deliverable

Submit the original record ID, the valid variation, the invalid variation, a one-page semantic comparison, and a validation table containing expected stage, result, diagnostic, source hash, and semantic hash.

## Review questions

1. Which semantic invariant is most important in `theorem`?
2. What evidence would distinguish modeled behavior from native execution?
3. Which negative case should be added before certifying an implementation?
4. How do purity, determinism, and policy interact in this chapter?

## Further corpus study

Filter `catalogs/CORPUS_INDEX.csv` for: theorem, proof_term, unsound_proof. Compare at least one positive, one negative, and—where available—one certification record. Identify which fields remain invariant across the three classes and which fields encode the expected failure.


# 15. Symbolic Reasoning and Proof Normalization

> **Corpus focus:** `symbolic_reasoning`, `proof_normalization`  
> **Representative record:** `EX-DMLL-03263` · tier `advanced_composition` · class `positive`

## Learning objectives

By the end of this chapter, the reader should be able to:

- Explain and apply **rewriting**.
- Explain and apply **canonical proofs**.
- Explain and apply **simplification**.
- Explain and apply **identity preservation**.

## Core idea

DeepML Logic/Functional treats source code as one layer of a larger evidence object. A construct is not complete merely because it parses: its type, purity, logical meaning, compiler identity, runtime behavior, diagnostics, and provenance must agree. In this chapter the key design space is rewriting, canonical proofs, simplification, and identity preservation. The practical discipline is to make each assumption explicit enough that another implementation can reproduce the same judgment without network access or hidden state.

The language's `pure_by_default` posture is architectural rather than decorative. It makes referential transparency the normal case, forces capabilities to appear at boundaries, and allows functions, rules, proofs, and compiler rewrites to be compared by semantic identity. Logic evaluation adds another dimension: operational search choices can affect termination and performance even when declarative meaning is stable. The corpus therefore records both denotational intent and operational evidence.

## Reading the evidence

A useful review separates four lenses:

- **SOPHIA:** Is the meaning coherent, typed, pure, and preserved?
- **CHARLOTTE:** Is the construct discoverable, consistently named, and represented across the corpus?
- **LANDON:** Can a compiler, validator, and runtime report deterministic evidence for it?
- **Professor + Podium:** Can a learner explain it, modify it, and diagnose its failure modes?

For `symbolic_reasoning`, the source record explains: This advanced Logic Functional Language (DeepML) example teaches symbolic reasoning. It preserves the corpus-derived source → AST → typed/policy-verified semantic record → R12 → MCRT trace and uses deterministic IDs, hashes, provenance, and no-network safety. The example is expected to compile, lower, and produce deterministic runtime evidence.

## Worked corpus program

```deepml
deepml logic 0.3
module corpus.deepml_logic.example_03263
policy pure_by_default
policy no_network
theorem identity_composition<T>(f:T->T) : compose(identity,f) == f
proof identity_composition { extensionality x simplify identity qed }
constraint schedule(X,Y) { X >= 0 Y >= X + 4 }
predicate reachable(A,B)
rule reachable(A,B) :- edge(A,B)
rule reachable(A,C) :- edge(A,B), reachable(B,C)
infer reachable("start", Goal) strategy best_first memoize true
integrate graph Knowledge03263 from facts and rules
```

### What to inspect

- **Concepts:** symbolic_reasoning, compose_symbolic_reasoning, DEEPML_LOGIC_R12, R12, MCRT
- **Expected stage:** `runtime`
- **Expected result:** `pass`
- **Source identity:** `sha256:27b422f4dcf8369a6622e42fbc29ff98c699cb59a6c3f927f065325373df1552`
- **Semantic identity:** `sha256:974118793e1b719acebb00f98ecb2ac1a014bd49c7371dff07ce24b76c5de9c8`

Read the program top-down once for syntax, then bottom-up for obligations. The header establishes language identity; policies constrain effects; declarations introduce types, functions, relations, or proofs; and terminal operations expose evaluation, inference, transformation, or certification intent. A correct implementation should be able to explain not only whether the program succeeds, but why the reported stage is the first decisive stage.

## Engineering checklist

- [ ] The language version and module identity are explicit.
- [ ] All names resolve within declared namespace boundaries.
- [ ] Types and pattern alternatives are complete and coherent.
- [ ] Effects are absent or explicitly declared and authorized.
- [ ] Recursive definitions have a termination or bounded-resource argument.
- [ ] Logic search strategy is explicit where operational behavior matters.
- [ ] Compiler transformations carry preservation evidence.
- [ ] Expected diagnostics identify the earliest responsible stage.
- [ ] R12 and MCRT identities can be traced without network access.
- [ ] Certification claims are separated from ordinary training examples.

## Laboratory 15

1. Locate `EX-DMLL-03263` in the technical corpus and verify its source hash.
2. Copy the program into a local air-gapped workspace and annotate every declaration.
3. Create one valid variation that preserves the `symbolic_reasoning` invariant.
4. Create one intentionally invalid variation and specify its expected failure stage.
5. Record the semantic identity, expected diagnostic, and replay evidence in a lab notebook.

### Deliverable

Submit the original record ID, the valid variation, the invalid variation, a one-page semantic comparison, and a validation table containing expected stage, result, diagnostic, source hash, and semantic hash.

## Review questions

1. Which semantic invariant is most important in `symbolic_reasoning`?
2. What evidence would distinguish modeled behavior from native execution?
3. Which negative case should be added before certifying an implementation?
4. How do purity, determinism, and policy interact in this chapter?

## Further corpus study

Filter `catalogs/CORPUS_INDEX.csv` for: symbolic_reasoning, proof_normalization. Compare at least one positive, one negative, and—where available—one certification record. Identify which fields remain invariant across the three classes and which fields encode the expected failure.


# 16. Knowledge Bases and Planning Systems

> **Corpus focus:** `knowledge_base`, `planning_system`  
> **Representative record:** `EX-DMLL-06106` · tier `large_integrated_examples` · class `positive`

## Learning objectives

By the end of this chapter, the reader should be able to:

- Explain and apply **knowledge organization**.
- Explain and apply **goals**.
- Explain and apply **actions**.
- Explain and apply **preconditions**.
- Explain and apply **plan evidence**.

## Core idea

DeepML Logic/Functional treats source code as one layer of a larger evidence object. A construct is not complete merely because it parses: its type, purity, logical meaning, compiler identity, runtime behavior, diagnostics, and provenance must agree. In this chapter the key design space is knowledge organization, goals, actions, preconditions, and plan evidence. The practical discipline is to make each assumption explicit enough that another implementation can reproduce the same judgment without network access or hidden state.

The language's `pure_by_default` posture is architectural rather than decorative. It makes referential transparency the normal case, forces capabilities to appear at boundaries, and allows functions, rules, proofs, and compiler rewrites to be compared by semantic identity. Logic evaluation adds another dimension: operational search choices can affect termination and performance even when declarative meaning is stable. The corpus therefore records both denotational intent and operational evidence.

## Reading the evidence

A useful review separates four lenses:

- **SOPHIA:** Is the meaning coherent, typed, pure, and preserved?
- **CHARLOTTE:** Is the construct discoverable, consistently named, and represented across the corpus?
- **LANDON:** Can a compiler, validator, and runtime report deterministic evidence for it?
- **Professor + Podium:** Can a learner explain it, modify it, and diagnose its failure modes?

For `knowledge_base`, the source record explains: This expert Logic Functional Language (DeepML) example teaches knowledge base. It preserves the corpus-derived source → AST → typed/policy-verified semantic record → R12 → MCRT trace and uses deterministic IDs, hashes, provenance, and no-network safety. The example is expected to compile, lower, and produce deterministic runtime evidence.

## Worked corpus program

```deepml
deepml logic 0.3
module corpus.deepml_logic.example_06106
policy pure_by_default
policy no_network
knowledge_base Logic06106 {
  fact scene("PortalScene3")
  fact timeline("Sequence9")
  rule can_open(P) :- authorized(P), stable_scene(P)
  rule execute_sequence(S) :- can_open(portal_of(S)), certified(S)
}
plan PortalPlan06106 goal entered_destination actions [authorize, open_portal, play_timeline, traverse]
transform SceneRuleSet with proof { preserve semantics using theorem identity_composition }
workflow SymbolicNeural06106 { symbolic: Logic06106 neural: deepml.core::Graph06106 bridge: typed }
certify logic Logic06106 using proof_carrying
```

### What to inspect

- **Concepts:** knowledge_base, integrate_knowledge_base, DEEPML_LOGIC_R12, R12, MCRT
- **Expected stage:** `runtime`
- **Expected result:** `pass`
- **Source identity:** `sha256:9534523ac64899c6ca97156bbfaa5dafbade5dff57502f7d46227de22895d81a`
- **Semantic identity:** `sha256:35e25ebdb2d10ce04ec1b5462c046110277625e4f2096df7a0c72f79e98b9c19`

Read the program top-down once for syntax, then bottom-up for obligations. The header establishes language identity; policies constrain effects; declarations introduce types, functions, relations, or proofs; and terminal operations expose evaluation, inference, transformation, or certification intent. A correct implementation should be able to explain not only whether the program succeeds, but why the reported stage is the first decisive stage.

## Engineering checklist

- [ ] The language version and module identity are explicit.
- [ ] All names resolve within declared namespace boundaries.
- [ ] Types and pattern alternatives are complete and coherent.
- [ ] Effects are absent or explicitly declared and authorized.
- [ ] Recursive definitions have a termination or bounded-resource argument.
- [ ] Logic search strategy is explicit where operational behavior matters.
- [ ] Compiler transformations carry preservation evidence.
- [ ] Expected diagnostics identify the earliest responsible stage.
- [ ] R12 and MCRT identities can be traced without network access.
- [ ] Certification claims are separated from ordinary training examples.

## Laboratory 16

1. Locate `EX-DMLL-06106` in the technical corpus and verify its source hash.
2. Copy the program into a local air-gapped workspace and annotate every declaration.
3. Create one valid variation that preserves the `knowledge_base` invariant.
4. Create one intentionally invalid variation and specify its expected failure stage.
5. Record the semantic identity, expected diagnostic, and replay evidence in a lab notebook.

### Deliverable

Submit the original record ID, the valid variation, the invalid variation, a one-page semantic comparison, and a validation table containing expected stage, result, diagnostic, source hash, and semantic hash.

## Review questions

1. Which semantic invariant is most important in `knowledge_base`?
2. What evidence would distinguish modeled behavior from native execution?
3. Which negative case should be added before certifying an implementation?
4. How do purity, determinism, and policy interact in this chapter?

## Further corpus study

Filter `catalogs/CORPUS_INDEX.csv` for: knowledge_base, planning_system. Compare at least one positive, one negative, and—where available—one certification record. Identify which fields remain invariant across the three classes and which fields encode the expected failure.


# 17. Scene and Timeline Rule Systems

> **Corpus focus:** `scene_timeline_rules`, `knowledge_base`  
> **Representative record:** `EX-DMLL-06124` · tier `large_integrated_examples` · class `positive`

## Learning objectives

By the end of this chapter, the reader should be able to:

- Explain and apply **JA21 scene facts**.
- Explain and apply **timeline transitions**.
- Explain and apply **authorization**.
- Explain and apply **deterministic orchestration**.

## Core idea

DeepML Logic/Functional treats source code as one layer of a larger evidence object. A construct is not complete merely because it parses: its type, purity, logical meaning, compiler identity, runtime behavior, diagnostics, and provenance must agree. In this chapter the key design space is JA21 scene facts, timeline transitions, authorization, and deterministic orchestration. The practical discipline is to make each assumption explicit enough that another implementation can reproduce the same judgment without network access or hidden state.

The language's `pure_by_default` posture is architectural rather than decorative. It makes referential transparency the normal case, forces capabilities to appear at boundaries, and allows functions, rules, proofs, and compiler rewrites to be compared by semantic identity. Logic evaluation adds another dimension: operational search choices can affect termination and performance even when declarative meaning is stable. The corpus therefore records both denotational intent and operational evidence.

## Reading the evidence

A useful review separates four lenses:

- **SOPHIA:** Is the meaning coherent, typed, pure, and preserved?
- **CHARLOTTE:** Is the construct discoverable, consistently named, and represented across the corpus?
- **LANDON:** Can a compiler, validator, and runtime report deterministic evidence for it?
- **Professor + Podium:** Can a learner explain it, modify it, and diagnose its failure modes?

For `knowledge_base`, the source record explains: This expert Logic Functional Language (DeepML) example teaches knowledge base. It preserves the corpus-derived source → AST → typed/policy-verified semantic record → R12 → MCRT trace and uses deterministic IDs, hashes, provenance, and no-network safety. The example is expected to compile, lower, and produce deterministic runtime evidence.

## Worked corpus program

```deepml
deepml logic 0.3
module corpus.deepml_logic.example_06124
policy pure_by_default
policy no_network
knowledge_base Logic06124 {
  fact scene("PortalScene4")
  fact timeline("Sequence1")
  rule can_open(P) :- authorized(P), stable_scene(P)
  rule execute_sequence(S) :- can_open(portal_of(S)), certified(S)
}
plan PortalPlan06124 goal entered_destination actions [authorize, open_portal, play_timeline, traverse]
transform SceneRuleSet with proof { preserve semantics using theorem identity_composition }
workflow SymbolicNeural06124 { symbolic: Logic06124 neural: deepml.core::Graph06124 bridge: typed }
certify logic Logic06124 using proof_carrying
```

### What to inspect

- **Concepts:** knowledge_base, integrate_knowledge_base, DEEPML_LOGIC_R12, R12, MCRT
- **Expected stage:** `runtime`
- **Expected result:** `pass`
- **Source identity:** `sha256:7ca2437f40f243eec97099d3f47df7a5457c72b7c55a740e08797e1e1b1f2812`
- **Semantic identity:** `sha256:0d60ee88d91396ec486a9eacd4fac26f02c91fe3401076916b984e8fd4907744`

Read the program top-down once for syntax, then bottom-up for obligations. The header establishes language identity; policies constrain effects; declarations introduce types, functions, relations, or proofs; and terminal operations expose evaluation, inference, transformation, or certification intent. A correct implementation should be able to explain not only whether the program succeeds, but why the reported stage is the first decisive stage.

## Engineering checklist

- [ ] The language version and module identity are explicit.
- [ ] All names resolve within declared namespace boundaries.
- [ ] Types and pattern alternatives are complete and coherent.
- [ ] Effects are absent or explicitly declared and authorized.
- [ ] Recursive definitions have a termination or bounded-resource argument.
- [ ] Logic search strategy is explicit where operational behavior matters.
- [ ] Compiler transformations carry preservation evidence.
- [ ] Expected diagnostics identify the earliest responsible stage.
- [ ] R12 and MCRT identities can be traced without network access.
- [ ] Certification claims are separated from ordinary training examples.

## Laboratory 17

1. Locate `EX-DMLL-06124` in the technical corpus and verify its source hash.
2. Copy the program into a local air-gapped workspace and annotate every declaration.
3. Create one valid variation that preserves the `knowledge_base` invariant.
4. Create one intentionally invalid variation and specify its expected failure stage.
5. Record the semantic identity, expected diagnostic, and replay evidence in a lab notebook.

### Deliverable

Submit the original record ID, the valid variation, the invalid variation, a one-page semantic comparison, and a validation table containing expected stage, result, diagnostic, source hash, and semantic hash.

## Review questions

1. Which semantic invariant is most important in `knowledge_base`?
2. What evidence would distinguish modeled behavior from native execution?
3. Which negative case should be added before certifying an implementation?
4. How do purity, determinism, and policy interact in this chapter?

## Further corpus study

Filter `catalogs/CORPUS_INDEX.csv` for: scene_timeline_rules, knowledge_base. Compare at least one positive, one negative, and—where available—one certification record. Identify which fields remain invariant across the three classes and which fields encode the expected failure.


# 18. Symbolic–Neural and Logic–Graph Integration

> **Corpus focus:** `symbolic_neural_workflow`, `logic_graph_integration`  
> **Representative record:** `EX-DMLL-03615` · tier `advanced_composition` · class `positive`

## Learning objectives

By the end of this chapter, the reader should be able to:

- Explain and apply **typed bridges**.
- Explain and apply **workflow boundaries**.
- Explain and apply **graph references**.
- Explain and apply **evidence exchange**.

## Core idea

DeepML Logic/Functional treats source code as one layer of a larger evidence object. A construct is not complete merely because it parses: its type, purity, logical meaning, compiler identity, runtime behavior, diagnostics, and provenance must agree. In this chapter the key design space is typed bridges, workflow boundaries, graph references, and evidence exchange. The practical discipline is to make each assumption explicit enough that another implementation can reproduce the same judgment without network access or hidden state.

The language's `pure_by_default` posture is architectural rather than decorative. It makes referential transparency the normal case, forces capabilities to appear at boundaries, and allows functions, rules, proofs, and compiler rewrites to be compared by semantic identity. Logic evaluation adds another dimension: operational search choices can affect termination and performance even when declarative meaning is stable. The corpus therefore records both denotational intent and operational evidence.

## Reading the evidence

A useful review separates four lenses:

- **SOPHIA:** Is the meaning coherent, typed, pure, and preserved?
- **CHARLOTTE:** Is the construct discoverable, consistently named, and represented across the corpus?
- **LANDON:** Can a compiler, validator, and runtime report deterministic evidence for it?
- **Professor + Podium:** Can a learner explain it, modify it, and diagnose its failure modes?

For `logic_graph_integration`, the source record explains: This advanced Logic Functional Language (DeepML) example teaches logic graph integration. It preserves the corpus-derived source → AST → typed/policy-verified semantic record → R12 → MCRT trace and uses deterministic IDs, hashes, provenance, and no-network safety. The example is expected to compile, lower, and produce deterministic runtime evidence.

## Worked corpus program

```deepml
deepml logic 0.3
module corpus.deepml_logic.example_03615
policy pure_by_default
policy no_network
theorem identity_composition<T>(f:T->T) : compose(identity,f) == f
proof identity_composition { extensionality x simplify identity qed }
constraint schedule(X,Y) { X >= 0 Y >= X + 1 }
predicate reachable(A,B)
rule reachable(A,B) :- edge(A,B)
rule reachable(A,C) :- edge(A,B), reachable(B,C)
infer reachable("start", Goal) strategy best_first memoize true
integrate graph Knowledge03615 from facts and rules
```

### What to inspect

- **Concepts:** logic_graph_integration, compose_logic_graph_integration, DEEPML_LOGIC_R12, R12, MCRT
- **Expected stage:** `runtime`
- **Expected result:** `pass`
- **Source identity:** `sha256:45f2daa654f41c5161f6979e0f2ef96723df6770c709d0a382594f0e5da2e59c`
- **Semantic identity:** `sha256:395e526b2550ac014bd51b4d867af4a7d15fc9232b0a92254b958313cb5be0f2`

Read the program top-down once for syntax, then bottom-up for obligations. The header establishes language identity; policies constrain effects; declarations introduce types, functions, relations, or proofs; and terminal operations expose evaluation, inference, transformation, or certification intent. A correct implementation should be able to explain not only whether the program succeeds, but why the reported stage is the first decisive stage.

## Engineering checklist

- [ ] The language version and module identity are explicit.
- [ ] All names resolve within declared namespace boundaries.
- [ ] Types and pattern alternatives are complete and coherent.
- [ ] Effects are absent or explicitly declared and authorized.
- [ ] Recursive definitions have a termination or bounded-resource argument.
- [ ] Logic search strategy is explicit where operational behavior matters.
- [ ] Compiler transformations carry preservation evidence.
- [ ] Expected diagnostics identify the earliest responsible stage.
- [ ] R12 and MCRT identities can be traced without network access.
- [ ] Certification claims are separated from ordinary training examples.

## Laboratory 18

1. Locate `EX-DMLL-03615` in the technical corpus and verify its source hash.
2. Copy the program into a local air-gapped workspace and annotate every declaration.
3. Create one valid variation that preserves the `logic_graph_integration` invariant.
4. Create one intentionally invalid variation and specify its expected failure stage.
5. Record the semantic identity, expected diagnostic, and replay evidence in a lab notebook.

### Deliverable

Submit the original record ID, the valid variation, the invalid variation, a one-page semantic comparison, and a validation table containing expected stage, result, diagnostic, source hash, and semantic hash.

## Review questions

1. Which semantic invariant is most important in `logic_graph_integration`?
2. What evidence would distinguish modeled behavior from native execution?
3. Which negative case should be added before certifying an implementation?
4. How do purity, determinism, and policy interact in this chapter?

## Further corpus study

Filter `catalogs/CORPUS_INDEX.csv` for: symbolic_neural_workflow, logic_graph_integration. Compare at least one positive, one negative, and—where available—one certification record. Identify which fields remain invariant across the three classes and which fields encode the expected failure.


# 19. Functional Compiler Optimization

> **Corpus focus:** `beta_reduction`, `cse`, `deforestation`, `tail_call`  
> **Representative record:** `EX-DMLL-07801` · tier `compiler_optimization` · class `positive`

## Learning objectives

By the end of this chapter, the reader should be able to:

- Explain and apply **beta reduction**.
- Explain and apply **common-subexpression elimination**.
- Explain and apply **deforestation**.
- Explain and apply **tail calls**.

## Core idea

DeepML Logic/Functional treats source code as one layer of a larger evidence object. A construct is not complete merely because it parses: its type, purity, logical meaning, compiler identity, runtime behavior, diagnostics, and provenance must agree. In this chapter the key design space is beta reduction, common-subexpression elimination, deforestation, and tail calls. The practical discipline is to make each assumption explicit enough that another implementation can reproduce the same judgment without network access or hidden state.

The language's `pure_by_default` posture is architectural rather than decorative. It makes referential transparency the normal case, forces capabilities to appear at boundaries, and allows functions, rules, proofs, and compiler rewrites to be compared by semantic identity. Logic evaluation adds another dimension: operational search choices can affect termination and performance even when declarative meaning is stable. The corpus therefore records both denotational intent and operational evidence.

## Reading the evidence

A useful review separates four lenses:

- **SOPHIA:** Is the meaning coherent, typed, pure, and preserved?
- **CHARLOTTE:** Is the construct discoverable, consistently named, and represented across the corpus?
- **LANDON:** Can a compiler, validator, and runtime report deterministic evidence for it?
- **Professor + Podium:** Can a learner explain it, modify it, and diagnose its failure modes?

For `deforestation`, the source record explains: This compiler Logic Functional Language (DeepML) example teaches deforestation. It preserves the corpus-derived source → AST → typed/policy-verified semantic record → R12 → MCRT trace and uses deterministic IDs, hashes, provenance, and no-network safety. The example is expected to compile, lower, and produce deterministic runtime evidence.

## Worked corpus program

```deepml
deepml logic 0.3
module corpus.deepml_logic.example_07801
policy pure_by_default
policy no_network
fn pipeline(xs: List<Int>) -> Int = fold((a,x) => a + (x * 1), 0, map(identity, xs))
rule path(A,C) :- edge(A,B), path(B,C)
rule path(A,B) :- edge(A,B)
theorem redundant_identity(xs) : map(identity,xs) == xs
proof redundant_identity { induction xs simplify qed }
optimize module using [beta_reduction, tail_call, deforestation, rule_indexing, common_subexpression_elimination, tabling, proof_normalization]
lower module to DEEPML_LOGIC_R12
```

### What to inspect

- **Concepts:** deforestation, optimize_logic, DEEPML_LOGIC_R12, R12, MCRT
- **Expected stage:** `runtime`
- **Expected result:** `pass`
- **Source identity:** `sha256:679db37d4ad2ea30c218fb0b1efd3046056e06faa02fa2fcb0d58c15abba94ac`
- **Semantic identity:** `sha256:3f8ef336ca4b3fc54df96bf4430fbd7f4d2ccafb2430d4997f64af9332196074`

Read the program top-down once for syntax, then bottom-up for obligations. The header establishes language identity; policies constrain effects; declarations introduce types, functions, relations, or proofs; and terminal operations expose evaluation, inference, transformation, or certification intent. A correct implementation should be able to explain not only whether the program succeeds, but why the reported stage is the first decisive stage.

## Engineering checklist

- [ ] The language version and module identity are explicit.
- [ ] All names resolve within declared namespace boundaries.
- [ ] Types and pattern alternatives are complete and coherent.
- [ ] Effects are absent or explicitly declared and authorized.
- [ ] Recursive definitions have a termination or bounded-resource argument.
- [ ] Logic search strategy is explicit where operational behavior matters.
- [ ] Compiler transformations carry preservation evidence.
- [ ] Expected diagnostics identify the earliest responsible stage.
- [ ] R12 and MCRT identities can be traced without network access.
- [ ] Certification claims are separated from ordinary training examples.

## Laboratory 19

1. Locate `EX-DMLL-07801` in the technical corpus and verify its source hash.
2. Copy the program into a local air-gapped workspace and annotate every declaration.
3. Create one valid variation that preserves the `deforestation` invariant.
4. Create one intentionally invalid variation and specify its expected failure stage.
5. Record the semantic identity, expected diagnostic, and replay evidence in a lab notebook.

### Deliverable

Submit the original record ID, the valid variation, the invalid variation, a one-page semantic comparison, and a validation table containing expected stage, result, diagnostic, source hash, and semantic hash.

## Review questions

1. Which semantic invariant is most important in `deforestation`?
2. What evidence would distinguish modeled behavior from native execution?
3. Which negative case should be added before certifying an implementation?
4. How do purity, determinism, and policy interact in this chapter?

## Further corpus study

Filter `catalogs/CORPUS_INDEX.csv` for: beta_reduction, cse, deforestation, tail_call. Compare at least one positive, one negative, and—where available—one certification record. Identify which fields remain invariant across the three classes and which fields encode the expected failure.


# 20. Proof-Carrying Transforms and R12/MCRT Lowering

> **Corpus focus:** `proof_carrying_transform`, `r12_mcrt_lowering`  
> **Representative record:** `EX-DMLL-08574` · tier `compiler_optimization` · class `positive`

## Learning objectives

By the end of this chapter, the reader should be able to:

- Explain and apply **preservation theorems**.
- Explain and apply **semantic identities**.
- Explain and apply **R12 relations**.
- Explain and apply **MCRT replay**.

## Core idea

DeepML Logic/Functional treats source code as one layer of a larger evidence object. A construct is not complete merely because it parses: its type, purity, logical meaning, compiler identity, runtime behavior, diagnostics, and provenance must agree. In this chapter the key design space is preservation theorems, semantic identities, R12 relations, and MCRT replay. The practical discipline is to make each assumption explicit enough that another implementation can reproduce the same judgment without network access or hidden state.

The language's `pure_by_default` posture is architectural rather than decorative. It makes referential transparency the normal case, forces capabilities to appear at boundaries, and allows functions, rules, proofs, and compiler rewrites to be compared by semantic identity. Logic evaluation adds another dimension: operational search choices can affect termination and performance even when declarative meaning is stable. The corpus therefore records both denotational intent and operational evidence.

## Reading the evidence

A useful review separates four lenses:

- **SOPHIA:** Is the meaning coherent, typed, pure, and preserved?
- **CHARLOTTE:** Is the construct discoverable, consistently named, and represented across the corpus?
- **LANDON:** Can a compiler, validator, and runtime report deterministic evidence for it?
- **Professor + Podium:** Can a learner explain it, modify it, and diagnose its failure modes?

For `r12_mcrt_lowering`, the source record explains: This compiler Logic Functional Language (DeepML) example teaches r12 mcrt lowering. It preserves the corpus-derived source → AST → typed/policy-verified semantic record → R12 → MCRT trace and uses deterministic IDs, hashes, provenance, and no-network safety. The example is expected to compile, lower, and produce deterministic runtime evidence.

## Worked corpus program

```deepml
deepml logic 0.3
module corpus.deepml_logic.example_08574
policy pure_by_default
policy no_network
fn pipeline(xs: List<Int>) -> Int = fold((a,x) => a + (x * 1), 0, map(identity, xs))
rule path(A,C) :- edge(A,B), path(B,C)
rule path(A,B) :- edge(A,B)
theorem redundant_identity(xs) : map(identity,xs) == xs
proof redundant_identity { induction xs simplify qed }
optimize module using [beta_reduction, tail_call, deforestation, rule_indexing, common_subexpression_elimination, tabling, proof_normalization]
lower module to DEEPML_LOGIC_R12
```

### What to inspect

- **Concepts:** r12_mcrt_lowering, optimize_logic, DEEPML_LOGIC_R12, R12, MCRT
- **Expected stage:** `runtime`
- **Expected result:** `pass`
- **Source identity:** `sha256:2b88e1d7b125f0c440559470eb3aa386d01fdebddb2cac2d1a76e232e276aa2d`
- **Semantic identity:** `sha256:5d6ad997ba8a521043702f7955fbf945e0dedd20547c2bfd22a9da3b2dfe25d3`

Read the program top-down once for syntax, then bottom-up for obligations. The header establishes language identity; policies constrain effects; declarations introduce types, functions, relations, or proofs; and terminal operations expose evaluation, inference, transformation, or certification intent. A correct implementation should be able to explain not only whether the program succeeds, but why the reported stage is the first decisive stage.

## Engineering checklist

- [ ] The language version and module identity are explicit.
- [ ] All names resolve within declared namespace boundaries.
- [ ] Types and pattern alternatives are complete and coherent.
- [ ] Effects are absent or explicitly declared and authorized.
- [ ] Recursive definitions have a termination or bounded-resource argument.
- [ ] Logic search strategy is explicit where operational behavior matters.
- [ ] Compiler transformations carry preservation evidence.
- [ ] Expected diagnostics identify the earliest responsible stage.
- [ ] R12 and MCRT identities can be traced without network access.
- [ ] Certification claims are separated from ordinary training examples.

## Laboratory 20

1. Locate `EX-DMLL-08574` in the technical corpus and verify its source hash.
2. Copy the program into a local air-gapped workspace and annotate every declaration.
3. Create one valid variation that preserves the `r12_mcrt_lowering` invariant.
4. Create one intentionally invalid variation and specify its expected failure stage.
5. Record the semantic identity, expected diagnostic, and replay evidence in a lab notebook.

### Deliverable

Submit the original record ID, the valid variation, the invalid variation, a one-page semantic comparison, and a validation table containing expected stage, result, diagnostic, source hash, and semantic hash.

## Review questions

1. Which semantic invariant is most important in `r12_mcrt_lowering`?
2. What evidence would distinguish modeled behavior from native execution?
3. Which negative case should be added before certifying an implementation?
4. How do purity, determinism, and policy interact in this chapter?

## Further corpus study

Filter `catalogs/CORPUS_INDEX.csv` for: proof_carrying_transform, r12_mcrt_lowering. Compare at least one positive, one negative, and—where available—one certification record. Identify which fields remain invariant across the three classes and which fields encode the expected failure.


# 21. Diagnostics, Safety, and Certification

> **Corpus focus:** `ambiguous_instance`, `impure_effect`, `incomplete_match`, `certification_logic`  
> **Representative record:** `EX-DMLL-06089` · tier `large_integrated_examples` · class `positive`

## Learning objectives

By the end of this chapter, the reader should be able to:

- Explain and apply **stage-specific diagnostics**.
- Explain and apply **negative examples**.
- Explain and apply **safety gates**.
- Explain and apply **holdout discipline**.

## Core idea

DeepML Logic/Functional treats source code as one layer of a larger evidence object. A construct is not complete merely because it parses: its type, purity, logical meaning, compiler identity, runtime behavior, diagnostics, and provenance must agree. In this chapter the key design space is stage-specific diagnostics, negative examples, safety gates, and holdout discipline. The practical discipline is to make each assumption explicit enough that another implementation can reproduce the same judgment without network access or hidden state.

The language's `pure_by_default` posture is architectural rather than decorative. It makes referential transparency the normal case, forces capabilities to appear at boundaries, and allows functions, rules, proofs, and compiler rewrites to be compared by semantic identity. Logic evaluation adds another dimension: operational search choices can affect termination and performance even when declarative meaning is stable. The corpus therefore records both denotational intent and operational evidence.

## Reading the evidence

A useful review separates four lenses:

- **SOPHIA:** Is the meaning coherent, typed, pure, and preserved?
- **CHARLOTTE:** Is the construct discoverable, consistently named, and represented across the corpus?
- **LANDON:** Can a compiler, validator, and runtime report deterministic evidence for it?
- **Professor + Podium:** Can a learner explain it, modify it, and diagnose its failure modes?

For `certification_logic`, the source record explains: This expert Logic Functional Language (DeepML) example teaches certification logic. It preserves the corpus-derived source → AST → typed/policy-verified semantic record → R12 → MCRT trace and uses deterministic IDs, hashes, provenance, and no-network safety. The example is expected to compile, lower, and produce deterministic runtime evidence.

## Worked corpus program

```deepml
deepml logic 0.3
module corpus.deepml_logic.example_06089
policy pure_by_default
policy no_network
knowledge_base Logic06089 {
  fact scene("PortalScene3")
  fact timeline("Sequence5")
  rule can_open(P) :- authorized(P), stable_scene(P)
  rule execute_sequence(S) :- can_open(portal_of(S)), certified(S)
}
plan PortalPlan06089 goal entered_destination actions [authorize, open_portal, play_timeline, traverse]
transform SceneRuleSet with proof { preserve semantics using theorem identity_composition }
workflow SymbolicNeural06089 { symbolic: Logic06089 neural: deepml.core::Graph06089 bridge: typed }
certify logic Logic06089 using proof_carrying
```

### What to inspect

- **Concepts:** certification_logic, integrate_certification_logic, DEEPML_LOGIC_R12, R12, MCRT
- **Expected stage:** `runtime`
- **Expected result:** `pass`
- **Source identity:** `sha256:bc3e5d4f56a86f2e7d6f9a04e524cb0ac9dd6c6bc3199768f0ecdec2de6f5e7a`
- **Semantic identity:** `sha256:f8b67f010092fc3906288f317c65baf67647041f8bdfa6bdd5919f7960b38b37`

Read the program top-down once for syntax, then bottom-up for obligations. The header establishes language identity; policies constrain effects; declarations introduce types, functions, relations, or proofs; and terminal operations expose evaluation, inference, transformation, or certification intent. A correct implementation should be able to explain not only whether the program succeeds, but why the reported stage is the first decisive stage.

## Engineering checklist

- [ ] The language version and module identity are explicit.
- [ ] All names resolve within declared namespace boundaries.
- [ ] Types and pattern alternatives are complete and coherent.
- [ ] Effects are absent or explicitly declared and authorized.
- [ ] Recursive definitions have a termination or bounded-resource argument.
- [ ] Logic search strategy is explicit where operational behavior matters.
- [ ] Compiler transformations carry preservation evidence.
- [ ] Expected diagnostics identify the earliest responsible stage.
- [ ] R12 and MCRT identities can be traced without network access.
- [ ] Certification claims are separated from ordinary training examples.

## Laboratory 21

1. Locate `EX-DMLL-06089` in the technical corpus and verify its source hash.
2. Copy the program into a local air-gapped workspace and annotate every declaration.
3. Create one valid variation that preserves the `certification_logic` invariant.
4. Create one intentionally invalid variation and specify its expected failure stage.
5. Record the semantic identity, expected diagnostic, and replay evidence in a lab notebook.

### Deliverable

Submit the original record ID, the valid variation, the invalid variation, a one-page semantic comparison, and a validation table containing expected stage, result, diagnostic, source hash, and semantic hash.

## Review questions

1. Which semantic invariant is most important in `certification_logic`?
2. What evidence would distinguish modeled behavior from native execution?
3. Which negative case should be added before certifying an implementation?
4. How do purity, determinism, and policy interact in this chapter?

## Further corpus study

Filter `catalogs/CORPUS_INDEX.csv` for: ambiguous_instance, impure_effect, incomplete_match, certification_logic. Compare at least one positive, one negative, and—where available—one certification record. Identify which fields remain invariant across the three classes and which fields encode the expected failure.


# 22. Smithson 8S Coupled Mechanics and the Capstone Toolchain

> **Corpus focus:** `certification_logic`, `r12_mcrt_lowering`, `planning_system`  
> **Representative record:** `EX-DMLL-05219` · tier `large_integrated_examples` · class `positive`

## Learning objectives

By the end of this chapter, the reader should be able to:

- Explain and apply **proposed coupling vocabulary**.
- Explain and apply **rho/psi/kappa/epsilon/chi evidence**.
- Explain and apply **air-gapped toolchain**.
- Explain and apply **capstone certification**.

## Core idea

DeepML Logic/Functional treats source code as one layer of a larger evidence object. A construct is not complete merely because it parses: its type, purity, logical meaning, compiler identity, runtime behavior, diagnostics, and provenance must agree. In this chapter the key design space is proposed coupling vocabulary, rho/psi/kappa/epsilon/chi evidence, air-gapped toolchain, and capstone certification. The practical discipline is to make each assumption explicit enough that another implementation can reproduce the same judgment without network access or hidden state.

The language's `pure_by_default` posture is architectural rather than decorative. It makes referential transparency the normal case, forces capabilities to appear at boundaries, and allows functions, rules, proofs, and compiler rewrites to be compared by semantic identity. Logic evaluation adds another dimension: operational search choices can affect termination and performance even when declarative meaning is stable. The corpus therefore records both denotational intent and operational evidence.

## Reading the evidence

A useful review separates four lenses:

- **SOPHIA:** Is the meaning coherent, typed, pure, and preserved?
- **CHARLOTTE:** Is the construct discoverable, consistently named, and represented across the corpus?
- **LANDON:** Can a compiler, validator, and runtime report deterministic evidence for it?
- **Professor + Podium:** Can a learner explain it, modify it, and diagnose its failure modes?

For `certification_logic`, the source record explains: This expert Logic Functional Language (DeepML) example teaches certification logic. It preserves the corpus-derived source → AST → typed/policy-verified semantic record → R12 → MCRT trace and uses deterministic IDs, hashes, provenance, and no-network safety. The example is expected to compile, lower, and produce deterministic runtime evidence.

## Worked corpus program

```deepml
deepml logic 0.3
module corpus.deepml_logic.example_05219
policy pure_by_default
policy no_network
knowledge_base Logic05219 {
  fact scene("PortalScene0")
  fact timeline("Sequence6")
  rule can_open(P) :- authorized(P), stable_scene(P)
  rule execute_sequence(S) :- can_open(portal_of(S)), certified(S)
}
plan PortalPlan05219 goal entered_destination actions [authorize, open_portal, play_timeline, traverse]
transform SceneRuleSet with proof { preserve semantics using theorem identity_composition }
workflow SymbolicNeural05219 { symbolic: Logic05219 neural: deepml.core::Graph05219 bridge: typed }
certify logic Logic05219 using proof_carrying
```

### What to inspect

- **Concepts:** certification_logic, integrate_certification_logic, DEEPML_LOGIC_R12, R12, MCRT
- **Expected stage:** `runtime`
- **Expected result:** `pass`
- **Source identity:** `sha256:3cab41535f6799e5c0a52bdd362eb5ea0d769275054e9f768b6e84f6ae25ce9a`
- **Semantic identity:** `sha256:7a85d0c48d85e6742d0da2916ef467cb515ad4de7a513849576597737ba000d4`

Read the program top-down once for syntax, then bottom-up for obligations. The header establishes language identity; policies constrain effects; declarations introduce types, functions, relations, or proofs; and terminal operations expose evaluation, inference, transformation, or certification intent. A correct implementation should be able to explain not only whether the program succeeds, but why the reported stage is the first decisive stage.

## Engineering checklist

- [ ] The language version and module identity are explicit.
- [ ] All names resolve within declared namespace boundaries.
- [ ] Types and pattern alternatives are complete and coherent.
- [ ] Effects are absent or explicitly declared and authorized.
- [ ] Recursive definitions have a termination or bounded-resource argument.
- [ ] Logic search strategy is explicit where operational behavior matters.
- [ ] Compiler transformations carry preservation evidence.
- [ ] Expected diagnostics identify the earliest responsible stage.
- [ ] R12 and MCRT identities can be traced without network access.
- [ ] Certification claims are separated from ordinary training examples.

## Laboratory 22

1. Locate `EX-DMLL-05219` in the technical corpus and verify its source hash.
2. Copy the program into a local air-gapped workspace and annotate every declaration.
3. Create one valid variation that preserves the `certification_logic` invariant.
4. Create one intentionally invalid variation and specify its expected failure stage.
5. Record the semantic identity, expected diagnostic, and replay evidence in a lab notebook.

### Deliverable

Submit the original record ID, the valid variation, the invalid variation, a one-page semantic comparison, and a validation table containing expected stage, result, diagnostic, source hash, and semantic hash.

## Review questions

1. Which semantic invariant is most important in `certification_logic`?
2. What evidence would distinguish modeled behavior from native execution?
3. Which negative case should be added before certifying an implementation?
4. How do purity, determinism, and policy interact in this chapter?

## Further corpus study

Filter `catalogs/CORPUS_INDEX.csv` for: certification_logic, r12_mcrt_lowering, planning_system. Compare at least one positive, one negative, and—where available—one certification record. Identify which fields remain invariant across the three classes and which fields encode the expected failure.


# Appendices

## A. Corpus navigation

- `corpus/technical/` — normalized master corpus, schema, guide, and shards.
- `catalogs/CORPUS_INDEX.csv` — record-level navigation.
- `catalogs/TOPIC_ATLAS.md` — conceptual map of all topics.
- `scripts/` — 1,000 source-faithful programs.
- `validation/` — conformance cases and claim discipline.
- `tools/` — offline inspection and structural validation.

## B. Recommended assessment model

- 25% functional-language laboratories
- 25% logic and proof laboratories
- 20% compiler and optimization evidence
- 15% diagnostics and negative cases
- 15% capstone conformance report

## C. Glossary

**Semantic identity:** Stable digest or relation representing program meaning under the corpus model.  
**R12:** Compiler-side relation identity represented in corpus evidence.  
**MCRT:** Runtime/replay relation identity represented in corpus evidence.  
**Certification holdout:** A case reserved for final evaluation rather than iterative tuning.  
**Pure by default:** Effects are prohibited unless explicitly declared and authorized.  
**Proof-carrying transform:** Optimization or rewrite paired with evidence that required semantics are preserved.  
**Tabling:** Storage of intermediate logic goals and answers to avoid redundant evaluation.  
**Occurs check:** Unification check that prevents construction of an infinite self-containing term.
