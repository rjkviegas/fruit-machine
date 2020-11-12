from PrizeCalculator import PrizeCalculator, JackpotCalculator
from PrizeCalculator import OneOfEachCalculator, TwoInARowCalculator

class PrizeCalculatorFactory:
    @classmethod
    def createPrizeCalculator(cls, turn, player, game_machine):
            if cls.is_jackpot(turn.get_slots()):
                return JackpotCalculator(player, game_machine)
            elif cls.is_one_of_each(turn.get_slots()):
                return OneOfEachCalculator(player, game_machine)
            elif cls.is_two_in_a_row(turn.get_slots()):
                return TwoInARowCalculator(player, game_machine)
    
    @classmethod
    def is_jackpot(cls, slots_tup):
        return slots_tup.count(slots_tup[0]) == len(slots_tup)
    
    @classmethod
    def is_one_of_each(cls, slots_tup):
        def is_one_of_each_helper(slots_tup, i):
            if cls.is_last_slot(slots_tup, i):
                return cls.only_one_occurrence(slots_tup, i)
            elif cls.only_one_occurrence(slots_tup, i):
                return is_one_of_each_helper(slots_tup, i + 1)
            else:
                return False
        return is_one_of_each_helper(slots_tup, 0)
    
    @classmethod
    def is_two_in_a_row(cls, slots_tup):
        def is_two_in_a_row_helper(slots_tup, i):
            if cls.is_last_slot(slots_tup, i):
                return False
            elif slots_tup[i] == slots_tup[i + 1]:
                return True
            else:
                return is_two_in_a_row_helper(slots_tup, i + 1)
        return is_two_in_a_row_helper(slots_tup, 0)
    
    @classmethod
    def only_one_occurrence(cls, slots_tup, index):
        return slots_tup.count(slots_tup[index]) == 1
    
    @classmethod
    def is_last_slot(cls, slots_tup, index):
        return index + 1 == len(slots_tup)