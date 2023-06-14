class Year:
    def __init__(self,days,season) -> None:
        self.__days = days
        self.__season = season

# #ГЕТТЕРЫ
#     def get_days(self):
#         return self.__days
    
#     def get_season(self):
#         return self.__season
    
# #СЕТТЕРЫ
#     def set_days(self, days):
#         if days == 365 or days == 366:
#             self.__days = days
#         else:
#             raise Exception('Неверно')

#     def set_season(self, season):
#         self.__season = season

    @property
    def days(self):
        return self.__days
    
    @days.setter
    def days(self, days):
        if days == 365 or days == 366:
            self.__days = days
        else:
            raise Exception('Неверно')
        self.__days = days

    @property
    def season(self):
        return self.__season
    
    @season.setter
    def season(self, season):
        self.__season = season

year = Year(365,'summer')

year.days = 365
year.season = 'winter'
print(year.season)
print(year.days)

# year.set_days(450)
# year.set_season('winter')
# print(year.get_days())
# print(year.get_season())











# class Person:
#     def __init__(self, name, age) -> None:
#         self.__name = name
#         self.__age = age

#     @property
#     def name(self):
#         return self.__name
    
#     @name.setter
#     def name(self, name):
#         self.__name = name
    
#     @property
#     def age(self):
#         return self.__age
    
#     @age.setter
#     def age(self, age):
#         if age <= 0:
#             raise ValueError('Not born')
#         self.__age = age


# person = Person('Ваня', -7)
# person.age = 12
# person.name = 'Катя'
# print(person.name)
# print(person.age)