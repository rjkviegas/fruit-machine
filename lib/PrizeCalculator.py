class PrizeCalculator:
    def __init__(self, turn, player, game):
        self.turn = turn
        self.player = player
        self.game = game

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