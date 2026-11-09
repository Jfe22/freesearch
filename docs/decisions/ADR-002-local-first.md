# ADR-002: Local-first development and cost control
- **Status:** Accepted
- **Date:** 2026-11-09

## Context
The project demonstrates skills rather than operating commercially. Development machine: Apple M3 Pro, 18 GB unified memory, approximately 35 GB free SSD. Recurring costs are undesirable.

## Decision
Develop locally first. Use local embeddings where practical. Keep generation behind an adapter so a local model or external API can be selected by configuration. Do not deploy a public server during the MVP.

## Rationale
Minimizes cost and provider lock-in, and allows the RAG pipeline to be tested without paid API access.

## Consequences
Measure local model performance rather than assume it; manage model files carefully; support fake adapters in tests; consider public demo later, not as an MVP prerequisite.
