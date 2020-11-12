from PrizeFactory import DefaultPrizeFactory
import random

class GameMachine:
    def __init__(self, slot_opts, balance,
                fee, turn_class, prize_factory):
        self.slots = slot_opts
        self.balance = balance
        self.fee = fee
        self.turn_class = turn_class
        self.prize_factory = prize_factory()
    
    def get_slots(self):
        return self.slots
    
    def get_balance(self):
        return self.balance
    
    def get_fee(self):
        return self.fee
    
    def get_prize_factory(self):
        return self.prize_factory

    def play(self, player):
        turn = self.turn_class(self.get_slots())
        prize = self.get_prize_factory().create_prize(turn, player, self)
        self.payout(prize)
    
    def payout(self, prize):
        try:
            prize.payout_to_player()
        except AttributeError:
            print('Sorry, no prize this time.') 