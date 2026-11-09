# ADR-001: Initial technology stack
- **Status:** Accepted (initial direction)
- **Date:** 2026-11-09

## Context
Portfolio project combining backend engineering, applied RAG, and security-aware design. Developer has Python/Vue familiarity and uses an Apple Silicon Mac with 18 GB unified memory and limited free SSD space.

## Decision
Python + FastAPI; PostgreSQL for metadata; ChromaDB for vector search; Vue.js; Pytest; Git/GitHub; local embeddings initially; provider-independent LLM adapter; Docker introduced when useful.

## Rationale
Python has a mature AI ecosystem. FastAPI is focused on APIs. Vue reuses existing experience. PostgreSQL suits relational metadata and ChromaDB provides local vector search. Native development reduces initial setup overhead.

## Consequences
Keep provider code behind interfaces; keep embedding model consistent; document local persistence/reset; defer Docker, not exclude it; revisit based on evidence.
