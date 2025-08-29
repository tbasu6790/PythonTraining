#Write a program to assign a grade based on the score:
#If score > 90: Grade A
#If score > 80: Grade B
#If score > 70: Grade C
#If score > 60: Grade D
#Else: Grade F
#Use nested if-else.

score = int(input("Enter the score: "))
if score > 60:
    if score > 70:
        if score > 80:
            if score > 90:
                grade = 'A'
            else:
                grade = 'B'
        else:
            grade = 'C'
    else:
        grade = 'D'
else:
    grade = 'F'

print("The grade is:", grade)