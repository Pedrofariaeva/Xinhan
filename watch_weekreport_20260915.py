#!/usr/bin/env python3
"""Watch the week-report txt source and rebuild .docx/.pdf on every save.

Usage:  python3 watch_weekreport_20260915.py
Stop:   Ctrl-C
"""

import subprocess
import time
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "uncoveredDocs" / "V20260915" / "weekReport_20260915_content.txt"
BUILD = ROOT / "generate_weekreport_20260915.py"


def build():
    r = subprocess.run(["python3", str(BUILD)], capture_output=True, text=True)
    if r.returncode == 0:
        print(f"[{time.strftime('%H:%M:%S')}] rebuilt docx + pdf")
    else:
        print(f"[{time.strftime('%H:%M:%S')}] BUILD FAILED:\n{r.stderr}")


def main():
    print(f"Watching {SRC}\nEdit and save the txt — the documents rebuild automatically. Ctrl-C to stop.")
    build()
    last = SRC.stat().st_mtime
    while True:
        time.sleep(2)
        mtime = SRC.stat().st_mtime
        if mtime != last:
            last = mtime
            time.sleep(1)  # let the editor finish writing
            build()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("watcher stopped")
