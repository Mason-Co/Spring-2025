# Programmer: Mason Colacicco
# Date: March
# Program: Employee Class

# Create class
class Employee:
    def __init__(self, name, id, dept, title):
        self.__name = name
        self.__id = id
        self.__dept = dept
        self.__title = title

    # Create get methods
    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__id
    def get_dept(self):
        return self.__dept
    def get_title(self):
        return self.__title

def main():
    # Create objects
    emp1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
    emp2 = Employee("Mark Jones", 39119, "IT", "Programmer")
    emp3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")

    # Display data
    print("Name\t\t\tID\t\tDepartment\t\tTitle")
    print(f"{emp1.get_name()}\t{emp1.get_id()}\t{emp1.get_dept()}\t\t{emp1.get_title()}")
    print(f"{emp2.get_name()}\t\t{emp2.get_id()}\t{emp2.get_dept()}\t\t\t\t{emp2.get_title()}")
    print(f"{emp3.get_name()}\t\t{emp3.get_id()}\t{emp3.get_dept()}\t{emp3.get_title()}")

# Call main function
if __name__ == '__main__':
    main()