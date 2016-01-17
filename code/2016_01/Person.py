#!/usr/bin/env python3

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def say_hi(self):
        print("Hi! I am")
        print(self.name)

    def vote(self,man):
        if self.age >= 20:
            print("you vote ", man)
        else:
            print("You can't vote because you age.")

    def __str__(self):
        return self.name 

    def __enter__(self):
        print("---------------{} call __enter__".format(self.name))

    def __exit__(self,exc_type,exc_val, exc_tb):
        print("---------------{} call __exit__".format(self.name))


from random import randint

class Student(Person):
    def __init__(self, name, age):
        super().__init__(name,age)
        self.score = 0
        self.accept_test_to_get_score()

    def accept_test_to_get_score(self):
        self.score = randint(0,100)

    def get_score(self):
        return self.score

    def set_score(self,score):
        self.score = score


class Teacher(Person):
    def __init__(self,name):
        super().__init__(name,40)
        pass

    def give_score(self, student, score):
        student.set_score(score)

            
def main2():
    student = Student('john',25)
    teacher = Teacher("David")
    print("student score: ", student.get_score())
    teacher.give_score(student,90)
    print("teacher give student score: ",90)
    print("student score: ", student.get_score())


def main():
    man1 = Person("John",25)  # call man1.__init__()
    with man1 :
        print(man1)

def main1():
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



if __name__ == "__main__":
    main2()
