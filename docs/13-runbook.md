# Operations Runbook

## Common incidents

1. Provider outage:
   - switch to fallback provider in admin panel.
   - verify adapter health and cache TTL.
2. Quote latency spike:
   - inspect tracing by endpoint.
   - check cache hit ratio and DB slow queries.
3. Excel generation errors:
   - inspect generator logs + blob permissions.
4. Incorrect risk coefficients:
   - roll back active formula version.
   - re-run impacted quote set.

## Recovery actions

- Postgres restore: latest PITR point.
- ClickHouse restore: replicated part recovery.
- AKS rollback: Argo CD sync to previous revision.

## SLO and alerts

- API availability 99.9%.
- Calculate p95 < 2.5s.
- Failed quote ratio < 1%.
- Alert channels: Teams/Slack + pager.
