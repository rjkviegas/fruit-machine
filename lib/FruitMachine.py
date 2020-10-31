import random

def create_win_combs(slot_opts):
        return tuple(map(lambda x: (x,)*4, slot_opts))

class FruitMachine:

    def __init__(self, slot_opts):
        self.slots = slot_opts
        self.win_combs = create_win_combs(self.slots)

    def play(self):
        return (
            random.choice(self.slots),
            random.choice(self.slots),
            random.choice(self.slots),
            random.choice(self.slots)
        )
    
    def is_winner(self, slots):
        return slots in self.win_combs

