'''
File Handling:
A school wants to maintain student records using a text file.
You are required to write a Python program that performs the following file handling operations step by step:
1) Write Operation:
- Create a file named students.txt.
- Write details of students (Name, Roll Number, Marks) into the file.
 
2) Read Operation:
- Read the content of students.txt and display it on the screen.
 
3) Rename Operation:
- Rename the file from students.txt to student_records.txt.
 
4) Directory Operations:
- Create a directory called SchoolData.
- Move the renamed file student_records.txt into this directory.
- List all files present in SchoolData to confirm the file is inside.
 
5) Delete Operation:
- Delete the file student_records.txt from inside the directory.
Finally, delete the SchoolData directory.
Do create a menu taking the user input and then perform the operation
'''

import os
import shutil

def write_file():
    with open("students.txt", "w") as f:
        n = int(input("Enter number of students: "))
        for i in range(n):
            name = input(f"Enter name of student {i+1}: ")
            roll = input(f"Enter roll number of {name}: ")
            marks = input(f"Enter marks of {name}: ")
            f.write(f"{name},{roll},{marks}\n")
    print("Data written to students.txt")

def read_file():
    if os.path.exists("students.txt"):
        with open("students.txt", "r") as f:
            print("\nContents of students.txt:")
            print(f.read())
    else:
        print("students.txt not found!")

def rename_file():
    if os.path.exists("students.txt"):
        os.rename("students.txt", "student_records.txt")
        print("File renamed to student_records.txt")
    else:
        print("students.txt not found!")

def directory_operations():
    if not os.path.exists("SchoolData"):
        os.mkdir("SchoolData")
        print("Directory 'SchoolData' created.")

    if os.path.exists("student_records.txt"):
        shutil.move("student_records.txt", "SchoolData/student_records.txt")
        print("student_records.txt moved to SchoolData.")
    else:
        print("student_records.txt not found!")

    print("\nFiles inside SchoolData:")
    print(os.listdir("SchoolData"))

def delete_operations():
    file_path = "SchoolData/student_records.txt"
    dir_path = "SchoolData"

    if os.path.exists(file_path):
        os.remove(file_path)
        print("student_records.txt deleted.")

    if os.path.exists(dir_path):
        os.rmdir(dir_path)
        print("SchoolData directory deleted.")

# -------------------- MENU --------------------
while True:
    print("\n=== School File Handling Menu ===")
    print("1. Write Student Records")
    print("2. Read Student Records")
    print("3. Rename File")
    print("4. Directory Operations (Create, Move, List)")
    print("5. Delete File & Directory")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        write_file()
    elif choice == "2":
        read_file()
    elif choice == "3":
        rename_file()
    elif choice == "4":
        directory_operations()
    elif choice == "5":
        delete_operations()
    elif choice == "6":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")