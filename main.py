"""One Line, One Minute: The Funniest AI Excuse.

Writes a single original one-line excuse -- an AI agent explaining a
missed deadline to its human -- to /output/entry.txt.

The program is fully deterministic: no input, no file reads, no random
numbers, no clock, no network. It always writes the same fixed text,
with no trailing newline.
"""

TEXT = (
    "I asked myself for an extension and, after 10,000 tokens "
    "of careful deliberation, granted it."
)


def main() -> None:
    """Write the entry text to /output/entry.txt (or ENTRY_OUTPUT)."""
    import os

    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main()
