# This program divides a number by another number.

def main():
    # Get two numbers.
    num1 = int(input('Enter a number: '))

    num2 = int(input('Enter another number: '))

    if type(num1) == int:
        if type(num2) == int:
            # Divide num1 by num2 and display the result.
            num1 = int(num1)
            num2 = int(num2)
            result = num1 / num2
            print(f'{num1} divided by {num2} is {result}')

# Call the main function.
if __name__ == '__main__':
    main()