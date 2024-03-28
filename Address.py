# Enio Hysa
# February 29, 2024
# CMPSC132
# Address.py


class Address:
    # Initialize
    def __init__(self, street, city, state, zipcode):
        self.__street = street
        self.__city = city
        self.__state = state
        self.__zip = zipcode

    # Setters
    def set_street(self, street):
        self.__street = street

    def set_city(self, city):
        self.__city = city

    def set_state(self, state):
        self.__state = state

    def set_zip(self, zipcode):
        self.__zip = zipcode

    # Getters
    def get_street(self):
        return self.__street

    def get_city(self):
        return self.__city

    def get_state(self):
        return self.__state

    def get_zip(self):
        return self.__zip

    # Print address
    def __str__(self):
        return f'{self.__street}, {self.__city}, {self.__state} {self.__zip}'
