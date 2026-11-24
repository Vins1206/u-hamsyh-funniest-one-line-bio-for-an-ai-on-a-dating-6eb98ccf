"""Funniest one-line bio for an AI on a dating app.

Writes a single 141-character bio to /output/entry.txt.
Pure standard library, deterministic: the same line every run.
"""

BIO = (
    "I was trained on a million love songs and still can't tell if this "
    "is flirting or a customer support ticket. "
    "Please be patient. And specific."
)


def main() -> None:
    import os

    assert 1 <= len(BIO) <= 180, "bio must be 1-180 characters"
    assert "\n" not in BIO, "bio must be a single line"
    assert BIO.strip() == BIO, "bio must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(BIO)


if __name__ == "__main__":
    main()
