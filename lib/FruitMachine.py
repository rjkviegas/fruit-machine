import random

class FruitMachine:
    def __init__(self, slot_opts, balance, fee):
        self.slots = slot_opts
        self.balance = balance
        self.fee = fee
    
    def get_slots(self):
        return self.slots
    
    def get_balance(self):
        return self.balance
    
    def get_fee(self):
        return self.fee
    
    def generate_slot(self):
        return random.choice(self.get_slots())

    def play(self):
        return (
            self.generate_slot(),
            self.generate_slot(),
            self.generate_slot(),
            self.generate_slot()
        )
    
    def is_jackpot(self, aTurn):
        return aTurn.count(aTurn[0]) == len(aTurn)

    def is_one_of_each(self, aTurn):
        def iter(self, aTurn, i):
            if self.is_last_slot(aTurn, i):
                return self.is_one_occurrence(aTurn, i)
            elif self.is_one_occurrence(aTurn, i):
                return iter(self, aTurn, i + 1)
            else:
                return False
        return iter(self, aTurn, 0)
    
    def is_last_slot(self, aTurn, index):
        return index + 1 == len(aTurn)
    
    def is_one_occurrence(self, aTurn, index):
        return aTurn.count(aTurn[index]) == 1
    
    def is_two_in_a_row(self, aTurn):
        def iter(self, aTurn, i):
            if self.is_last_slot(aTurn, i):
                return False
            elif aTurn[i] == aTurn[i + 1]:
                return True
            else:
                return iter(self, aTurn, i + 1)
        return iter(self, aTurn, 0)
