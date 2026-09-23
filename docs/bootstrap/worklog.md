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

The service-credential entry now records public REAL_CONSUMER verification as
NOT_RUN. A local maintainer-reported integration remains labelled restricted and
does not establish public adoption. The upstream bbolt provenance link is pinned
to the full commit that introduced the source file. Implementation and test
evidence revisions will be pinned after the Go PR is merged and reverified.
