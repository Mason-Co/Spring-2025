# Programmer: Mason Colacicco
# Date: March
# Program: Pet Info

from pets import Pet

def main():
    # Initialize variables
    pet_name = ''
    pet_type = ''
    pet_age = 0

    # User input to create a pet
    pet_name = input("What is the pet name? ")
    pet_type = input("What is the pet type? ")
    pet_age = input("What is the pet age (human years)? ")

    # Create the pet
    myPet = Pet(pet_name, pet_type, pet_age)

    # Display data
    print("Here is the pet data: ")
    print("Pet Name:", myPet.get_name())
    print("Pet Type:", myPet.get_animal_type())
    print("Pet Age (years):", myPet.get_age())


if __name__ == '__main__':
    main()