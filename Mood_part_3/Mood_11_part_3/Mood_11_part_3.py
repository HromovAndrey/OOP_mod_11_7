class Apartment:
    def __init__(self, num_rooms, area):
        self.__num_rooms = num_rooms
        self.__area = area

    def get_num_rooms(self):
        return self.__num_rooms
    def get_area(self):
        return self.__area

apartment = Apartment(4 ,54)
print(f"{apartment.get_num_rooms()=}")
print(f"{apartment.get_area()=}")


class Event:
    def __init__(self, name, desc, date):
        self.__name = name
        self.__desc = desc
        self.__date = date

    def set_data(self, new_date):
        self.__date = new_date
    def set_desc(self, new_desc):
        self.__desc = new_desc

    def get_name(self):
        return self.__name

    def get_data(self):
        return self.__data

    def get_desc(self):
        return self.__desc

    def __str__(self):
        return f"Name:{}"