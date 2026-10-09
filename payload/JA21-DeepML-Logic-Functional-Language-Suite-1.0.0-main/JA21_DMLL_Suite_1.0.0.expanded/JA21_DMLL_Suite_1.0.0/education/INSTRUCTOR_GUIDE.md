# Instructor Guide

## Course purpose

Teach the Logic/Functional segment of JA21 as a unified language, corpus, compiler-evidence, and conformance discipline.

## Recommended prerequisites

Students should understand typed programming, recursive data, basic discrete mathematics, and command-line file inspection. Prior theorem-proving or logic-programming experience is useful but not required.

## Teaching method

1. Begin with source meaning, not syntax memorization.
2. Pair every positive example with a negative example.
3. Require explicit expected stages before tools are run.
4. Grade explanations and evidence tables, not only final output.
5. Keep certification holdouts outside ordinary practice sessions.
6. Require air-gapped reproducibility for the capstone.

## Assessment

| Component | Weight |
|---|---:|
| Weekly laboratories | 30% |
| Corpus and diagnostic notebooks | 20% |
| Midterm knowledge-base/planning project | 15% |
| Compiler preservation dossier | 15% |
| Final conformance capstone | 20% |

## Answer-quality rubric

A strong answer identifies the construct, states its semantic invariant, names the earliest decisive stage, cites a record ID, distinguishes expected from observed behavior, and explains how hashes or proof evidence support reproducibility.

## Safety and claim discipline

Do not award credit for claims of native compilation or runtime execution unless students provide a real toolchain, invocation transcript, versioned environment, and reproducible outputs. The bundled Python validator checks structure only.
