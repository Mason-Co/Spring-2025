# This program divides a number by another number.

def main():
    # Get two numbers.
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))

    if num2 != 0:
        result = num1 / num2
        print(f'{num1} divided by {num2} is {result}')
    else:
        print('Second number is a 0; cannot divide by 0.')

# Call the main function.
if __name__ == '__main__':
    main()