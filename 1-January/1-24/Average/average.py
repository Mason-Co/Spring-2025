# Programmer: Mason C
# Date: 1-January
# Program: Average

# Set variables
HIGH_SCORE = 95
average = 0
# Getting user input for test scores through a loop
for i in range(0,3):
    test_score = int(input(f"What was the score of test {i+1}?"))
    average += test_score
# Calculate average after the scores have been added
average = average/3

# Display average
print(f"The average test score is {average:.1f}.")

# Display data with if statements
if average >= HIGH_SCORE:
    print("Congratulations, you have a great average!")
else:
    print(f"Sorry, try studying a little more.")