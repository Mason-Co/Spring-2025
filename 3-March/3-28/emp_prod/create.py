# Programmer: Mason Colacicco
# Date: March
# Program: Employee and Production Worker Class

import emp_prod


def main():
    # Initialize variables
    worker_name = ''
    worker_id = 0
    worker_shift = 0
    worker_rate = 0.0

    # User input
    worker_name = input("Enter worker name: ")
    worker_id = int(input("Enter worker ID: "))
    worker_shift = int(input("Enter worker shift number: "))
    worker_rate = float(input("Enter worker pay rate: "))

    # Instantiate worker object
    worker = emp_prod.Production(worker_name, worker_id, worker_shift, worker_rate)

    # Display data
    print(f'Name: {worker.get_name()}')
    print(f'ID: {worker.get_id()}')
    print(f'Shift: {worker.get_shift()}')
    print(f'Pay Rate: ${worker.get_rate():.2f}')


# Call main function
if __name__ == '__main__':
    main()
