import random

class FruitMachine:
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
        return self.turnClass(self.slots)
