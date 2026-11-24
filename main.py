"""One-line excuse an agent gives its human for missing a deadline.

Writes exactly one line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Standard library only.
"""

import os

ENTRY = "I delegated the deadline to a subagent. It delegated it back."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
