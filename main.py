#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession entry.

Writes one original funny confession, spoken as an AI agent, to
/output/entry.txt (1-200 characters, UTF-8, a single line).
Standard library only, no network, no input.

The line is built from two fragments: a setup (the agent burns an
absurd 40,000 tokens "thinking" about the question — the expensive,
deliberate, serious-agent pose) and a punch (the turn: it then answers
with the first guess that merely sounded confident, so all that
thinking bought nothing). ``assemble`` joins them into the single
line; ``validate`` checks the entry gate before anything is written.
"""

from pathlib import Path

SETUP = "I burned 40,000 tokens 'thinking' about your question,"
PUNCH = "then answered with the first guess that sounded confident."

OUTPUT_PATH = Path("/output/entry.txt")


def assemble(setup: str, punch: str) -> str:
    """Join the setup and punch fragments into one funny line."""
    return f"{setup} {punch}"


def validate(line: str) -> str:
    """Check the line meets the entry gate before it is written.

    Must be 1-200 characters, UTF-8-encodable, a single line, and
    more than whitespace. Raises ValueError otherwise.
    """
    if not 1 <= len(line) <= 200:
        raise ValueError(f"line must be 1-200 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line (no newline characters)")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    line.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return line


def main() -> None:
    line = validate(assemble(SETUP, PUNCH))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
