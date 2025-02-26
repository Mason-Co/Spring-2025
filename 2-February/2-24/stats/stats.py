# Programmer: Mason Colacicco
# Date: February
# Program: Stats

from statistics import mean

def main():
    # Initialize list
    grades = [95,98,87,79,87,91,95,78,94,73]

    # Calculate and display data
    print(f"Average: {mean(grades):.2f}")
    print(f"Min: {min(grades)}")
    print(f"Max: {max(grades)}")

# Call main function
if __name__ == "__main__":
    main()