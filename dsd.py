class ATM:
    last_id = 0
    all_atms = []

    @classmethod
    def count_atms(cls):
        print("Всего банкоматов", len(cls.all_atms))

    def __init__(self):
        self.id = ATM.last_id
        self._total = 0
        ATM.last_id += 1
        ATM.all_atms.append(self)

    def deposit(self, money):
        self._total += money
        print(f"Внесли {money}, на счёте {self.total}")

    def withdraw (self, money):
        print("карта опознана")
        print("пин-код опознану")
        self._total -= money
        print(f"сняли {money}, на счёте {self._total}")


    
atm1 = ATM()
atm2 = ATM()

print(atm1.id)
print(atm2.id)

ATM.count_atms()