class Player:
    def __init__(self, name="Безымянный"):
        self.name = name
        self.hp = 100
    
    def ride(self):
        print("ТЫАЛЫВЬЛАЬДПЫПЫЗПЫДВБАДЖЫПЫВБАЫДБППДЫАБДПЫЬПДЫПБДЫПЫБПЫ")

    def heal(self):
        self.hp += 15
        print("вылечил 15 hp")


p1 = Player()
p2 = Player("Ася")
p3 = Player("Квася")

print(p1.name)
print(p2.name)
print(p3.name)