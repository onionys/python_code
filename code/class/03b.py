#!/usr/bin/env python3
import types


class Person:
    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)

    def say_hi(self, name=""):
        print("Hi! ",name)
        print("I'm ", self.__name)

    def get_name(self):
        return self.__name

    def set_name(self,name):
        if(type(name) == str):
            self.__name = name
        else:
            self.__name = "unknown"

    def get_age(self):
        return self.__age

    def set_age(self,age):
        try:
            age = int(age)
            if(age > 0):
                self.__age = age
            else:
                self.__age = 18
        except:
            pass


    def __str__(self):
        msg =  "-" * 25 + "\n"
        msg += "name: " + self.__name + "\n"
        msg += "age : {}\n".format(self.__age)
        msg += "-" * 25 + "\n"
        return msg


if __name__ == "__main__":
    someone = Person("John",19)
    someone.say_hi()
    print(someone.get_age())
    print(someone)
    print(dir(someone))

    pass

