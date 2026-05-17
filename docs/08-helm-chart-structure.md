# Helm Chart Structure

```text
infra/helm/charts/platform/
  Chart.yaml
  values.yaml
  values-dev.yaml
  values-test.yaml
  values-prod.yaml
  templates/
    _helpers.tpl
    namespace.yaml
    backend-api/deployment.yaml
    backend-api/service.yaml
    backend-api/hpa.yaml
    route-service/deployment.yaml
    weather-service/deployment.yaml
    maritime-data-service/deployment.yaml
    auth-service/deployment.yaml
    ingress.yaml
    network-policy.yaml
    service-monitor.yaml
    sealed-secret-ref.yaml
```

## Conventions

- One sub-template per workload.
- Secrets are references (Key Vault CSI / external secrets), never inline.
- Environment-specific values files.
- Global labels include `app`, `team`, `env`, `cost-center`.
