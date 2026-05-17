select
  toDate(created_at) as quote_date,
  tenant_id,
  count(*) as quote_count,
  avg(total_price_usd) as avg_total_price_usd,
  avg(risk_score) as avg_risk_score
from {{ source('oltp', 'quote_result_flat') }}
group by quote_date, tenant_id
