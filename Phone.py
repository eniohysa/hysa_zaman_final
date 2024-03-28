# Enio Hysa
# February 29, 2024
# CMPSC132
# Phone.py


class Phone:
    # Initialize
    def __init__(self, number, phone_type):
        self.__number = number
        self.__phone_type = phone_type

    # Setters
    def set_number(self, number):
        self.__number = number

    def set_phone_type(self, phone_type):
        self.__phone_type = phone_type

    # Getters
    def get_number(self):
        return self.__number

    def get_phone_type(self):
        return self.__phone_type

    # Print number and type in parentheses
    def __str__(self):
        return f"{self.__number} ({self.__phone_type})"