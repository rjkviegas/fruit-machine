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

    def play(self):
        return Turn(self.slots)
    
    def is_jackpot(self, turn):
        return turn.count(turn[0]) == len(turn)

    def is_one_of_each(self, turn):
        def is_one_of_each_helper(self, turn, i):
            if self.is_last_slot(turn, i):
                return self.is_one_occurrence(turn, i)
            elif self.is_one_occurrence(turn, i):
                return is_one_of_each_helper(self, turn, i + 1)
            else:
                return False
        return is_one_of_each_helper(self, turn, 0)
    
    def is_last_slot(self, turn, index):
        return index + 1 == len(turn)
    
    def is_one_occurrence(self, turn, index):
        return turn.count(turn[index]) == 1
    
    def is_two_in_a_row(self, turn):
        def is_two_in_a_row_helper(self, turn, i):
            if self.is_last_slot(turn, i):
                return False
            elif turn[i] == turn[i + 1]:
                return True
            else:
                return is_two_in_a_row_helper(self, turn, i + 1)
        return is_two_in_a_row_helper(self, turn, 0)

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
