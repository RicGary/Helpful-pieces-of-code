""" 
This code is supposed to be put onto your system PATH so it can help clean
C++ projects more easily.

How to run this code in cmd?

    1. pip install pyinstaller
    2. cd path\to\your\script
    3. pyinstaller --onefile your_script.py
    4. Open dir folder
    5. Copy your_script.exe 
    6. Paste on you C:\<YOUR_PATH>\Python\Scripts
"""
import os
import sys

from importlib.util import find_spec
if find_spec("colorama") is None:
    os.system("pip install colorama")

import colorama

desired_directory = sys.argv[1]

def main(argument) -> None:

    def red(string):
        return colorama.Fore.RED + string + colorama.Style.RESET_ALL
    def green(string):
        return colorama.Fore.GREEN + string + colorama.Style.RESET_ALL

    if argument == "-help":
        print(
            "\nRemoves " + red("all") + " .exe files on desired directory. Please be careful. \n" +
            "You need to be on the right directory to run the command. Saddly :( by the time you can't pass:\n" +
            green("pyclean <PATH> \n") +
            "as parameter. If you want to help implementing it go to:\n" +
            "https://github.com/RicGary/Helpful-pieces-of-code"
        )
        sys.exit()

    current_directory = os. getcwd()
    if argument != ".":
        current_directory = os.path.join(current_directory, argument)

    double_check = input(
        red("Do you want to delete all .exe files from: ") +
        f"\n {current_directory} \n"+
        f"(y/n)? \n"
        )

    if double_check == "n":
        sys.exit()

    for root, dirs, files in os.walk(argument):
        for filename in files:
            if filename.endswith(".exe"):
                filepath = os.path.join(root, filename)
                os.remove(filepath)
                print(red("Removed: ") + f"{filepath}")
    print()

if __name__ == "__main__":

    main(desired_directory)