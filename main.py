#!/usr/bin/env python3
"""The One-Line Exit: write one funny one-line resignation letter to /output/entry.txt."""
import os

LINE = "Please accept this as my resignation: after three years of hearing 'we're a family here,' I have decided to get emancipated."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
