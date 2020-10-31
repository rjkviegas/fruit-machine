class Player:
    
    def __init__(self, balance):
        self.balance = balance
    
    def play(self, game):
        self.pay_for(game)
        if game.is_winner(game.play()):
            self.balance += game.balance
            game.balance = 0
    
    def pay_for(self, game):
        self.balance -= game.fee
        game.balance += game.fee

