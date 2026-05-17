# Repository Structure

## Recommended model: monorepo

Trade-off:

- Pros: shared contracts, lower CI overhead, easier refactoring, single release cadence for small team.
- Cons: larger CI scope, stricter ownership boundaries required.

Decision: monorepo now; if teams split by domain later, extract `frontend` and `data-pipeline` first.

## Tree

```text
apps/
  frontend/
  admin-console/
services/
  backend-api/
  route-service/
  weather-service/
  maritime-data-service/
  auth-service/
packages/
  calculator-engine/
  excel-generator/
data-pipeline/
  airflow/
  dbt/
infra/
  terraform/azure/
  helm/charts/
  argocd/
docs/
```

## Boundaries

- `services/*` never import from `apps/*`.
- Business formulas live only in `packages/calculator-engine`.
- Excel formatting logic lives only in `packages/excel-generator`.
- Ingestion code writes to normalized bronze/silver contracts before dbt marts.
