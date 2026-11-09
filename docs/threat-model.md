# Initial Threat Model
**Status:** Draft v0.1. Lightweight working analysis, not a security certification.

## Assets
PDFs and extracted text; metadata and ownership; embeddings/vector metadata; credentials and tokens (Version 2); LLM API keys; questions, retrieved context, answers, and logs.

## Trust boundaries
Client-to-FastAPI; uploaded files-to-parser; backend-to-PostgreSQL/ChromaDB; backend-to-external LLM; one user's data versus another's (Version 2).

## Threats and planned controls
| Threat | Example | Planned control / validation |
|---|---|---|
| Malformed PDF | Parser crash/resource exhaustion | Size limits, validation, controlled errors, parser tests |
| Fake PDF | Extension differs from content | Validate content and parser result; do not trust filename |
| Prompt injection | Document tells model to ignore instructions | Treat retrieved text as untrusted; explicit instruction/data boundaries; adversarial tests |
| Hallucination | Answer goes beyond evidence | Ground in retrieved context; uncertainty fallback; evaluation |
| Secret leakage | API key committed | Environment variables; `.env` ignored; placeholder `.env.example` |
| Cross-user exposure | User A retrieves User B's chunks | Version 2 authorization filters and negative integration tests |
| Sensitive logs | Full documents/tokens logged | Minimize logs; never log secrets/full content |
| Vulnerable dependency | Unsafe package version | Managed dependencies and periodic review |

## Principles
Least privilege; deny by default; validate untrusted input; treat document content and model output as untrusted; keep secrets out of source control; minimize personal data; make claims only when controls are tested.

## MVP limitations
The MVP is local and for non-sensitive sample documents. It is not hardened for untrusted multi-user access. Authentication and multi-user authorization are deferred to Version 2.

## Validation plan
Test invalid/empty/oversized uploads, missing configuration, insufficient retrieval context, and prompt-injection examples. Add cross-user authorization tests before claiming Version 2 complete.
