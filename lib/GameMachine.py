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

    def play(self):
        turn = self.turnClass(self.get_slots())
        for reel in turn.get_slots():
            print(reel)
        return turn