from __future__ import annotations

import hashlib
from typing import Any

from sqlalchemy import select
from sqlalchemy.orm import Session

from ..entities import (
    ExcelDocumentEntity,
    QuoteAuditEventEntity,
    QuoteRequestEntity,
    QuoteResultEntity,
)


class QuoteRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def save_quote(self, payload: dict[str, Any], result: dict[str, Any]) -> dict[str, Any]:
        request = QuoteRequestEntity(
            tenant_id=payload["tenant_id"],
            origin_port_code=payload["origin_port_code"],
            destination_port_code=payload["destination_port_code"],
            vessel_type=payload["vessel_type"],
            formula_version=result["formula_version"],
            input_payload=payload,
        )
        self.session.add(request)
        self.session.flush()

        stored = {
            "quote_id": request.id,
            "tenant_id": payload["tenant_id"],
            "origin_port_code": payload["origin_port_code"],
            "destination_port_code": payload["destination_port_code"],
            **result,
        }

        quote_result = QuoteResultEntity(
            request_id=request.id,
            currency="USD",
            total_price=result["total_price_usd"],
            negotiate_min=result["negotiation_min_usd"],
            negotiate_max=result["negotiation_max_usd"],
            result_payload=stored,
        )
        self.session.add(quote_result)

        self.session.add(
            QuoteAuditEventEntity(
                request_id=request.id,
                event_type="quote.calculated",
                event_payload={
                    "formula_version": result["formula_version"],
                    "distance_nm": result["distance_nm"],
                    "risk_score": result["risk_score"],
                },
            )
        )
        self.session.flush()
        return stored

    def get_quote(self, quote_id: str) -> dict[str, Any] | None:
        stmt = (
            select(QuoteResultEntity.result_payload)
            .join(QuoteRequestEntity, QuoteRequestEntity.id == QuoteResultEntity.request_id)
            .where(QuoteRequestEntity.id == quote_id)
        )
        row = self.session.execute(stmt).first()
        return row[0] if row else None

    def save_excel_document(self, quote_id: str, excel_bytes: bytes) -> dict[str, Any]:
        checksum = hashlib.sha256(excel_bytes).hexdigest()
        document = ExcelDocumentEntity(
            request_id=quote_id,
            blob_path=f"local://excel/{quote_id}.xlsx",
            checksum_sha256=checksum,
            access_scope="tenant",
        )
        self.session.add(document)
        self.session.add(
            QuoteAuditEventEntity(
                request_id=quote_id,
                event_type="quote.export.generated",
                event_payload={"blob_path": document.blob_path, "checksum": checksum},
            )
        )
        self.session.flush()
        return {"blob_path": document.blob_path, "checksum": checksum}

