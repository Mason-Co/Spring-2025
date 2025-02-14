# Programmer: Mason Colacicco
# Date: 1-January
# Program: Hot Dog Cookout Calculator

# Import rounding to the ceiling
from math import ceil

# Collect data on attendees
people = int(input("How many people are attending? "))
hot_dogs = int(input("How many hot dogs does each person get? "))
# Calculate number of hot dogs needed
num = people * hot_dogs

# Calculate hot dog material requirements
buns = ceil(num/8)
dogs = ceil(num/10)
# Calculate remainders
buns_r = num % 8
dogs_r = num % 10
# Use remainder to calculate leftovers
if buns_r != 0:
    buns_r = 8-buns_r
if dogs_r != 0:
    dogs_r = 10-dogs_r
# Display data
print(f"{buns} hot dog bun packages are required with {buns_r} buns left over.")
print(f"{dogs} hot dog packages are required with {dogs_r} hot dogs left over.")