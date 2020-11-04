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
    
    def is_jackpot(self, slots):
        return slots.count(slots[0]) == len(slots)

    def is_one_of_each(self, slots):
        def iter(self, slots, i):
            if self.is_last_slot(slots, i):
                return self.is_one_occurrence(slots, i)
            elif self.is_one_occurrence(slots, i):
                return iter(self, slots, i + 1)
            else:
                return False
        return iter(self, slots, 0)
    
    def is_last_slot(self, slots, slots_index):
        return slots_index + 1 == len(slots)
    
    def is_one_occurrence(self, slots, index):
        return slots.count(slots[index]) == 1
            
