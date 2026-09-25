# Active-repo census — AMSL extract priorities (2026-09-25)

Maintainer-operated census of repositories under admin-owned GitHub
organizations. **Identifying organization and private product names are
omitted** (public AMSL repos must not publish private census documents).
Methodology and raw inventory remain maintainer-restricted. Cutoff: pushed
since 2025-03-24, not archived, non-fork.

## Scale (aggregate only)

| Measure | Count |
| --- | --- |
| Unique repos | 381 |
| Active last 18 months | 170 |
| Active non-fork | 130 |

## Workflow pattern counts (sampled active product workflows)

| Pattern | Workflow files |
| --- | --- |
| `actions/setup-go` | 59 |
| `go test` | 35 |
| `goreleaser` | 15 |
| `golangci-lint` | 14 |
| `pulumi` | 14 |
| `docker/build-push` | 5 |
| `cosign` / `trivy` | 5 each |
| `configure-aws-credentials` | 5 |
| `ajent-social/workflows` already called | 2 (public: `ajent-social/go`, `zerfoo/zerfoo`) |

## Map to AMSL

| Repeated seam | AMSL action |
| --- | --- |
| go test / vet | `delivery.go-validation` (exists) |
| goreleaser / gh release assets | `delivery.go-release` |
| docker build + scan/sign | `delivery.container-artifact` |
| pulumi preview / deploy OIDC | `delivery.infrastructure-preview` |
| golangci-lint | `delivery.go-lint` |
| SSM params / NLB TLS | `paramstore` / `nlbedge` |
| Cloudflare DNS-only alias to ALB | `cloudflare/dnsalias` |
| GitHub OIDC deploy roles | already `oidcprovider` + `deploymentidentity` — **adopt** |
| Stripe webhook verify | already `billing/stripeverify` — **adopt** |
| Provider webhook formats (non-AMSL HMAC) | keep product-local |
| Full audit logging stacks | single-consumer — defer |
| Proxied CDN / zone create / page rules | product-local |

## Explicit non-goals from this census

Marketing sites, package taps, one-off notebooks, and stacks outside AMSL
Go / Pulumi / workflows bootstrap scope.
