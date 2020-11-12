from PrizeCalculator import PrizeCalculator, JackpotCalculator
from PrizeCalculator import OneOfEachCalculator, TwoInARowCalculator

class PrizeCalculatorFactory:
    def createPrizeCalculator(self, turn, player, game_machine):
            if turn.is_jackpot():
                return JackpotCalculator(turn, player, game_machine)
            elif turn.is_one_of_each():
                return OneOfEachCalculator(turn, player, game_machine)
            elif turn.is_two_in_a_row():
                return TwoInARowCalculator(turn, player, game_machine)