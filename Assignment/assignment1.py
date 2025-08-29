#Write a Python program that manages a list of student scores. Perform the following operations step-by-step:
#Create an empty list to store scores.
#Append the scores: 85, 90, 78, 92, 88
#Insert the score 80 at index 
#Remove the score 92 from the list
#Sort the scores in ascending order
#Reverse the list
#Find and print the maximum and minimum score
#Check if 90 is in the list
#Print the total number of scores
#Slice and print the first three scores
#Iterate through the list and print each score
#find the last element from the list
#replace the score with new score on the index 2
#create a new copied list also


scores = [85, 90, 78, 92, 88]
print("Initial Scores List: ", scores)

scores.insert(2, 80) #inserting 80 at index 2
print("Scores List after inserting 80 at index 2: ", scores)

scores.remove(92)
print("Scores List after removing 92: ", scores)

scores.sort()
print("Scores List after sorting in ascending order: ", scores)

scores.reverse()
print("Scores List after reversing: ", scores)

max_score = max(scores)
min_score = min(scores)
print("Maximum Score: ", max_score)
print("Minimum Score: ", min_score)

is_ninety_present = 90 in scores
print("Is 90 present in the list? ", is_ninety_present)#returns boolean value

total_scores = len(scores)
print("Total number of scores: ", total_scores)

first_three_scores = scores[:3] #slicing the first three scores
print("First three scores: ", first_three_scores)

print("Iterating through the list and printing each score:")
for score in scores:
    print(score)

last_element = scores[-1]
print("Last element in the list: ", last_element)

scores[2] = 95
print("Scores List after replacing the score at index 2 with 95: ", scores)

copied_scores = scores.copy()
print("Copied Scores List: ", copied_scores)

