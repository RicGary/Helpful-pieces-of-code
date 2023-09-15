"""
Code to easy setup the environment, creates a dir for the data, updates pip and install dependencies.
"""

import os
import sys
import platform

def setup_dir():
    """Simple function to setup the enviroment."""
    files = os.listdir()
    python_version = platform.python_version()

    if "data" not in files:
        os.mkdir("data")
        
        try:
            os.system("python -m venv venv")
            os.system("python.exe -m pip install --upgrade pip")
            os.system("pip install -r requirements.txt")
        except:
            os.system("python3 -m venv venv")
            os.system("python.exe -m pip install --upgrade pip")
            os.system("pip3 install -r requirements.txt")

        if python_version[0] != "3":
            print("Please consider using Python 3!")
            print("https://www.python.org/downloads/", "\n")


if __name__ == "__main__":
    setup_dir()