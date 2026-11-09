# Free Search

Portfolio project: secure, document-grounded question answering using Retrieval-Augmented Generation (RAG).

**Status:** Planning / initial setup. The first target is a local MVP.

## Goals
- Upload PDF documents, extract and chunk their text.
- Create embeddings and retrieve relevant passages.
- Answer questions using retrieved evidence and show source references.
- Treat security, privacy, testing, and transparent limitations as core requirements.

## Planned stack
Python + FastAPI; PostgreSQL for application metadata; ChromaDB for vector search; local embeddings; provider-independent LLM adapter; Vue.js; Pytest; Git/GitHub. Docker will be introduced when useful for reproducible multi-service setup.

## Versions
### MVP
PDF upload, validation, text extraction, chunking, embeddings, semantic retrieval, grounded answers, source references, automated tests.
### Version 2 — Security and identity
Authentication, authorization, document ownership/isolation, safe upload handling, prompt-injection mitigations, security tests.
### Version 3 — Portfolio completion
Vue.js interface, document/conversation management, RAG evaluation, Docker, CI, privacy-conscious logging, screenshots/demo and polished documentation.

## Repository map
- `backend/` — FastAPI application
- `frontend/` — Vue.js application
- `docs/requirements.md` — scope and acceptance criteria
- `docs/architecture.md` — component design
- `docs/threat-model.md` — initial security analysis
- `docs/testing.md` — test strategy
- `docs/decisions/` — Architecture Decision Records

## Development principles
1. Work in small increments with acceptance criteria.
2. Test success, failure, and security-relevant paths.
3. Record important technical decisions as short ADRs.
4. Never commit secrets, API keys, private documents, or real user data.
5. Only claim security controls that are implemented and tested.

## Limitations
This is an educational portfolio project, not a production-ready service. The local MVP is for non-sensitive sample documents and is not intended for untrusted multi-user use.

## License
MIT. See `LICENSE`.
