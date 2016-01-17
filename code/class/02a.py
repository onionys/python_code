#!/usr/bin/env python3

class Person:

    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def say_hi(self,name=""):
        print("Hi! {}".format(name))
        print("I'm {}".format(self.name))

    def __str__(self):
        msg = "-" * 25 + "\n"
        msg += "name:{} age:{}\nheight:{} weight{}\n".format(self.name, self.age, self.height, self.weight)
        msg += "-" * 25 + "\n"
        return msg

if __name__ == "__main__":
    someone = Person("John",19,170.0,75.0)
    someone.say_hi()

    print(someone)
    pass

