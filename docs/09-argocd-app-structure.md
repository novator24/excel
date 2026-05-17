# Argo CD Application Structure

```text
infra/argocd/
  projects/
    fertifreight.yaml
  applications/
    dev-platform.yaml
    test-platform.yaml
    prod-platform.yaml
```

## Application model

- One Argo project per business platform.
- One app per environment.
- Source: helm chart in this repo.
- Destination: dedicated namespace per env.
- Sync policy:
  - dev: automated prune/self-heal.
  - test/prod: manual sync with policy checks.
