from PrizeFactory import DefaultPrizeFactory
import random

class GameMachine:
    def __init__(self, slot_options, balance,
                fee, turn_generator, prize_factory):
        self.slot_options = slot_options
        self.balance = balance
        self.fee = fee
        self.turn_generator = turn_generator
        self.prize_factory = prize_factory()
    
    def get_slot_options(self):
        return self.slot_options
    
    def get_balance(self):
        return self.balance
    
    def get_fee(self):
        return self.fee
    
    def get_prize_factory(self):
        return self.prize_factory

    def play(self, player):
        turn = self.turn_generator(self.get_slot_options())
        prize = self.get_prize_factory().create_prize(turn, player, self)
        self.payout(prize)
    
    def payout(self, prize):
        try:
            prize.payout_to_player()
        except AttributeError:
            print('Sorry, no prize this time.') 