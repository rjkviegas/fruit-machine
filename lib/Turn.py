import random

class Turn:
    def __init__(self, slot_options):
        self.slots = (
            random.choice(slot_options),
            random.choice(slot_options),
            random.choice(slot_options),
            random.choice(slot_options)
        )
    
    def get_slots(self):
        return self.slots
    
    def is_last_slot(self, index):
        return index + 1 == len(self.get_slots())
    
    def is_one_occurrence(self, index):
        return self.get_slots().count(self.get_slots()[index]) == 1

    def is_jackpot(self):
        return self.get_slots().count(self.get_slots()[0]) == len(self.get_slots())
    
    def is_one_of_each(self):
        def is_one_of_each_helper(self, i):
            if self.is_last_slot(i):
                return self.is_one_occurrence(i)
            elif self.is_one_occurrence(i):
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