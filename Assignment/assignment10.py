'''
Assignment 3: 
Validate Phone Numbers with re.match.
Given a list of phone numbers, print only the ones that match this format: (123) 456-7890
'''

import re

phone_numbers = [
    "(123) 456-7890",
    "123-456-7890",
    "(987) 654-3210",
    "(123 456-7890)"
]

pattern = r"^\(\d{3}\) \d{3}-\d{4}$"

for number in phone_numbers:
    if re.match(pattern, number):
        print(number)

