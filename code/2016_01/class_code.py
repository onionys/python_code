#!/usr/bin/env python3


def say_hi(name="", is_female=True):
    if not name:
        name = "beauty" if is_female else "man"
    print("Hi!", name)


def sec_func(name,*tt):
    print("name:", name)
    for i in tt:
        print(i)
        

print("this is in class_code.py")
print("print", __name__)




def my_func(*tt):
    print(type(tt))
    for i in tt:
        print(i)

def dic_func(**test):
    print(type(test))
    print(test)
    #print(test['name'])

def make_dic(**args):
    return args

if __name__ == "__main__":
    a = (1,2,3,4,5,6,7)
    #my_func(*a)
    #my_func(1,2,3,4,5,6,7)

    #dic_func( age=20,height=176, weight=75)

    #data = {"age":20,"name":"John"}
    #dic_func( **data )

    data = make_dic(name="john",age=18,height=19)
    print(data)














