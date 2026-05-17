from __future__ import annotations

from datetime import UTC, datetime
from uuid import uuid4

from sqlalchemy import JSON, DateTime, Float, ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class QuoteRequestEntity(Base):
    __tablename__ = "quote_request"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid4()))
    tenant_id: Mapped[str] = mapped_column(String(128), nullable=False)
    created_by: Mapped[str] = mapped_column(String(128), nullable=False, default="system")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(UTC)
    )
    origin_port_code: Mapped[str] = mapped_column(String(16), nullable=False)
    destination_port_code: Mapped[str] = mapped_column(String(16), nullable=False)
    vessel_type: Mapped[str] = mapped_column(String(64), nullable=False)
    formula_version: Mapped[str] = mapped_column(String(64), nullable=False)
    input_payload: Mapped[dict] = mapped_column(JSON, nullable=False)


class QuoteResultEntity(Base):
    __tablename__ = "quote_result"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid4()))
    request_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("quote_request.id", ondelete="CASCADE"), nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(UTC)
    )
    currency: Mapped[str] = mapped_column(String(8), nullable=False, default="USD")
    total_price: Mapped[float] = mapped_column(Float, nullable=False)
    negotiate_min: Mapped[float] = mapped_column(Float, nullable=False)
    negotiate_max: Mapped[float] = mapped_column(Float, nullable=False)
    result_payload: Mapped[dict] = mapped_column(JSON, nullable=False)


class QuoteAuditEventEntity(Base):
    __tablename__ = "quote_audit_event"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid4()))
    request_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("quote_request.id", ondelete="CASCADE"), nullable=False
    )
    event_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(UTC)
    )
    actor_type: Mapped[str] = mapped_column(String(32), nullable=False, default="user")
    actor_id: Mapped[str] = mapped_column(String(128), nullable=False, default="unknown")
    event_type: Mapped[str] = mapped_column(String(64), nullable=False)
    event_payload: Mapped[dict] = mapped_column(JSON, nullable=False)


class ExcelDocumentEntity(Base):
    __tablename__ = "excel_document"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid4()))
    request_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("quote_request.id", ondelete="CASCADE"), nullable=False
    )
    blob_path: Mapped[str] = mapped_column(String(512), nullable=False)
    checksum_sha256: Mapped[str] = mapped_column(String(128), nullable=False)
    access_scope: Mapped[str] = mapped_column(String(64), nullable=False, default="tenant")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(UTC)
    )

