from Player import Player
from FruitMachine import FruitMachine
import random

slot_options = ('test')
fm_float = 100
fee = 1
player_init_balance = 5


def test_player_play_fruit_machine_win(monkeypatch):
    def always_win(x):
        return True

    player = Player(player_init_balance)
    fruit_machine = FruitMachine(slot_options, fm_float, fee)
    assert fruit_machine.balance == fm_float
    assert player.balance == player_init_balance

    monkeypatch.setattr(fruit_machine, 'is_winner', always_win)
    player.play(fruit_machine)
    assert fruit_machine.balance == 0
    assert player.balance == player_init_balance + fm_float

def test_player_play_fruit_machine_lose(monkeypatch):
    def always_lose(x):
        return False

    player = Player(player_init_balance)
    fruit_machine = FruitMachine(slot_options, fm_float, fee)
    assert fruit_machine.balance == fm_float
    assert player.balance == player_init_balance

    monkeypatch.setattr(fruit_machine, 'is_winner', always_lose)
    player.play(fruit_machine)
    assert fruit_machine.balance == fm_float + fee
    assert player.balance == player_init_balance - fee