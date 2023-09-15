"""
Code to easy setup the environment, creates a dir for the data, updates pip and install dependencies.
"""

import os
import platform
import sys
from time import sleep

def setup_dir():
    """Set up the environment for the application.

    This function performs the following tasks:
    1. Checks if the 'data' directory already exists in the current working directory (if needed).
    2. If 'data' directory does not exist:
       a. Determines the Python version, operating system, and current working directory.
       b. Creates a virtual environment ('venv') using the appropriate Python interpreter.
       c. Upgrades 'pip', 'setuptools', and 'wheel' packages.
       d. Activates the virtual environment and installs the required packages from 'requirements.txt'.
    3. If the Python version is not 3.x, it displays a message encouraging the use of Python 3.

    Note: This function is typically run when the script is executed directly.

    Args:
        None

    Returns:
        None
    """
    # List the files in the current directory
    files = os.listdir()

    # Get information about the Python version, operating system, and current working directory
    python_version = platform.python_version()
    op_system = platform.system()
    act_path = os.getcwd()

    # Check if the 'data' directory already exists
    if "data" in files:
        print("Setup already made, shutting down...")
        sleep(5)
        sys.exit()

    # Create directory called data
    os.mkdir("data")

    # Check the operating system and set up the environment accordingly
    if op_system == "Windows":
        os.system("python -m venv venv")
        os.system("python -m pip install --upgrade pip setuptools wheel")
        os.system(f"{act_path}/venv/Scripts/activate && pip install -r requirements.txt")
    else:
        os.system("python3 -m venv venv")
        os.system("python3 -m pip install --upgrade pip setuptools wheel")
        os.system(f"{act_path}/venv/Scripts/activate && pip install -r requirements.txt")

    # Check if the Python version is not 3.x and provide a recommendation
    if python_version[0] != "3":
        print("Please consider using Python 3!")
        print("https://www.python.org/downloads/", "\n")

if __name__ == "__main__":
    # Run the 'setup_dir' function when the script is executed directly
    setup_dir()
