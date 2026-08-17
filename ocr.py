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


def join_words(items, separator=" "):
    """Join OCR word items into a single string using each item's `text`."""
    return separator.join(str(it.get("text", "")) for it in items)


def clamp_confidence(value, low=0.0, high=100.0):
    """Clamp an OCR confidence score into the [low, high] range."""
    return max(low, min(high, float(value)))
