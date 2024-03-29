class Date:
    def __init__(self, day, month, year):
        self.__day = day
        self.__month = month
        self.__year = year

    def set_day(self, day):
        self.__day = day

    def set_month(self, month):
        self.__month = month

    def set_year(self, year):
        self.__year = year

    def get_day(self):
        return self.__day

    def get_month(self):
        return self.__month

    def get_year(self):
        return self.__year

    def __str__(self):
        return f"{self.__month} {self.__day}, {self.__year}"
