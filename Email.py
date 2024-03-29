class Email:
    def __init__(self, address, email_type):
        self.__address = address
        self.__type = email_type

    def get_address(self):
        return self.__address

    def get_type(self):
        return self.__type

    def set_address(self, address):
        self.__address = address

    def set_type(self, email_type):
        self.__type = email_type

    def __str__(self):
        return f"Email: {self.__address} ({self.__type})"
