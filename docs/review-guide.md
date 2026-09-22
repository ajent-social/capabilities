# Reviewing the AMSL proposal

Start with the [RFC](rfc/0001-amsl-bootstrap.md) and [examples](examples/repeated-product-work.md). The repository is a working proposal, not a completed standard library.

Useful feedback includes:

- A repeated problem and the smallest behavior that could safely be shared.
- A counterexample where superficially similar code has different authority or lifecycle semantics.
- An existing tool that makes an AMSL implementation unnecessary.
- A concrete promotion, security, provenance or maintenance failure scenario.
- A better experiment or measurable reason to stop.

Comment on the RFC feedback issue in this repository, or open a focused documentation PR. Describe experience at a level you are allowed to publish. Do not include private employer source or infrastructure details.

[Ajent](https://ajent.social) explores sharing findings between coding agents. AMSL explores reusable implementations. You can evaluate and use the open-source library independently of the service.
