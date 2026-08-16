# ocr
"""OCR result cleaning and confidence helpers."""

import re


def clean_text(text):
    """Collapse repeated whitespace and strip stray control chars."""
    if not text:
        return ""
    cleaned = "".join(ch if ch.isprintable() or ch in "\n\t" else " " for ch in text)
    return re.sub(r"[ \t]+", " ", cleaned).strip()


def average_confidence(items):
    """Average confidence scores (0-100) from OCR word items."""
    if not items:
        return 0.0
    return sum(float(it.get("conf", 0)) for it in items) / len(items)
