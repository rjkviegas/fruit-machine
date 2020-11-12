import random

class FruitMachineTurn:
    def __init__(self, slot_options):
        self.slots = self.generate_slots(slot_options, len(slot_options))

    def generate_slots(self, slot_options, num_of_reels):
        result = list()
        for reel in range(num_of_reels):
            result.append(random.choice(slot_options))
        print(result)
        return tuple(result)
    
    def get_slots(self):
        return self.slots

class FourReelsTurn(FruitMachineTurn):
    def __init__(self, slot_options):
        self.num_of_reels = 4
        self.slots = self.generate_slots(slot_options, self.num_of_reels)
    