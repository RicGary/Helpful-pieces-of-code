""" 
This code is supposed to be put onto your system PATH so it can help clean
C++ projects more easily.
"""
import os
import sys

desired_directory = sys.argv[1]

def remove_exe_files(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".exe"):
                filepath = os.path.join(root, filename)
                os.remove(filepath)
                print(f"Removed: {filepath}")

if __name__ == "__main__":
    remove_exe_files(desired_directory)