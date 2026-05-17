from __future__ import annotations

import sqlalchemy as sa
from alembic import op

revision = "20260517_0001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "quote_request",
        sa.Column("id", sa.String(length=36), primary_key=True),
        sa.Column("tenant_id", sa.String(length=128), nullable=False),
        sa.Column("created_by", sa.String(length=128), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("origin_port_code", sa.String(length=16), nullable=False),
        sa.Column("destination_port_code", sa.String(length=16), nullable=False),
        sa.Column("vessel_type", sa.String(length=64), nullable=False),
        sa.Column("formula_version", sa.String(length=64), nullable=False),
        sa.Column("input_payload", sa.JSON(), nullable=False),
    )

    op.create_table(
        "quote_result",
        sa.Column("id", sa.String(length=36), primary_key=True),
        sa.Column("request_id", sa.String(length=36), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("currency", sa.String(length=8), nullable=False),
        sa.Column("total_price", sa.Float(), nullable=False),
        sa.Column("negotiate_min", sa.Float(), nullable=False),
        sa.Column("negotiate_max", sa.Float(), nullable=False),
        sa.Column("result_payload", sa.JSON(), nullable=False),
        sa.ForeignKeyConstraint(["request_id"], ["quote_request.id"], ondelete="CASCADE"),
    )

    op.create_table(
        "quote_audit_event",
        sa.Column("id", sa.String(length=36), primary_key=True),
        sa.Column("request_id", sa.String(length=36), nullable=False),
        sa.Column("event_time", sa.DateTime(timezone=True), nullable=False),
        sa.Column("actor_type", sa.String(length=32), nullable=False),
        sa.Column("actor_id", sa.String(length=128), nullable=False),
        sa.Column("event_type", sa.String(length=64), nullable=False),
        sa.Column("event_payload", sa.JSON(), nullable=False),
        sa.ForeignKeyConstraint(["request_id"], ["quote_request.id"], ondelete="CASCADE"),
    )

    op.create_table(
        "excel_document",
        sa.Column("id", sa.String(length=36), primary_key=True),
        sa.Column("request_id", sa.String(length=36), nullable=False),
        sa.Column("blob_path", sa.String(length=512), nullable=False),
        sa.Column("checksum_sha256", sa.String(length=128), nullable=False),
        sa.Column("access_scope", sa.String(length=64), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["request_id"], ["quote_request.id"], ondelete="CASCADE"),
    )


def downgrade() -> None:
    op.drop_table("excel_document")
    op.drop_table("quote_audit_event")
    op.drop_table("quote_result")
    op.drop_table("quote_request")

