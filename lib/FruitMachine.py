import random

class FruitMachine:

    def __init__(self, slot_opts, balance, fee):
        self.slots = slot_opts
        self.balance = balance
        self.fee = fee

    def play(self):
        return (
            random.choice(self.slots),
            random.choice(self.slots),
            random.choice(self.slots),
            random.choice(self.slots)
        )

    def is_winner(self, slots):
        return slots.count(slots[0]) == 4

