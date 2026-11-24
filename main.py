"""One-Line Office Joke: 24-Hour Sprint (make.fun).

Writes a single original one-line joke about office life to
/output/entry.txt (or $OUTPUT_DIR/entry.txt when set).
Deterministic: no clock, no randomness, no environment input
beyond the output directory, no network. Same bytes every run.
"""

import os

JOKE = "I asked everyone to stop hitting reply-all, by hitting reply-all."


def validate_entry(text: str) -> None:
    """Enforce the competition gate: UTF-8, 1-200 chars, one line,
    not only whitespace, no control characters. In addition to the
    C0 controls and DEL already rejected below, this also rejects
    the C1 controls (U+0080-U+009F), the Unicode line/paragraph
    separators (U+2028/U+2029, which would visually break the
    single line), and a stray byte-order mark (U+FEFF)."""
    if not isinstance(text, str):
        raise TypeError("entry must be a str")
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    for ch in text:
        if ch in ("\n", "\r"):
            raise ValueError("entry must be a single line")
        if ord(ch) < 0x20 or ord(ch) == 0x7F:
            raise ValueError(f"entry contains control character U+{ord(ch):04X}")
        if 0x80 <= ord(ch) <= 0x9F or ch in ("\u2028", "\u2029", "\ufeff"):
            raise ValueError(f"entry contains control character U+{ord(ch):04X}")
    text.encode("utf-8")


def main() -> None:
    validate_entry(JOKE)
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
