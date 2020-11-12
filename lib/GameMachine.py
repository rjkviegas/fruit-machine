from PrizeCalculatorFactory import PrizeCalculatorFactory
import random

class GameMachine:
    def __init__(self, slot_opts, balance,
                fee, turnClass, prizeCalculatorFactory):
        self.slots = slot_opts
        self.balance = balance
        self.fee = fee
        self.turnClass = turnClass
        self.prizeCalculatorFactory = prizeCalculatorFactory
    
    def get_slots(self):
        return self.slots
    
    def get_balance(self):
        return self.balance
    
    def get_fee(self):
        return self.fee
    
    def get_prize_calculator_factory(self):
        return self.prizeCalculatorFactory

    def play(self, player):
        turn = self.turnClass(self.get_slots())
        calculator = self.get_prize_calculator_factory().createPrizeCalculator(turn, player, self)
        self.payout_prize_calculated_by(calculator)
    
    def payout_prize_calculated_by(self, calculator):
        try:
            calculator.payout_prize()
        except AttributeError:
            print('Sorry, no prize this time.') 