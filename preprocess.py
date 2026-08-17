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


def median_filter(values, window=3):
    """Apply a moving-median filter to suppress salt-and-pepper noise."""
    if window % 2 == 0:
        window += 1
    half = window // 2
    out = []
    for i in range(len(values)):
        lo, hi = max(0, i - half), min(len(values), i + half + 1)
        window_vals = values[lo:hi]
        out.append(sorted(window_vals)[len(window_vals) // 2])
    return out


def contrast_stretch(values, low=0, high=255):
    """Linearly stretch `values` to fill the [low, high] intensity range."""
    if not values:
        return []
    mn, mx = min(values), max(values)
    if mx == mn:
        return [int((low + high) / 2)] * len(values)
    span = mx - mn
    return [int(low + (v - mn) * (high - low) / span) for v in values]
