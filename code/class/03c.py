#!/usr/bin/env python3
import types


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        if(type(name) == str):
            self.__name = name


    def say_hi(self, name=""):
        print("Hi! ",name)
        print("I'm ", self.__name)

    def __str__(self):
        msg =  "-" * 25 + "\n"
        msg += "name: " + self.name + "\n"
        msg += "age : {}\n".format(self.age)
        msg += "-" * 25 + "\n"
        return msg


if __name__ == "__main__":
    someone = Person("John",19)
    print(someone.name)
    print(someone.age)
    print(someone)
    print(dir(someone))

    pass

