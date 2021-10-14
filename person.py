class Person():
    def __init__(self):
        self.__age = None
        self.__name = None

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,ika):
        self.__age = ika

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,nimi):
        self.__name = nimi

    def __str__(self):
        return print(f"{self.__name}, aged {self.__age}")