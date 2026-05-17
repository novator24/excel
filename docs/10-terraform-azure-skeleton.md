# Terraform Skeleton (Azure)

## Modules

- `network`: vnet, subnets, nat, private dns.
- `aks`: cluster, node pools, identities.
- `data`: postgres, blob, key vault.
- `observability`: log analytics, managed grafana (optional).
- `security`: role assignments, policy.

## Directory

```text
infra/terraform/azure/
  modules/
    network/
    aks/
    data/
    observability/
    security/
  envs/
    dev/
    test/
    prod/
```

## State and secrets

- Remote backend: Azure Storage account + state locking.
- Sensitive variables from Key Vault or CI secure vars.

## Baseline policy

- Private endpoints for data services.
- AKS workload identity.
- Deny public access on storage and database where feasible.
