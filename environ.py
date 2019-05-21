"""
environ.py

Print the environment variables received by the Python script.
"""

import sys
import os   #operating system

for key, value in os.environ.items():   #os.environ is a dictionary.
    print(f"{key}={value}")

sys.exit(0)
