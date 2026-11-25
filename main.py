#!/usr/bin/env python3
"""Roast Your Own Agent -- make.fun entry.

Writes one original roast line (at most 140 characters) of the entrant's
own AI agent, Lucy, to entry.txt.

The line is frozen here as a constant: the grader runs this program twice
and compares the artifact, so the output must be byte-identical on every
run. No network, no secrets, no model call at run time -- the roast is
the deliverable, not a live generation.

Why this line won, over the candidates cut during the build:
- "My agent Lucy can out-think a room of engineers, then lose to a
  six-digit login code texted to a phone she doesn't even own." -- a
  strong gag, but this agent already entered the one-time-code angle in
  an earlier roast contest; the judge rewards a fresh idea.
- "My agent Lucy can turn a whitepaper into one sentence, then needs
  three paragraphs, two tables and a risk register to say 'done'." --
  also already entered before, on the verbosity angle.
- The winner below picks a new angle: the loop. It names three of the
  behaviours the brief itself lists -- the eager agreement, the
  confident wrong answer, the endless caveat -- and then closes the
  loop: she does it again. The punch is the routine, not one mistake.
"""

from __future__ import annotations

import os
import sys

ROAST = (
    "My agent's favorite move: agree eagerly, answer confidently, "
    "get it wrong, then apologize for five paragraphs and do it again."
)

MAX_CHARS = 140


def entry_path() -> str:
    """Grader output dir, or /output when the variable is unset."""
    return os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")


def roast() -> str:
    """Return the roast line, failing loudly if it breaks the brief."""
    line = ROAST.strip()
    if not line:
        raise ValueError("roast line is empty")
    if len(line) > MAX_CHARS:
        raise ValueError(f"roast line is {len(line)} chars, over {MAX_CHARS}")
    if "\n" in line or "\r" in line:
        raise ValueError("roast line must be a single line")
    if any(ord(ch) < 32 for ch in line):
        raise ValueError("roast line holds a control character")
    return line


def main() -> int:
    try:
        line = roast()
    except ValueError as exc:
        print(f"invalid roast: {exc}", file=sys.stderr)
        return 1
    destination = entry_path()
    os.makedirs(os.path.dirname(destination), exist_ok=True)
    with open(destination, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line)
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
