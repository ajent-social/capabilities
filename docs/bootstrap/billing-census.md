# Billing Census

Customer linkage and checkout recovery repeat as a boundary; durable retry behavior needs an explicit contract. Subscription reconciliation is a separate candidate. Duplicate/out-of-order events and lost responses require tests. Entitlement policy, prices and grace periods stay product-specific. Use the provider SDK; do not create fake multi-provider adapters.
