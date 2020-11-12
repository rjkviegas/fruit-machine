from PrizeCalculator import PrizeCalculator, JackpotCalculator
from PrizeCalculator import OneOfEachCalculator, TwoInARowCalculator
import random

class GameMachine:
    def __init__(self, slot_opts, balance, fee, turnClass):
        self.slots = slot_opts
        self.balance = balance
        self.fee = fee
        self.turnClass = turnClass
    
    def get_slots(self):
        return self.slots
    
    def get_balance(self):
        return self.balance
    
    def get_fee(self):
        return self.fee

    def play(self, player):
        turn = self.turnClass(self.get_slots())
        calculator = self.createPrizeCalculator(turn, player, self)
        self.payout_prize_calculated_by(calculator)
    
    def createPrizeCalculator(self, turn, player, game):
        if turn.is_jackpot():
            print("You hit the jackpot!")
            return JackpotCalculator(turn, player, game)
        elif turn.is_one_of_each():
            print("That's one of each!")
            return OneOfEachCalculator(turn, player, game)
        elif turn.is_two_in_a_row():
            print("That's two in a row!")
            return TwoInARowCalculator(turn, player, game)
    
    def payout_prize_calculated_by(self, calculator):
        try:
            calculator.payout_prize()
        except AttributeError:
            print('Sorry, no prize this time.') 