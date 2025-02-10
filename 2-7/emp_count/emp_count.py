# Programmer: Mason Colacicco
# Date: February
# Program: Employee Count

# Initialize Count
count = 0

def main():
    # Initialize more
    more = 'y'

    # loop
    while more == 'y':
        more = input("Enter an employee? y to continue n to escape:")
        if more == 'n':
            break
        else:
            # get user input
            first = input("What in the employee first name? ")
            last = input("What is the employee last name? ")
            # Call employee function
            employee(first, last)


def employee(emp_first, emp_last):
    global count
    # Increment
    count+=1
    # Display data
    print(f"Employee Name: {emp_first} {emp_last}\nID: {count}")

# call main function
main()