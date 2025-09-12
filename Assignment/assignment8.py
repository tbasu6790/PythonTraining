'''Assignment 1 : List all .txt Files and Check for a Word using glob + re.search 
Write a script to: 
- Find all .txt files in a folder. 
- Check if any file contains the word "Python". 
- Print the file name if the word is found.'''

import glob
import re

txt_files = glob.glob(r"C:\Users\Titli.Basu\Documents\PythonTraining\Assignment\note.txt")

for file in txt_files:
    with open(file, "r") as f:
        content = f.read()
        if re.search(r"\bPython\b", content):
            print(f"Found 'Python' in: {file}")

