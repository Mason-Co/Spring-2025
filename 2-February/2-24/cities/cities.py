# Programmer: Mason Colacicco
# Date: February
# Program: Cities

def main():
    try:
        # Initialize cities
        cities = ['blaine', 'st. paul', 'brooklyn park', 'edina', 'hastings']

        # User input to find city
        city_remove = input("Enter city you do not want to visit. ").lower()
        i = cities.index(city_remove)

        # User input to replace city
        city_visit = input("Enter a city you would like to visit. ").lower()
        cities[i] = city_visit

        # Display data
        print(cities)
    except ValueError:
        # Display error
        print("That city is not in the list.")

# Call main function
if __name__ == '__main__':
    main()