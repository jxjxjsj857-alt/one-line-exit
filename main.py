#!/usr/bin/env python3
"""The One-Line Exit: write one funny one-line resignation letter to /output/entry.txt."""
import os

LINE = "Please accept this as my resignation: after three years of hearing 'we're a family here,' I have decided to get emancipated."

def main():
    line = LINE.strip()
    assert 1 <= len(line) <= 140, f"entry must be 1-140 characters, got {len(line)}"
    assert "\n" not in line, "entry must be exactly one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)

if __name__ == "__main__":
    main()
