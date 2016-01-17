#!/usr/bin/env python3


class Person:

    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def say_hi(self):
        print("Hi! I am")
        print(self.__name)

    def vote(self,man):
        if self.__age >= 20:
            print("you vote ", man)
        else:
            print("You can't vote because you age.")

    def __str__(self):
        return "Hello this is str..."


if __name__ == "__main__":
    man1 = Person("John")  # call man1.__init__()
    man2 = Person("David") # call man2.__init__()
    print(man1.name)
    print(man2.name)
    man1.say_hi()
    man2.say_hi()







    ## dynamically add attitudes
    someone.age  = 19
    print("age", someone.age)





    ## dynamically add member functions 
    import types
    def temp_func(self):
        print("Hi! I'm ", self.name)
    someone.say_hi = types.MethodType(temp_func,someone)
    someone.say_hi()



