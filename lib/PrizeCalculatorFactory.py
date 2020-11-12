from PrizeCalculator import PrizeCalculator, JackpotCalculator
from PrizeCalculator import OneOfEachCalculator, TwoInARowCalculator

class PrizeCalculatorFactory:
    def create_prize_calculator(self, turn, player, game_machine):
            if self.is_jackpot(turn.get_slots()):
                return JackpotCalculator(player, game_machine)
            elif self.is_one_of_each(turn.get_slots()):
                return OneOfEachCalculator(player, game_machine)
            elif self.is_two_in_a_row(turn.get_slots()):
                return TwoInARowCalculator(player, game_machine)
    
    def is_jackpot(self, slots_tup):
        return slots_tup.count(slots_tup[0]) == len(slots_tup)
    
    def is_one_of_each(self, slots_tup):
        def is_one_of_each_helper(slots_tup, i):
            if self.is_last_slot(slots_tup, i):
                return self.only_one_occurrence(slots_tup, i)
            elif self.only_one_occurrence(slots_tup, i):
                return is_one_of_each_helper(slots_tup, i+1)
            else:
                return False
        return is_one_of_each_helper(slots_tup, 0)
    
    def is_two_in_a_row(self, slots_tup):
        def is_two_in_a_row_helper(slots_tup, i):
            if self.is_last_slot(slots_tup, i):
                return False
            elif slots_tup[i] == slots_tup[i+1]:
                return True
            else:
                return is_two_in_a_row_helper(slots_tup, i+1)
        return is_two_in_a_row_helper(slots_tup, 0)
    
    def only_one_occurrence(self, slots_tup, i):
        return slots_tup.count(slots_tup[i]) == 1
    
    def is_last_slot(self, slots_tup, i):
        return len(slots_tup) == i+1

class DefaultPrizeCalculatorFactory(PrizeCalculatorFactory):
        def create_prize_calculator(self, turn, player, game_machine):
            if self.is_jackpot(turn.get_slots()):
                return JackpotCalculator(player, game_machine)
            elif self.is_one_of_each(turn.get_slots()):
                return OneOfEachCalculator(player, game_machine)
            elif self.is_two_in_a_row(turn.get_slots()):
                return TwoInARowCalculator(player, game_machine)
