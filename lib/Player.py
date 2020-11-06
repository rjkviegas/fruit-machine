from PrizeCalculator import PrizeCalculator, JackpotCalculator
from PrizeCalculator import OneOfEachCalculator, TwoInARowCalculator

class Player:  
    def __init__(self, balance):
        self.balance = balance
    
    def get_balance(self):
        return self.balance
    
    def play(self, game):
        self.pay_for(game)
        turn = game.play()
        calculator = self.createPrizeCalculator(turn, self, game)
        try:
            calculator.payout_prize()
        except AttributeError:
            print('Sorry, no prize this time.')
    
    def pay_for(self, game):
        if self.get_balance() < game.fee:
            raise InsufficientBalance('Insufficient balance to play')
        self.balance -= game.get_fee()
        game.balance += game.get_fee()

    def createPrizeCalculator(self, turn, player, game):
        if game.is_jackpot(turn):
            return JackpotCalculator(turn, player, game)
        elif game.is_one_of_each(turn):
            return OneOfEachCalculator(turn, player, game)
        elif game.is_two_in_a_row(turn):
            return TwoInARowCalculator(turn, player, game)

class InsufficientBalance(ZeroDivisionError):
	def __init__(self, msg):
	    self.msg = msg