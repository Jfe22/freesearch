# Testing Strategy
**Status:** Draft v0.1

## Principles
- Test deterministic logic independently of external LLMs.
- Use isolated temporary storage and test databases.
- Use synthetic/public documents and fake model adapters.
- Test success, invalid input, failure, and security boundaries.

## Layers
1. Unit: file validation, chunking, metadata mapping, prompt construction, config validation.
2. Integration: API, persistence, vector store.
3. Contract: embedding and LLM adapters using fakes/mocks.
4. Security: malformed uploads, access denials, cross-user retrieval attempts, prompt-injection cases.
5. RAG evaluation: retrieval relevance, source correctness, groundedness, insufficient-context behaviour.

## MVP acceptance checks
Valid PDF accepted; invalid/empty PDF rejected; page references retained where possible; chunk metadata maps to source; retrieval works on known questions; answers include references; unsupported questions trigger uncertainty; automated tests run without a paid API.

## Later automation
Add GitHub Actions for formatting/linting and tests once the environment and first backend slice exist.
