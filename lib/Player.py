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
        if turn.is_jackpot():
            print("You hit the jackpot!")
            return JackpotCalculator(turn, player, game)
        elif turn.is_one_of_each():
            print("That's one of each!")
            return OneOfEachCalculator(turn, player, game)
        elif turn.is_two_in_a_row():
            print("That's two in a row!")
            return TwoInARowCalculator(turn, player, game)

class InsufficientBalance(ZeroDivisionError):
	def __init__(self, msg):
	    self.msg = msg