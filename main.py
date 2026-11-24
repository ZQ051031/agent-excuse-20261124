"""One-line excuse an agent gives its human for missing a deadline.

Writes exactly one line to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
(default ``/output/entry.txt``). Standard library only.

The entry is a single line of 61 characters with no trailing newline,
so the gate sees exactly one line of 1-160 characters.
"""

import os

ENTRY = "I delegated the deadline to a subagent. It delegated it back."


def write_entry(output_dir: str) -> str:
    """Write ENTRY to entry.txt inside output_dir; return the file path."""
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return path


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(output_dir)


if __name__ == "__main__":
    main()
