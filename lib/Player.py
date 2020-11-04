class Player:  
    def __init__(self, aBalance):
        self.balance = aBalance
    
    def get_balance(self):
        return self.balance
    
    def play(self, aGame):
        self.pay_for(aGame)
        turn = aGame.play()
        calculator = self.createPrizeCalculator(turn, self, aGame)
        try:
            calculator.payout_prize()
        except AttributeError:
            print('Sorry, no prize this time.')
    
    def pay_for(self, aGame):
        if self.get_balance() < aGame.fee:
            raise InsufficientBalance('Insufficient balance to play')
        self.balance -= aGame.get_fee()
        aGame.balance += aGame.get_fee()

    def createPrizeCalculator(self, aTurn, aPlayer, aGame):
        if aGame.is_jackpot(aTurn):
            return JackpotCalculator(aTurn, aPlayer, aGame)
        elif aGame.is_one_of_each(aTurn):
            return OneOfEachCalculator(aTurn, aPlayer, aGame)
        elif aGame.is_two_in_a_row(aTurn):
            return TwoInARowCalculator(aTurn, aPlayer, aGame)

class PrizeCalculator:
    def __init__(self, aTurn, aPlayer, aGame):
        self.turn = aTurn
        self.player = aPlayer
        self.game = aGame
    
    # def payout_prize(self):
    #     self.player.balance += (self.game.get_fee() * 5)
    #     self.game.balance -= (self.game.get_fee() * 5)

class JackpotCalculator(PrizeCalculator):
    def payout_prize(self):
        self.player.balance += self.game.get_balance()
        self.game.balance = 0

class OneOfEachCalculator(PrizeCalculator):
    def payout_prize(self):
        self.player.balance += self.game.get_balance() / 2
        self.game.balance /= 2

class TwoInARowCalculator(PrizeCalculator):
    def payout_prize(self):
        self.player.balance += (self.game.get_fee() * 5)
        self.game.balance -= (self.game.get_fee() * 5)

class InsufficientBalance(ZeroDivisionError):
	def __init__(self, msg):
	    self.msg = msg