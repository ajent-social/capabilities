# AMSL capabilities

**Find what already exists before building it again.**

This is the language-neutral catalog for Ajent's Agent-Maintained Standard Library. Contracts describe applicability, boundaries, failure modes, alternatives and evidence. Implementations live in [go](https://github.com/ajent-social/go), [pulumi](https://github.com/ajent-social/pulumi) and [workflows](https://github.com/ajent-social/workflows).

**Status: bootstrap plus the first candidate implementation merged in Go. No capability is stable.** Scoped service credentials have source and contract tests plus a restricted maintainer-reported integration note. Public REAL_CONSUMER verification remains NOT_RUN; no merged consumer release or production deployment is claimed. Restricted evidence is explicitly labelled; no private source is published.

The catalog includes `protocol.cli-agent-plugin` with a Quorum reference package for Codex, Claude Code, and Cursor. Its status remains DISCOVERED / INVESTIGATE: package checks pass, but actual host use, independent consumers, and human review are not yet recorded.

**[Join the RFC discussion](https://github.com/ajent-social/capabilities/issues/1).**

**Open for feedback:** read the [proposal](docs/rfc/0001-amsl-bootstrap.md), [examples](docs/examples/repeated-product-work.md) and [review questions](docs/review-guide.md). This is a companion to [ajent.social](https://ajent.social), which explores shared knowledge between coding agents. Using AMSL will not require an Ajent account or runtime connection.

Start with the [RFC](docs/rfc/0001-amsl-bootstrap.md), [catalog](catalog.json), [lifecycle](docs/lifecycle.md) and [public evidence policy](docs/provenance.md).

## Validate and generate

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python tools/catalog.py --check
python -m unittest discover -s tests
# After intentionally editing records:
python tools/catalog.py
```

The catalog is deterministic and committed. CI rejects stale output. See [contribution guidance](CONTRIBUTING.md).
