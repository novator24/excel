# MCP Server Recommendations

## Recommended MCP servers

- Files/workspace: local filesystem MCP.
- Git: git MCP for branch, diff, commit introspection.
- PostgreSQL: postgres MCP for schema and query checks.
- API/HTTP: generic HTTP MCP for provider contract tests.
- Azure: Azure CLI/ARM MCP wrapper (or shell + az fallback).
- Kubernetes: kubectl MCP (or shell fallback).
- Browser/docs: docs web fetch MCP.
- Diagrams: Mermaid renderer MCP or markdown preview workflow.
- Testing: pytest/jest command MCP wrappers.
- Secrets-safe env handling: vault/keyvault MCP with masked output.
- Spreadsheets/Excel: python execution MCP with openpyxl/xlsxwriter helpers.

## If MCP not available

Use equivalent:

- CLI tools (`az`, `kubectl`, `helm`, `argocd`) via controlled shell.
- Secure `.env` injection through CI secret stores.
- Python scripts for Excel and data validation.

## Connection pattern

1. Keep credentials outside repo.
2. Scope each MCP server to least privilege.
3. Add audit logs for MCP actions in CI and local scripts.
