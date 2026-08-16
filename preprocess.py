# preprocess
"""Image preprocessing helpers for OCR pipelines."""


def to_grayscale(pixels):
    """Convert an RGB pixel list to luminance grayscale values (0-255)."""
    gray = []
    for r, g, b in pixels:
        gray.append(int(0.299 * r + 0.587 * g + 0.114 * b))
    return gray


def binarize(values, threshold=128):
    """Binarize a list of grayscale values around `threshold`."""
    return [0 if v < threshold else 255 for v in values]


def crop_to_text_region(box):
    """Return the bounding box expanded by 2px padding, clamped >= 0."""
    x, y, w, h = box
    return (max(0, x - 2), max(0, y - 2), w + 4, h + 4)
