#!/usr/bin/env python3
import types
import random

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self, name=""):
        print("Hi! ",name)
        print("I'm ", self.name)

    def __str__(self):
        msg =  "-" * 25 + "\n"
        msg += "name: " + self.name + "\n"
        msg += "age : {}\n".format(self.age)
        msg += "-" * 25 + "\n"
        return msg




class Student(Person):
    def __init__(self,name,age,major):
        super().__init__(name,age)
        self.major = major

    def get_test(self):
        return random.randint(0,100)

    def say_hi(self):
        super().say_hi()
        print("My major is ", self.major)



if __name__ == "__main__":
    some_student = Student("John",23,"Math")
    some_student.say_hi()
    print()
    print("score:", some_student.get_test())
    print()
    print(some_student)
