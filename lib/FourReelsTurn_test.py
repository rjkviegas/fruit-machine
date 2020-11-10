from FourReelsTurn import FourReelsTurn
import random

slot_opts = (
    'black',
    'white',
    'green',
    'yellow'
)

turn = FourReelsTurn(slot_opts, 4)

def test_turn_returns_same_slot_when_random_choice_mocked(monkeypatch):
    def mock_choice(x):
        return slot_opts[0]

    monkeypatch.setattr(random, 'choice', mock_choice)
    x = FourReelsTurn(slot_opts, 4).get_slots()
    assert x == (
            slot_opts[0],
            slot_opts[0],
            slot_opts[0],
            slot_opts[0]
        )

def test_turn_is_last_slot():
    index_of_last_slot = len(turn.get_slots()) - 1
    assert turn.is_last_slot(index_of_last_slot) == True

def test_is_jackpot_when_slots_all_same_option(monkeypatch):
    def mock_get_slots():
        return (slot_opts[0],) * 4
    
    monkeypatch.setattr(turn, 'get_slots', mock_get_slots)
    assert turn.is_jackpot() == True

def test_is_one_of_each_when_each_slot_option_once(monkeypatch):
    def mock_get_slots():
        return (
        'black',
        'white',
        'green',
        'yellow'
    )

    monkeypatch.setattr(turn, 'get_slots', mock_get_slots)
    assert turn.is_one_of_each() == True

def test_is_two_in_a_row(monkeypatch):
    def mock_get_slots():
        return (
        'green',
        'yellow',
        'black',
        'black'
    )

    monkeypatch.setattr(turn, 'get_slots', mock_get_slots)
    assert turn.is_two_in_a_row() == True

