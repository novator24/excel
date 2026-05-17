# CI/CD Pipeline

## Toolchain

- CI: GitHub Actions (or GitLab CI equivalent).
- Build: Docker BuildKit.
- Deploy: Helm charts + Argo CD (GitOps).

## Pipeline stages

1. `lint`: ruff, mypy, eslint.
2. `test`: unit/integration tests.
3. `build`: container images for each service.
4. `scan`: Trivy image scan + dependency scan.
5. `publish`: push image + SBOM.
6. `gitops-update`: update environment values repo.
7. Argo CD sync by policy.

## Promotion

- dev: auto after merge to main.
- test: manual approval.
- prod: change window + two-person review.

## Required quality gates

- Test coverage >= 75% backend/calculator.
- No critical vulnerabilities.
- Contract tests pass.
- Helm dry-run and kubeconform pass.
