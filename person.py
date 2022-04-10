# Filename      person.py
# Authors:      Jenna Laaksovirta, Karolina Mäkinen ja Sanna Salminen
# Description:  Setting persons infromation that are going to play the game

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def set_name(self, name):
        self.__name = name
    
    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def __str__(self):
        return f'Name: {self.__name}, Age: {self.__age}'