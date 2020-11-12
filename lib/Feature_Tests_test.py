from Player import Player, InsufficientBalance
from GameMachine import GameMachine
from FourReelsTurn import FourReelsTurn
from PrizeFactory import DefaultPrizeFactory
import pytest, random

slot_options = ('test')
game_machine_float = 100
game_fee = 1
player_initial_balance = 5

def test_no_prize_scenario(monkeypatch):
    def losing_slots_combination(x, y, z):
        return None

    player = Player(player_initial_balance)

    fruit_machine = GameMachine(
        slot_options,
        game_machine_float,
        game_fee,
        FourReelsTurn,
        DefaultPrizeFactory
    )

    assert fruit_machine.get_balance() == game_machine_float
    assert player.get_balance() == player_initial_balance

    monkeypatch.setattr(
        fruit_machine.prize_calculator_factory,
        'create_prize_calculator',
        losing_slots_combination
    )
    player.play(fruit_machine)

    assert fruit_machine.get_balance() == game_machine_float + game_fee
    assert player.get_balance() == player_initial_balance - game_fee

def test_player_has_insuffcient_funds_to_play():
    with pytest.raises(InsufficientBalance):

        player_with_sufficient_funds = Player(0)

        fruit_machine = GameMachine(
            slot_options,
            game_machine_float,
            game_fee,
            FourReelsTurn,
            DefaultPrizeFactory
        )

        assert player_with_sufficient_funds.get_balance() < fruit_machine.get_fee()
        player_with_sufficient_funds.play(fruit_machine)

def test_jackpot_prize_payout(monkeypatch):
    def return_black(x):
        return 'black'

    player = Player(player_initial_balance)

    fruit_machine = GameMachine(
        slot_options,
        game_machine_float,
        game_fee,
        FourReelsTurn,
        DefaultPrizeFactory
    )

    assert fruit_machine.get_balance() == game_machine_float
    assert player.get_balance() == player_initial_balance

    monkeypatch.setattr(random, 'choice', return_black)
    player.play(fruit_machine)

    assert fruit_machine.get_balance() == 0
    assert player.get_balance() == player_initial_balance + game_machine_float

def test_one_of_each_prize_payout(monkeypatch):
    def return_false(x):
        return False
    
    def return_true(x):
        return True

    player = Player(player_initial_balance)

    fruit_machine = GameMachine(
        slot_options,
        game_machine_float,
        game_fee,
        FourReelsTurn,
        DefaultPrizeFactory
    )

    assert fruit_machine.get_balance() == game_machine_float
    assert player.get_balance() == player_initial_balance

    monkeypatch.setattr(fruit_machine.prize_calculator_factory, 'is_jackpot', return_false)
    monkeypatch.setattr(fruit_machine.prize_calculator_factory, 'is_one_of_each', return_true)

    player.play(fruit_machine)

    assert fruit_machine.get_balance() == (game_machine_float + game_fee) / 2
    assert player.get_balance() == player_initial_balance - game_fee + ((game_machine_float + game_fee) / 2)

def test_two_in_a_row_prize_payout(monkeypatch):
    def return_false(x):
        return False
    
    def return_true(x):
        return True

    player = Player(player_initial_balance)
    fruit_machine = GameMachine(
        slot_options,
        game_machine_float,
        game_fee, 
        FourReelsTurn,
        DefaultPrizeFactory
    )

    assert fruit_machine.get_balance() == game_machine_float
    assert player.get_balance() == player_initial_balance

    monkeypatch.setattr(fruit_machine.prize_calculator_factory, 'is_jackpot', return_false)
    monkeypatch.setattr(fruit_machine.prize_calculator_factory, 'is_one_of_each', return_false)
    monkeypatch.setattr(fruit_machine.prize_calculator_factory, 'is_two_in_a_row', return_true)

    player.play(fruit_machine)
    
    assert fruit_machine.get_balance() == (game_machine_float + game_fee) - (game_fee * 5)
    assert player.get_balance() == player_initial_balance - game_fee + (game_fee * 5)  