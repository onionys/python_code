#!/usr/bin/env python3

battle = []

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

        self.hp = 20
        self.mp = 10
        self.attack_point = 5

    def __str__(self):
        return "[" + self.name + "]"

    def attack(self,enemy):
        _type = str(type(self)).split('.')[1][:-2]
        print("{} attack {} by {} power.".format(self,enemy,_type) )
        enemy.hp -= self.attack_point 
        if enemy.hp <= 0:
            if enemy in battle :
                battle.remove(enemy)
                print("!!!!!!     ",enemy,"out battle")


class Magic(Person):
    def __init__(self,name):
        super().__init__(name,30)
        self.mp = 30
        self.attack_point = 10

    def attack(self,enemy):
        if(self.mp >= 10):
            self.mp -= 15
            super().attack(enemy)
        else:
            print("!!!! {} Out of MP...".format(self))




def main():
    battle.append(Person('John',25))
    battle.append(Person('David',25))
    battle.append(Person('Bob',25))
    battle.append(Magic('TTTT'))
    battle.append(Magic('GGGG'))

    for i in battle:
        print("Player:",i)

    input("GAME START")

    from random import shuffle
    from time import sleep

    while(len(battle) > 1):
        shuffle(battle)
        print("--"*20)
        battle[0].attack(battle[1])
        sleep(1.2)
    print("GAME OVER")
    print("=======The Winner is", battle[0], "===========")


if __name__ == "__main__":
    main()
