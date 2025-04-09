# Programmer: Mason Colacicco
# Date: March
# Program: Employee and Production Worker Class

class Employee:
    def __init__(self, name, id):
        self.__name = name
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_id(self, id):
        self.__id = id

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id


class Production(Employee):
    def __init__(self, name, id, shift, rate):
        Employee.__init__(self, name, id)
        self.__shift = shift
        self.__rate = rate

    def set_shift(self, shift):
        self.__shift = shift

    def set_rate(self, rate):
        self.__rate = rate

    def get_shift(self):
        return self.__shift

    def get_rate(self):
        return self.__rate
