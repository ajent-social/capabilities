# Worklog

2026-09-22: Repository foundation prepared from sanitized behavioral requirements. Original public RFC, candidate/rejection metadata, strict schema and deterministic catalog tooling added. Implementation and real consumer adoption remain pending. See validation.md for executed checks. No private census documents or source code were copied.


## 2026-09-22 — First candidate runtime implementation

identity.service-credentials now references an immutable implementation revision
and separate evidence summary in ajent-social/go. Lifecycle remains CANDIDATE;
human maintainer review is NOT_RUN. Public contract/security tests and public
source provenance are distinct from restricted, maintainer-reported application
branch verification. No private consumer identity, source path or revision is
published. No deployment, second-consumer migration or production adoption is
claimed.

Catalog generation/check and all 12 catalog tests passed. The validator initially
rejected a URL attached to restricted evidence; the record was corrected to keep
restricted evidence URL-free, without weakening validation. Other identity,
billing, infrastructure and delivery capabilities retain their existing statuses.

## 2026-09-23 — Review corrections

The service-credential entry records public REAL_CONSUMER verification as
NOT_RUN. A local maintainer-reported integration remains labelled restricted and
does not establish public adoption. The upstream bbolt provenance link is pinned
to an immutable commit. Go PR #1 is merged at
`2bb7b6d4f54e35a676c61d90ffce1e18b365e60a`; implementation and verification
links now point to that merged revision and its exact CI run. Two headless
Opus 5.5 review rounds and focused follow-ups found and corrected security,
portability and evidence issues. AI review does not count as human maintainer
review; the capability remains CANDIDATE and HUMAN_REVIEW is NOT_RUN.

## 2026-09-23 — MCP OAuth candidate contract

identity.mcp-oauth added as CANDIDATE / EXTRACT: a bounded OAuth 2.1
authorization server plus bearer verification for one MCP resource with public
PKCE S256 clients, exact redirect binding, RFC 8707 resource binding, public-only
dynamic client registration, fixed-issuer metadata, expiry and revocation.
Login, consent rendering, CSRF and live ownership policy stay with the product.
Refresh tokens and remote client metadata fetches are excluded from the first
slice and are not advertised.

Provenance is an existing maintainer implementation (restricted, not
independently verifiable) with a proposed public first consumer. The Go
extraction is on an unmerged branch, so no implementation revision is recorded
and all four verification kinds are NOT_RUN placeholders pointing at the branch;
they must be replaced with a pinned commit, its CI run and consumer verification
before any promotion. No adoption, deployment or human review is claimed.

Catalog regenerated and checked with 13 records; 12 catalog tests pass.

## 2026-09-24 — MCP OAuth contract aligned with implementation

Added strict rotating refresh grants required by native client registration,
separate default-off localhost callback compatibility, pinned Go implementation
and passing public library CI evidence. Linked the real Serenity consumer PR
evidence; public consumer CI and human maintainer review remain pending.
Status remains CANDIDATE. No private source identity or production adoption
is published. Catalog generation/check and all 12 schema tests pass.

Consumer evidence update: Serenity PR #271 public hosted-browser job passes
six real-service signup/consent flows. REAL_CONSUMER is PASS for that candidate
integration only; no production adoption or cloud qualification is inferred.
