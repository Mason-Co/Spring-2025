# Programmer: Mason Colacicco
# Date: March
# Program: Cities 2

def main():
    # Initialize the dictionary
    cities = {'Nairobi':1, 'Johannesburg':26, 'Cairo':30, 'Abidjan':5, 'Khartoum':15, 'Zanzibar':6}

    # Copy relevant items
    tropics = {k:v for k,v in cities.items() if v<23}

    # display data
    print(tropics)

# Call main function
if __name__ == '__main__':
    main()