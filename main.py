import random
import os


class Voin:
    def __init__(self, name, attack):
        self.name = name
        self.hp = 100
        self.attack = attack
        self.lvl = 1
        self.money = 10
        self.inventory = []

    def srt(self):
        swr = Sword("Меч", 10)
        p3.inventory.append(swr)
        p3.attack += swr.attack
        print("-------")
        print("В ваш инвентарь добавился мечь")
        print("-------")

    def visibl(self):
        print("-Статистика-")
        print(f"Имя: {self.name}")
        print(f"Здоровье:{self.hp}")
        print(type(self))
        print(f"Атака: {self.attack}")
        print(f"Уровень: {self.lvl}")
        print(f"Деньги: {self.money}")
        print(f"Инвентарь: {self.inventory}")
        print("------------")

    def combat_turn(self):
        if self.hp > 0:
            damage = self.attack
            p1.hp -= damage
            print("-------")
            print(f"{self.name} ударил {p1.name} на {damage} жизней!")
            print("-------")
            
    def combat_turn2(self):
        if self.hp > 0:
            damage = self.attack
            p3.hp -= damage
            print("-------")
            print(f"{self.name} ударил {p3.name} на {damage} жизней!")    
            print("-------")    

    def fights(self):
        while p3.hp > 0 and p1.hp > 0:
            p3.combat_turn()
            p1.combat_turn2()
            print("")
            print(f"{p1.name} {p1.hp}")
            print(f"{p3.name} {p3.hp}")
            input("\nНажмите ENTER чтобы сделать следующий ход")
        os.system("cls")
        if p3.hp > 0 and p1.hp <= 0:
            print("-------")
            print(f"{p3.name} победил!")
            print("-------")

        elif p3.hp <= 0 and p1.hp > 0:
            print("-------")
            print(f"{p1.name} победил!")
            print("-------")
        else:
            print("-------")
            print(f"{p1.name} и {p3.name} пали в бою:(")
            print("-------")

class Npc(Voin):
    def __init__(self, name, attack):
        super().__init__(name, attack)


class Sword:
    def __init__(self, name, attack):
        self.name = name
        self.attack = attack


first_names = ("Жран", "Дрын", "Брысь", "Жлыг", "Паша")
last_names = ("Ужасный", "Зловонный", "Борзый", "Кровавый", "Жирный")

namess = input("Введите имя и нажмите ENTER! ")
namesf = random.choice(first_names) + " " + random.choice(last_names)      

p3 = Voin(namess, 10)
p1 = Npc(namesf, random.randint(1, 10))



p3.srt()
p3.visibl()
p1.visibl()
p3.fights()
p3.visibl()
p1.visibl()


