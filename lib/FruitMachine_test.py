from FruitMachine import FruitMachine
import random

slot_opts = (
    'black',
    'white',
    'green',
    'yellow'
)

fruit_machine = FruitMachine(slot_opts, 100, 1)

def test_play_returns_4_black(monkeypatch):
    def mockchoice(x):
        return 'black'

    monkeypatch.setattr(random, 'choice', mockchoice)
    x = fruit_machine.play()
    assert x == (
            'black',
            'black',
            'black',
            'black'
        )

def test_play_returns_4_white(monkeypatch):
    def mockchoice(x):
        return 'white'

    monkeypatch.setattr(random, 'choice', mockchoice)
    x = fruit_machine.play()
    assert x == (
            'white',
            'white',
            'white',
            'white'
        )

def test_play_returns_4_green(monkeypatch):
    def mockchoice(x):
        return 'green'

    monkeypatch.setattr(random, 'choice', mockchoice)
    x = fruit_machine.play()
    assert x == (
        'green',
        'green',
        'green',
        'green'
    )

def test_play_returns_4_yellow(monkeypatch):
    def mockchoice(x):
        return 'yellow'

    monkeypatch.setattr(random, 'choice', mockchoice)
    x = fruit_machine.play()
    assert x == (
        'yellow',
        'yellow',
        'yellow',
        'yellow'
    )

def test_is_winner_when_slots_all_black():
    all_black = (
        'black',
        'black',
        'black',
        'black'
    )
    assert fruit_machine.is_winner(all_black) == True

def test_is_winner_when_slots_all_white():
    all_white = (
        'white',
        'white',
        'white',
        'white'
    )
    assert fruit_machine.is_winner(all_white) == True

def test_is_winner_when_slots_all_green():
    all_green =  (
        'green',
        'green',
        'green',
        'green'
    )
    assert fruit_machine.is_winner(all_green) == True

def test_is_winner_when_slots_all_yellow():
    all_yellow = (
        'yellow',
        'yellow',
        'yellow',
        'yellow'
    )
    assert fruit_machine.is_winner(all_yellow) == True

def test_is_winner_when_each_slot_option_once():
    one_each = (
        'black',
        'white',
        'green',
        'yellow'
    )
    assert fruit_machine.is_winner(one_each) == True

def test_one_of_each():
    one_each = (
        'black',
        'white',
        'green',
        'yellow'
    )
    assert fruit_machine.one_of_each(one_each) == True

