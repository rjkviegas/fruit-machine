class PrizeCalculator:
    def __init__(self, player, game_machine):
        self.player = player
        self.game_machine = game_machine

class JackpotCalculator(PrizeCalculator):
    def payout_prize(self):
        print("You won all the money in the machine!")
        self.player.balance += self.game_machine.get_balance()
        self.game_machine.balance = 0

class OneOfEachCalculator(PrizeCalculator):
    def payout_prize(self):
        print("You won half the machine's total float!")
        self.player.balance += self.game_machine.get_balance() / 2
        self.game_machine.balance /= 2

class TwoInARowCalculator(PrizeCalculator):
    def payout_prize(self):
        print("You won 5 x the fee amount!")
        self.player.balance += (self.game_machine.get_fee() * 5)
        self.game_machine.balance -= (self.game_machine.get_fee() * 5)