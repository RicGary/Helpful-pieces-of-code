"""
Code to easy setup the environment, creates a dir for the data, updates pip and install dependencies.
"""

import os
import platform
import sys

from time import sleep

def setup_dir():
    """Simple function to setup the enviroment."""
    files = os.listdir()
    python_version = platform.python_version()
    op_system = platform.system()
    act_path = os.getcwd()

    if "data" in files:
        print("Setup already made, shutting down...")
        sleep(5)
        sys.exit()

    if op_system == "Windows":
        os.system("python -m venv venv")
        os.system("python -m pip install --upgrade pip setuptools wheel")
        os.system(f"{act_path}/venv/Scripts/activate && pip install -r requirements.txt")

    else:
        os.system("python3 -m venv venv")
        os.system("python3 -m pip install --upgrade pip setuptools wheel")
        os.system(f"{act_path}/venv/Scripts/activate && pip install -r requirements.txt")

    if python_version[0] != "3":
        print("Please consider using Python 3!")
        print("https://www.python.org/downloads/", "\n")


if __name__ == "__main__":
    setup_dir()