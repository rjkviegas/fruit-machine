class Player:  
    def __init__(self, balance):
        self.balance = balance
    
    def get_balance(self):
        return self.balance
    
    def play(self, game_machine):
        self.pay_fee_for(game_machine)
        game_machine.play(self)
    
    def pay_fee_for(self, game_machine):
        if self.get_balance() < game_machine.fee:
            raise InsufficientBalance('Insufficient balance to play')
        self.balance -= game_machine.get_fee()
        game_machine.balance += game_machine.get_fee() 

class InsufficientBalance(ZeroDivisionError):
	def __init__(self, msg):
	    self.msg = msg