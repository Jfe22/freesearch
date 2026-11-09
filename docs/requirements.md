# Requirements — Secure Knowledge Assistant
**Status:** Draft v0.1

## Purpose
Make it easier to find information across technical PDFs through question answering grounded in document passages, with visible source references. This is a portfolio project demonstrating software engineering, applied RAG, testing, and security-aware design.

## Intended users
- MVP: developer using a local instance and non-sensitive sample documents.
- Version 2: authenticated users restricted to documents they are authorized to access.
- Portfolio reviewers inspecting code, documentation, tests, and demo.

## MVP functional requirements
| ID | Requirement | Acceptance criteria |
|---|---|---|
| FR-01 | PDF upload | Valid PDF accepted and assigned a document ID. |
| FR-02 | File validation | Invalid, empty, malformed, or over-limit files rejected clearly. |
| FR-03 | Text extraction | Text extracted; page metadata retained where available. |
| FR-04 | Chunking | Text split into bounded, overlapping chunks with source metadata. |
| FR-05 | Embeddings | Each chunk embedded using a configured model. |
| FR-06 | Indexing | Vectors and metadata stored in ChromaDB. |
| FR-07 | Retrieval | A question retrieves relevant indexed passages. |
| FR-08 | Answer generation | LLM answers using retrieved context. |
| FR-09 | Source references | Answer identifies source document and page/chunk references. |
| FR-10 | Uncertainty | Insufficient evidence produces an explicit fallback, not an invented answer. |

## Non-functional requirements
- Maintainable separation of API, business logic, persistence, retrieval, and model providers.
- Core tests must run without a paid LLM API.
- Setup documented for macOS Apple Silicon.
- Use synthetic/public sample documents; do not commit confidential files.
- Validate inputs, protect secrets, and enforce authorization before exposing data.
- Record model/configuration and retrieval parameters during evaluation.
- Local embeddings by default; external LLM use optional and configurable.

## Version 2 — security and identity
Authentication; authorization on every document operation; ownership and per-user retrieval isolation; secure credential/session handling; file limits; cross-user access-denial tests; prompt-injection analysis and mitigations; safe secrets and logs.

## Version 3 — portfolio completion
Vue.js interface; document listing/deletion; privacy-aware conversation history; repeatable RAG evaluation; Docker setup; CI; demo using synthetic documents; documented limitations.

## Out of scope initially
Commercial billing, public multi-tenant hosting, high availability, guaranteed protection against every prompt-injection technique, confidential/regulated data, and OCR for scanned PDFs.

## MVP definition of done
A developer can run the documented local setup, upload a text-based PDF, ask a question, receive a grounded answer with source references, see an uncertainty fallback when evidence is insufficient, and run the automated test suite.
