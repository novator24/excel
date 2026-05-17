# Excel Template Design

## Sheet 1: Quote Summary

Sections:

1. Input metadata (quote id, formula version, user, timestamp).
2. Route (origin, destination, mapped baseline route, distance, ETA).
3. Cost breakdown (freight, bunker, insurance, port fees, waiting, surcharges).
4. Risk-adjusted total and negotiation range.
5. Assumptions and manager-readable explanations.

## Sheet 2: Risk Classifier

Columns:

- Category
- Factor
- Score (1-5 stars)
- Severity index (0-1)
- Weight
- Impact USD
- Manager comment

Mandatory categories:

- Crew safety
- Port conditions
- Weather phenomena
- Arctic/far north specifics
- Seasonality
- Ice risks
- Navigation risks

Weather classifier includes:

- wind
- storm
- fog
- icing
- snow
- rain
- wave height
- visibility
- extreme cold
- polar night
- ice season
- transitional season

## Extensibility

- Named ranges for formulas.
- Data validation lists for risk categories.
- Hidden metadata cells for parser version and checksum.
