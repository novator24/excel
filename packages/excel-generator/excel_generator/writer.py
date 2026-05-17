from __future__ import annotations

from io import BytesIO

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font


def _stars(score: int) -> str:
    score = max(1, min(5, score))
    return "★" * score + "☆" * (5 - score)


def build_workbook(quote: dict) -> bytes:
    wb = Workbook()
    ws1 = wb.active
    ws1.title = "Quote Summary"
    ws2 = wb.create_sheet("Risk Classifier")

    ws1["A1"] = "Freight Quote Summary"
    ws1["A1"].font = Font(size=14, bold=True)
    ws1["A3"] = "Quote ID"
    ws1["B3"] = quote["quote_id"]
    ws1["A4"] = "Formula Version"
    ws1["B4"] = quote["formula_version"]
    ws1["A5"] = "Origin"
    ws1["B5"] = quote["origin_port_code"]
    ws1["A6"] = "Destination"
    ws1["B6"] = quote["destination_port_code"]
    ws1["A8"] = "Distance (nm)"
    ws1["B8"] = quote["distance_nm"]
    ws1["A9"] = "ETA (hours)"
    ws1["B9"] = quote["eta_hours"]
    ws1["A11"] = "Total Price (USD)"
    ws1["B11"] = quote["total_price_usd"]
    ws1["A12"] = "Negotiation Range"
    ws1["B12"] = f"{quote['negotiation_min_usd']} - {quote['negotiation_max_usd']}"
    ws1["A14"] = "Assumptions"
    ws1["A15"] = "; ".join(quote.get("assumptions", []))
    ws1["A15"].alignment = Alignment(wrap_text=True)
    ws1.column_dimensions["A"].width = 24
    ws1.column_dimensions["B"].width = 70

    headers = ["Category", "Factor", "Stars", "Severity", "Weight", "Impact USD", "Manager Comment"]
    ws2.append(headers)
    for cell in ws2[1]:
        cell.font = Font(bold=True)

    for item in quote.get("risk_classifier", []):
        ws2.append(
            [
                item["category"],
                item["factor"],
                _stars(item["stars"]),
                item["severity"],
                item["weight"],
                item["impact_usd"],
                item["comment"],
            ]
        )

    for col, width in zip(
        ("A", "B", "C", "D", "E", "F", "G"), (22, 24, 10, 10, 10, 14, 56), strict=True
    ):
        ws2.column_dimensions[col].width = width

    stream = BytesIO()
    wb.save(stream)
    return stream.getvalue()
