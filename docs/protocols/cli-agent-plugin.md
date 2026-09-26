# CLI-backed coding-agent host plugin contract

**Status: discovery contract with one reference implementation.** This document
specifies the reusable behavior AMSL has actually identified so far. It does
not define a universal plugin API, runtime, marketplace, or skills corpus.

## Boundary

A host package makes a canonical, already-installed command-line tool easier to
invoke from an agent host. The CLI remains the source of product behavior,
configuration, authentication, provider calls, output, and version support. The
host package contains only the host-native entry point and user-facing
instructions needed to invoke that CLI safely.

## Contract

1. **Native entry point.** Use the host's documented skill, command, or plugin
   package format. Keep host-specific metadata at the boundary.
2. **Canonical CLI.** Invoke the installed CLI and its documented arguments.
   Do not fork, reimplement, or silently substitute its behavior.
3. **Explicit user intent.** State what user invocation triggers and whether it
   can cause network access, provider charges, or file writes. Preserve the
   host's normal command-approval settings.
4. **Bounded inputs.** Identify the supported input shape and ask when the
   target is ambiguous or exceeds the CLI's documented scope. Send only inputs
   the user supplied or approved.
5. **Credential boundary.** Let the CLI use its established configuration and
   secret mechanism. Do not read, display, copy, or store secret values in the
   host package.
6. **Visible failures.** If the CLI is absent, misconfigured, incompatible, or
   returns an error, report that result. Do not simulate a successful run or
   fall back to a different engine.
7. **Traceable output.** Direct the user to the CLI's saved artifacts and
   report provider-reported usage or cost without inventing missing values.
8. **No implicit edits.** Applying proposed changes to source material requires
   a separate user request unless the canonical CLI explicitly owns that edit.

## Conformance evidence

For each host package, maintainers should verify:

- the native manifest and referenced entry point are accepted by that host;
- the host can discover and invoke the workflow;
- the installed CLI receives one supported input and the intended context;
- no secret value is surfaced or copied by the package;
- missing CLI/configuration and CLI failure are visible;
- outputs and any network/cost effects are disclosed accurately;
- host packages remain aligned with the canonical workflow text.

Repository-level schema checks and CLI dry-runs are packaging/contract checks;
they do not prove an actual host installation or independent consumer adoption.
Do not promote maturity based on those checks alone.

## Quorum reference implementation

Quorum provides Codex, Claude Code, and Cursor entry points in the public
[`dndungu/quorum` repository](https://github.com/dndungu/quorum/tree/feature/amsl-agent-host-plugins/plugins).
All invoke the installed `quorum` CLI. They provide no hooks, MCP server,
credential handler, background process, or alternate review engine. The
[`plugins/README.md`](https://github.com/dndungu/quorum/blob/feature/amsl-agent-host-plugins/plugins/README.md)
documents installation and host-specific limits.

This implementation is an example against which to test the contract. Its
availability in three host formats does not establish independent consumer
verification or justify extracting a shared runtime.
