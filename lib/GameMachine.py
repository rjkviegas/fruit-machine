from PrizeCalculatorFactory import PrizeCalculatorFactory
import random

class GameMachine:
    def __init__(self, slot_opts, balance, fee, turnClass, prizeCalculatorFactoryClass):
        self.slots = slot_opts
        self.balance = balance
        self.fee = fee
        self.turnClass = turnClass
        self.prizeCalculatorFactory = prizeCalculatorFactoryClass()
    
    def get_slots(self):
        return self.slots
    
    def get_balance(self):
        return self.balance
    
    def get_fee(self):
        return self.fee

    def play(self, player):
        turn = self.turnClass(self.get_slots())
        calculator = self.prizeCalculatorFactory.createPrizeCalculator(turn, player, self)
        self.payout_prize_calculated_by(calculator)
    
    def payout_prize_calculated_by(self, calculator):
        try:
            calculator.payout_prize()
        except AttributeError:
            print('Sorry, no prize this time.') 