class Prize:
    def __init__(self, player, game_machine):
        self.player = player
        self.game_machine = game_machine

class JackpotPrize(Prize):
    def payout_to_player(self):
        self.player.balance += self.game_machine.get_balance()
        self.game_machine.balance = 0
        print("You won all the money in the machine!")

class OneOfEachPrize(Prize):
    def payout_to_player(self):
        self.player.balance += self.game_machine.get_balance() /2
        self.game_machine.balance /= 2
        print("You won half the machine's total float!")

class TwoInARowPrize(Prize):
    def payout_to_player(self):
        self.player.balance += (self.game_machine.get_fee() *5)
        self.game_machine.balance -= (self.game_machine.get_fee() *5)
        print("You won 5 x the fee amount!")