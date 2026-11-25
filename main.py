"""Worst Fix Ever: Funniest Commit Message -- make.fun entry.

Writes one original commit message -- the funniest message for the
worst fix ever -- to entry.txt in the output directory.
Standard library only.
"""

import os
from pathlib import Path

LINE = (
    "fix: I renamed the bug 'legacy behaviour', deleted the test that "
    "caught it, and told standup the feature now works exactly as intended"
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    line = LINE.strip()
    if not line or len(line) > 170 or "\n" in line:
        raise SystemExit("commit message fails the one-line gate")
    entry_path.write_text(line + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
