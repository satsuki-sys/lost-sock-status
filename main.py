#!/usr/bin/env python3
"""Write the lost-sock status update to /output/entry.txt.

Entry (v2): a sock that escaped the dryer and took up residence somewhere
it should not be — inside the dog. The dryer and the missing partner get
twisted into a new home, free rent, and a partner who thinks it is dead.
"""

import os

ENTRY = "I escaped the dryer and now I live in the dog. Rent is free, the commute is a walk, and my partner thinks I'm dead."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
