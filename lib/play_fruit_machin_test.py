from play_fruit_machine import play_fruit_machine, is_winner
from unittest import mock

@mock.patch("play_fruit_machine.choice", return_value='black', autospec=True)
def test_play_fruit_machine_returns_4_black(mock_choice):
    assert play_fruit_machine() == (
        'black',
        'black',
        'black',
        'black'
    )

@mock.patch("play_fruit_machine.choice", return_value='white', autospec=True)
def test_play_fruit_machine_returns_4_white(mock_choice):
    assert play_fruit_machine() == (
        'white',
        'white',
        'white',
        'white'
    )

@mock.patch("play_fruit_machine.choice", return_value='green', autospec=True)
def test_play_fruit_machine_returns_4_green(mock_choice):
    assert play_fruit_machine() == (
        'green',
        'green',
        'green',
        'green'
    )

@mock.patch("play_fruit_machine.choice", return_value='yellow', autospec=True)
def test_play_fruit_machine_returns_4_yellow(mock_choice):
    assert play_fruit_machine() == (
        'yellow',
        'yellow',
        'yellow',
        'yellow'
    )

def test_is_winner_when_slot_all_black():
    all_black = (
        'black',
        'black',
        'black',
        'black'
    )
    assert is_winner(all_black) == True

def test_is_winner_when_slot_all_white():
    all_white = (
        'white',
        'white',
        'white',
        'white'
    )
    assert is_winner(all_white) == True
