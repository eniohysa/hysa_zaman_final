class Semester:
    def __init__(self, season, year):
        self.__season = season
        self.__year = year

    def get_season(self):
        return self.__season

    def get_year(self):
        return self.__year

    def set_season(self, season):
        self.__season = season

    def set_year(self, year):
        self.__year = year

    def __str__(self):
        return f"Semester: {self.__season} {self.__year}"
