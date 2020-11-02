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

    def play(self):
        return (
            random.choice(self.get_slots()),
            random.choice(self.get_slots()),
            random.choice(self.get_slots()),
            random.choice(self.get_slots())
        )
    
    def is_jackpot(self, slots):
        return slots.count(slots[0]) == 4

    def is_one_of_each(self, slots):
        def iter(self, slots, i):
            if i == len(slots) - 1:
                return slots.count(slots[i]) == 1
            elif slots.count(slots[i]) == 1:
                return True and iter(self, slots, i + 1)
            else:
                return False
        return iter(self, slots, 0)
            
