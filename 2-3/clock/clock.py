# Programmer: Mason Colacicco
# Date: February
# Program: Clock

# Importing
from time import *

# Ask for time
minutes = int(input("How many minutes should be calculated (1-3)? "))

# Loop for printing
for i in range(0,minutes):
    for x in range(0,60):
        print(f"\rMinutes: {i} Seconds: {x}", end="")
        sleep(.1)

    if i == (minutes-1):
        x = 0
        print(f"\rMinutes: {minutes} Seconds: {x}", end="")