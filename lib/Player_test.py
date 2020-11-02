from Player import Player, InsufficientBalance
from FruitMachine import FruitMachine
import pytest, random

slot_options = ('test')
fm_float = 100
fee = 1
player_init_balance = 5


def test_player_play_fruit_machine_jackpot(monkeypatch):
    def always_win(x):
        return True

    player = Player(player_init_balance)
    fruit_machine = FruitMachine(slot_options, fm_float, fee)
    assert fruit_machine.get_balance() == fm_float
    assert player.get_balance() == player_init_balance

    monkeypatch.setattr(fruit_machine, 'is_jackpot', always_win)
    player.play(fruit_machine)
    assert fruit_machine.get_balance() == 0
    assert player.get_balance() == player_init_balance + fm_float

def test_player_play_fruit_machine_lose(monkeypatch):
    def return_none(x, y, z):
        return None

    player = Player(player_init_balance)
    fruit_machine = FruitMachine(slot_options, fm_float, fee)
    assert fruit_machine.get_balance() == fm_float
    assert player.get_balance() == player_init_balance

    monkeypatch.setattr(player, 'createPrizeCalculator', return_none)
    player.play(fruit_machine)
    assert fruit_machine.get_balance() == fm_float + fee
    assert player.get_balance() == player_init_balance - fee

def test_player_raise_insuffcient_funds_error():
    with pytest.raises(InsufficientBalance):
        player = Player(0)
        fruit_machine = FruitMachine(slot_options, fm_float, fee)

        player.play(fruit_machine)

def test_player_play_fruit_machine_one_of_each(monkeypatch):
    def always_win(x):
        return True

    def not_jackpot(x):
        return False

    player = Player(player_init_balance)
    fruit_machine = FruitMachine(slot_options, fm_float, fee)
    assert fruit_machine.get_balance() == fm_float
    assert player.get_balance() == player_init_balance
    monkeypatch.setattr(fruit_machine, 'is_jackpot', not_jackpot)
    monkeypatch.setattr(fruit_machine, 'is_one_of_each', always_win)
    player.play(fruit_machine)
    assert fruit_machine.get_balance() == (fm_float + fee) / 2
    assert player.get_balance() == player_init_balance - fee + ((fm_float + fee) / 2) 