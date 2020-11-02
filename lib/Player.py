class InsufficientBalance(ZeroDivisionError):
	def __init__(self,arg):
	    self.msg = arg

class Player:
    
    def __init__(self, balance):
        self.balance = balance
    
    def get_balance(self):
        return self.balance
    
    def play(self, game):
        self.pay_for(game)
        if game.is_winner(game.play()):
            self.balance += game.balance
            game.balance = 0
    
    def pay_for(self, game):
        if self.get_balance() < game.fee:
            raise InsufficientBalance('Insufficient balance to play')
        self.balance -= game.fee
        game.balance += game.fee
