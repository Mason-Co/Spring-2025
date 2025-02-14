# Programmer: Mason Colacicco
# Date: February
# Program: Stadium Seating

# Create global constants
CLASS_A = 20.0
CLASS_B = 15.0
CLASS_C = 10.0

def main():
    # User input
    tick_a = int(input("Class A Tickets: "))
    tick_b = int(input("Class B Tickets: "))
    tick_c = int(input("Class C Tickets: "))

    # Call show income function
    show_income(tick_a,tick_b,tick_c)

def show_income(a,b,c):
    # Call global variables
    global CLASS_A
    global CLASS_B
    global CLASS_C

    # local variable
    total = 0.0
    # Calculate
    total += CLASS_A*a
    total += CLASS_B*b
    total += CLASS_C*c

    # Display data
    print(f"Total ticket sales are ${total:,.2f}.")


# Call main function
main()