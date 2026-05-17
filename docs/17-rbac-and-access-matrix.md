# RBAC and Access Matrix

## Roles

- `admin`
- `analyst`
- `operator`
- `viewer`
- `external_client`

## Permissions

- `admin`:
  - manage users/roles
  - activate/deactivate providers
  - edit coefficients and formula versions
  - restrict columns/fields/sources
  - view all audit and exports
- `analyst`:
  - run calculations
  - create scenarios
  - view full risk classifier
  - export Excel for own tenant
- `operator`:
  - run and re-run calculations
  - limited coefficient override within admin-defined bounds
  - view operational risk summaries
- `viewer`:
  - read-only quote summaries
  - no raw provider payload access
- `external_client`:
  - access only explicitly shared quote IDs and generated Excel files
  - no internal risk or source details

## Data isolation controls

- Tenant-aware row filtering in API and DB queries.
- Signed expiring URLs for Excel download.
- Field masking policy per role.
