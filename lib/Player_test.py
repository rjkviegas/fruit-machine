from Player import Player, InsufficientBalance
from FruitMachine import FruitMachine
from FourReelsTurn import FourReelsTurn
import pytest, random

slot_options = ('test')
fm_float = 100
fee = 1
player_init_balance = 5

def test_when_no_prize_won(monkeypatch):
    def return_none(x, y, z):
        return None

    player = Player(player_init_balance)
    fruit_machine = FruitMachine(slot_options, fm_float, fee, FourReelsTurn)
    assert fruit_machine.get_balance() == fm_float
    assert player.get_balance() == player_init_balance

    monkeypatch.setattr(player, 'createPrizeCalculator', return_none)
    player.play(fruit_machine)
    assert fruit_machine.get_balance() == fm_float + fee
    assert player.get_balance() == player_init_balance - fee

def test_player_raise_insuffcient_funds_error():
    with pytest.raises(InsufficientBalance):
        player = Player(0)
        fruit_machine = FruitMachine(slot_options, fm_float, fee, FourReelsTurn)

        player.play(fruit_machine)

def test_jackpot_payout(monkeypatch):
    def return_black(x):
        return 'black'

    player = Player(player_init_balance)
    fruit_machine = FruitMachine(slot_options, fm_float, fee, FourReelsTurn)
    assert fruit_machine.get_balance() == fm_float
    assert player.get_balance() == player_init_balance

    monkeypatch.setattr(random, 'choice', return_black)
    player.play(fruit_machine)
    assert fruit_machine.get_balance() == 0
    assert player.get_balance() == player_init_balance + fm_float

def test_one_of_each_payout():
    class MockFourReelsTurn:
        def __init__(self, x):
            pass
        def get_slots(self):
            return (),
        def is_jackpot(self):
            return False
        def is_one_of_each(self):
            return True

    player = Player(player_init_balance)
    fruit_machine = FruitMachine(slot_options, fm_float, fee, MockFourReelsTurn)
    assert fruit_machine.get_balance() == fm_float
    assert player.get_balance() == player_init_balance

    player.play(fruit_machine)
    assert fruit_machine.get_balance() == (fm_float + fee) / 2
    assert player.get_balance() == player_init_balance - fee + ((fm_float + fee) / 2)

def test_two_in_a_row_payout():
    class MockFourReelsTurn:
        def __init__(self, x):
            pass
        def get_slots(self):
            return (),
        def is_jackpot(self):
            return False
        def is_one_of_each(self):
            return False
        def is_two_in_a_row(self):
            return True

    player = Player(player_init_balance)
    fruit_machine = FruitMachine(slot_options, fm_float, fee, MockFourReelsTurn)
    assert fruit_machine.get_balance() == fm_float
    assert player.get_balance() == player_init_balance

    player.play(fruit_machine)
    assert fruit_machine.get_balance() == (fm_float + fee) - (fee * 5)
    assert player.get_balance() == player_init_balance - fee + (fee * 5)  