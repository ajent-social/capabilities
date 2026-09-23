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
