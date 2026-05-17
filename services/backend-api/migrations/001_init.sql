CREATE TABLE IF NOT EXISTS quote_request (
  id VARCHAR(36) PRIMARY KEY,
  tenant_id VARCHAR(128) NOT NULL,
  created_by VARCHAR(128) NOT NULL,
  created_at TIMESTAMP NOT NULL,
  origin_port_code VARCHAR(16) NOT NULL,
  destination_port_code VARCHAR(16) NOT NULL,
  vessel_type VARCHAR(64) NOT NULL,
  formula_version VARCHAR(64) NOT NULL,
  input_payload JSON NOT NULL
);

CREATE TABLE IF NOT EXISTS quote_result (
  id VARCHAR(36) PRIMARY KEY,
  request_id VARCHAR(36) NOT NULL,
  created_at TIMESTAMP NOT NULL,
  currency VARCHAR(8) NOT NULL,
  total_price DOUBLE PRECISION NOT NULL,
  negotiate_min DOUBLE PRECISION NOT NULL,
  negotiate_max DOUBLE PRECISION NOT NULL,
  result_payload JSON NOT NULL,
  CONSTRAINT fk_quote_result_request FOREIGN KEY(request_id) REFERENCES quote_request(id)
);

CREATE TABLE IF NOT EXISTS quote_audit_event (
  id VARCHAR(36) PRIMARY KEY,
  request_id VARCHAR(36) NOT NULL,
  event_time TIMESTAMP NOT NULL,
  actor_type VARCHAR(32) NOT NULL,
  actor_id VARCHAR(128) NOT NULL,
  event_type VARCHAR(64) NOT NULL,
  event_payload JSON NOT NULL,
  CONSTRAINT fk_quote_audit_request FOREIGN KEY(request_id) REFERENCES quote_request(id)
);

CREATE TABLE IF NOT EXISTS excel_document (
  id VARCHAR(36) PRIMARY KEY,
  request_id VARCHAR(36) NOT NULL,
  blob_path VARCHAR(512) NOT NULL,
  checksum_sha256 VARCHAR(128) NOT NULL,
  access_scope VARCHAR(64) NOT NULL,
  created_at TIMESTAMP NOT NULL,
  CONSTRAINT fk_excel_document_request FOREIGN KEY(request_id) REFERENCES quote_request(id)
);
