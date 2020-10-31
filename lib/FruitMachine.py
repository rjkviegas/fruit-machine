import random

class FruitMachine:

    def __init__(self, slot_opts):
        self.slots = slot_opts

    def play(self):
        return (
            random.choice(self.slots),
            random.choice(self.slots),
            random.choice(self.slots),
            random.choice(self.slots)
        )
    
    def is_winner(self, slots):
        return slots.count(slots[0]) == 4

