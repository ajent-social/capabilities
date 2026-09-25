# Active-repo census — AMSL extract priorities (2026-09-25)

Source: GitHub CLI over `dndungu` + 34 admin orgs. Cutoff: pushed since
2025-03-24, not archived, non-fork.

## Scale

| Measure | Count |
| --- | --- |
| Unique repos | 381 |
| Active last 18 months | 170 |
| Active non-fork | 130 |
| Product-ish (excl. sites/taps/docs) scanned via API + local disk | ~50 |

Top active orgs by non-fork repo count: `dndungu`, `sirerun`, `sajili-biz`,
`zerfoo`, `shiftmesh`, `ajent-social`, `feza-ai`, `kazi-org`, `narrate-it`.

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
| `ajent-social/workflows` already called | 2 (`go`, `zerfoo`) |

## Map to AMSL

| Repeated seam | AMSL action |
| --- | --- |
| go test / vet | `delivery.go-validation` (exists) |
| goreleaser / gh release assets | `delivery.go-release` (P1 PR) |
| docker build + scan/sign | `delivery.container-artifact` (P1 PR) |
| pulumi preview / deploy OIDC | `delivery.infrastructure-preview` (P1 PR) |
| golangci-lint | `delivery.go-lint` (this wave) |
| SSM params / NLB TLS | `paramstore` / `nlbedge` (P1 PR) |
| Cloudflare DNS-only alias to ALB | `cloudflare/dnsalias` (this wave) |
| GitHub OIDC deploy roles | already `oidcprovider` + `deploymentidentity` — **adopt** |
| Stripe webhook verify | already `billing/stripeverify` — **adopt** |
| Svix / Resend ingress | keep product-local |
| CloudTrail+FlowLogs+Budgets | single strong consumer (blink) — defer |
| Proxied Cloudflare / zone create / page rules | product-local (postiz) |

## Explicit non-goals from this census

Personal sites, homebrew taps, marketing HTML, one-off ML notebooks, and
Elixir/Ruby/Dart stacks outside AMSL Go/Pulumi/workflows bootstrap scope.
