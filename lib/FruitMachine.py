import random

class FruitMachine:

    def __init__(self, slot_opts, win_combs):
        self.slots = slot_opts
        self.win_combs = win_combs

    def play(self):
        return (
            random.choice(self.slots),
            random.choice(self.slots),
            random.choice(self.slots),
            random.choice(self.slots)
        )
    
    def is_winner(self, slots):
        return slots in self.win_combs

