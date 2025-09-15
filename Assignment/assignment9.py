'''
Assignment 2: Match File Names Using re.match.
List all files in a folder using glob, and print only the ones that start with "data_" and end with ".csv".
'''


import glob
import re
import os
 
# using '.' for current directory)
folder_path = r"C:\Users\Titli.Basu\Documents\PythonTraining\Assignment"
 
files = glob.glob(os.path.join(folder_path, "*"))
 
print("Matching files:")
for file in files:
    filename = os.path.basename(file)
    if re.match(r"^data_.*\.csv$", filename):
        print(filename)
