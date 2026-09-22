# 0002: separate contracts and implementations

Status: accepted for repository bootstrap, 2026-09-22.

Language-neutral contracts live separately from Go, Pulumi and delivery implementations. One monolithic library would confuse runtime and execution boundaries.

Scope: repository foundation under the public/open-source requirement. The RFC remains open for feedback; this does not approve unimplemented security-sensitive APIs.
