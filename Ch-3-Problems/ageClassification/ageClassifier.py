# Programmer: Mason Colacicco
# Date: January
# Program: Age Classifier

# User input to determine age
age = int(input("What is your age? "))

# if-elif-else statements to determine classification
if age >= 20:
    classification = "adult"
elif age >= 13:
    classification = "teenager"
elif age > 1:
    classification = "child"
else:
    classification = "infant"

# Display data
print(f"At {age} you are a(n) {classification}!")