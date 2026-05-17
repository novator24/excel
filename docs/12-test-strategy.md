# Test Strategy

## Layers

- Unit tests:
  - formula evaluation
  - route mapping direction/trapezoid selection
  - risk scoring
  - Excel rendering
- Integration tests:
  - backend API + postgres
  - provider adapter normalization
- Contract tests:
  - provider schema contracts
  - API OpenAPI backward compatibility
- E2E:
  - UI -> quote -> Excel download
- Non-functional:
  - load (k6)
  - security (OWASP baseline)
  - resilience (dependency outage fallback)

## Test data

- Golden datasets for arctic, storm, and sanctions scenarios.
- Snapshot tests for deterministic quote outputs.
