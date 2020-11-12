from PrizeFactory import DefaultPrizeFactory
import random

class GameMachine:
    def __init__(self, slot_opts, balance,
                fee, turn_class, prize_calculator_factory):
        self.slots = slot_opts
        self.balance = balance
        self.fee = fee
        self.turn_class = turn_class
        self.prize_calculator_factory = prize_calculator_factory()
    
    def get_slots(self):
        return self.slots
    
    def get_balance(self):
        return self.balance
    
    def get_fee(self):
        return self.fee
    
    def get_prize_calculator_factory(self):
        return self.prize_calculator_factory

    def play(self, player):
        turn = self.turn_class(self.get_slots())
        calculator = self.get_prize_calculator_factory().create_prize_calculator(turn, player, self)
        self.payout_prize_calculated_by(calculator)
    
    def payout_prize_calculated_by(self, calculator):
        try:
            calculator.payout_prize()
        except AttributeError:
            print('Sorry, no prize this time.') 