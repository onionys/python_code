#!/usr/bin/env python3
import types

class Person:
    pass


if __name__ == "__main__":
    someone = Person()
    print(someone)

    ## dynamically add attitudes
    someone.name = "John"
    someone.age  = 19

    print("name", someone.name)
    print("age", someone.age)



    ## dynamically add member functions 
    def temp_func(self):
        print("Hi! I'm ", self.name)

    someone.say_hi = types.MethodType(temp_func,someone)
    someone.say_hi()

    pass

