# Programmer: Mason C
# Date: January
# Program: Average2

average = 0
# Getting user input for test scores through a loop
for i in range(0,3):
    test_score = int(input(f"What was the score of test {i+1}?"))
    average += test_score
# Calculate average after the scores have been added
average = average/3

# Find and print letter grade
if average >= 90:
    print(f"Your got an A with an average of {average:.1f}!")
elif average >= 80:
    print(f"Your got a B with an average of {average:.1f}!")
elif average >= 70:
    print(f"Your got a C with an average of {average:.1f}.")
elif average >= 60:
    print(f"Your got a D with an average of {average:.1f}.")
else:
    print(f"You got an F with an average of {average:.1f}. Speak with me after class.")