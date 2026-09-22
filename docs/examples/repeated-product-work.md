# Examples: work that should not restart with every project

These are generic illustrative scenarios inspired by recurring product engineering. They disclose no source application and make no claim of measured savings or completed AMSL adoption.

## A command-line tool becomes a paid hosted service

A developer has a useful local tool. Offering it as a monthly service adds human sign-in, revocable API credentials, hosted checkout, subscription reconciliation and a paid-access check. The engine itself remains product-specific.

The reusable opportunity is not an entire SaaS framework. It may be credential lifecycle and checkout recovery. The provider still handles payments; the product still decides what a subscription permits. An MCP interface can use the official SDK while retaining product-specific tool authorization.

Question: which shared behavior would actually remove code from a second service without forcing both into the same user model?

## Two subscription products disagree about grace periods

Both receive payment-provider events, but one allows a grace period after payment failure and the other suspends access immediately. Events can duplicate or arrive out of order in either product.

Reconciliation may be shared; entitlement policy should remain explicit. A common enum called SubscriptionStatus does not justify one access predicate.

Question: can the contract guarantee convergent local state without claiming exactly-once effects it cannot prove?

## Several services need secure cloud deployment

Each repository needs short-lived deployment credentials, a private database and secret access. Repeated resource declarations can drift toward broader trust or accidental public access.

A provider-specific component can encode narrow defaults. A policy pack can reject unsafe resources outside the component. Live denied-access and restore tests establish behavior that generated-property tests cannot.

Question: what belongs in the component, what belongs in enforced policy, and what must the caller choose explicitly?

## CI carries lessons that a copied template forgets

One service must preserve main-branch image builds while canceling obsolete PR tests. Another must verify every supported release architecture. Both need narrowly scoped credentials and a reliable failure result.

Share bounded jobs and regression cases; keep product triggers, required checks and deployment approval local. A copied starter template will not distribute the next fix.

Question: is a reusable workflow the smallest useful unit, or is a composite action plus caller-owned jobs safer?
