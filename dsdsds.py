class videocard:
    def __init__(self, name="RTX 3090", memory=24, pin=8, damage=0):
        self.name = name
        self.amount_of_memory = memory
        self.additional_power = pin
        self.damege_counter = damage

    def image(self):
        print("-------")
        print("вы попытались вывести изображение")
        print("-------")
        print("вы увидели пустоту потому что мы ещё не умеем выводить изображение")
        print("-------")

    def damager(self):
        print("-------")
        print("Вы решили запустить 5 бенчмарков сразу и ваша видюха перегрелась")
        print("-------")
        print("Перегрев видеокарту вы нанесли ей урон")
        print("-------")
        self.damege_counter += 10
        
        

p1 = videocard()
print("-------")
print(f"Название-{p1.name}")
print("-------")
print(f"Память-{p1.amount_of_memory} гб")
print("-------")
print(f"Доп.питание-{p1.additional_power}")
print("-------")
print(f"Изношеность-{p1.damege_counter}")
print("-------")


p1.damager()

print("-------")
print(f"Изношеность-{p1.damege_counter}")
print("-------")

p1.image()