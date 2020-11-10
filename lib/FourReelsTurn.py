import random

class FruitMachineTurn:
    def __init__(self, slot_options):
        self.num_of_reels = len(slot_options)
        self.slots = self.generate_slots(slot_options, self.num_of_reels)

    def generate_slots(self, slot_options, num_of_reels):
        result = list()
        for x in range(num_of_reels):
                result.append(random.choice(slot_options))
        return tuple(result)
    
    def get_slots(self):
        return self.slots
    
    def get_num_of_reels(self):
        return self.num_of_reels
    
    def is_last_slot(self, index):
        return index + 1 == self.get_num_of_reels()
    
    def only_one_occurrence(self, index):
        return self.get_slots().count(self.get_slots()[index]) == 1

class FourReelsTurn(FruitMachineTurn):
    def __init__(self, slot_options):
        self.num_of_reels = 4
        super().__init__(slot_options)

    def is_jackpot(self):
        return self.get_slots().count(self.get_slots()[0]) == self.get_num_of_reels()
    
    def is_one_of_each(self):
        def is_one_of_each_helper(self, i):
            if self.is_last_slot(i):
                return self.only_one_occurrence(i)
            elif self.only_one_occurrence(i):
                return is_one_of_each_helper(self, i + 1)
            else:
                return False
        return is_one_of_each_helper(self, 0)
    
    def is_two_in_a_row(self):
        def is_two_in_a_row_helper(self, i):
            if self.is_last_slot(i):
                return False
            elif self.get_slots()[i] == self.get_slots()[i + 1]:
                return True
            else:
                return is_two_in_a_row_helper(self, i + 1)
        return is_two_in_a_row_helper(self, 0)
    