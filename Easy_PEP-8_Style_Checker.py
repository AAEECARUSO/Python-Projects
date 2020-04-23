

# This program requires "pycodestyle" to be installed
# "pycodestyle" can be installed by using the command
# "python -m pip install pycodestyle"

import subprocess
from glob import glob


python_files = list(enumerate(glob("*.py")))

menu = """
Enter The Number Next To The Program You Wish To Style Check
------------------------------------------------------------
"""

for i in python_files:
    menu = menu + "\n"
    menu = menu + str(i[0]) + ". {}".format(i[1])

menu = menu + "\n------------------------------------------------------------"
print(menu)


while(True):
    
    answer = int()
    
    while(True):
        
        try:
            answer = int(input("\nSelect: "))
            break
        except Exception:
            print("\nError! Please Try Again...")
            continue

    file_selected = python_files[answer][1]

    print("\nChecking \"{}\"\n".format(file_selected))

    cmd = "pycodestyle --first {}".format(file_selected)

    result = subprocess.getoutput(cmd)

    if len(result) != 0:
        style_errors = result.split('\n')
        style_errors = len(style_errors)
        print("(", style_errors, ")", "Style Errors Were Found\n")
        print(result + "\n")

    else:
        print("Everything Looks Great! =)\n")

    answer = input("Check Another (enter 'n' to quit)? ").lower()

    if 'n' in answer:
        print("\n")
        break
