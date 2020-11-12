from PrizeCalculator import PrizeCalculator, JackpotCalculator
from PrizeCalculator import OneOfEachCalculator, TwoInARowCalculator

class PrizeCalculatorFactory:
    def createPrizeCalculator(self, turn, player, game_machine):
            if turn.is_jackpot():
                return JackpotCalculator(player, game_machine)
            elif turn.is_one_of_each():
                return OneOfEachCalculator(player, game_machine)
            elif turn.is_two_in_a_row():
                return TwoInARowCalculator(player, game_machine)