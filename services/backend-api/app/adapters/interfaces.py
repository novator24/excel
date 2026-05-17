from __future__ import annotations

from typing import Protocol


class AcquisitionAdapter(Protocol):
    def fetch(self, **kwargs) -> dict:
        """Acquire raw provider payload."""


class NormalizationAdapter(Protocol):
    def normalize(self, payload: dict) -> dict:
        """Convert raw provider payload to canonical internal schema."""


class ProviderAdapter(Protocol):
    name: str

    def acquire(self, **kwargs) -> dict:
        """Acquire raw payload from external provider."""

    def normalize(self, payload: dict) -> dict:
        """Normalize external schema for calculation layer."""
