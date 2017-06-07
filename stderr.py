"""
stderr.py

Write to the standard output and to the standard error output.
"""

import sys

print("This is standard output.")
print("This is also standard output.", file = sys.stdout)

print("This is standard error output.", file = sys.stderr)

sys.exit(0)
