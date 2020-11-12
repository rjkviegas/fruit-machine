from PrizeCalculator import PrizeCalculator, JackpotCalculator
from PrizeCalculator import OneOfEachCalculator, TwoInARowCalculator

class Player:  
    def __init__(self, balance):
        self.balance = balance
    
    def get_balance(self):
        return self.balance
    
    def play(self, game):
        self.pay_fee_for(game)
        game.play(self)
    
    def pay_fee_for(self, game):
        if self.get_balance() < game.fee:
            raise InsufficientBalance('Insufficient balance to play')
        self.balance -= game.get_fee()
        game.balance += game.get_fee() 

class InsufficientBalance(ZeroDivisionError):
	def __init__(self, msg):
	    self.msg = msg