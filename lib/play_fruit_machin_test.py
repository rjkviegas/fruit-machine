from play_fruit_machine import play_fruit_machine
from unittest import mock

@mock.patch("play_fruit_machine.choice", return_value='black', autospec=True)
def test_play_fruit_machine_returns_4_black(mock_choice):
    assert play_fruit_machine() == [
        'black',
        'black',
        'black',
        'black'
    ]

@mock.patch("play_fruit_machine.choice", return_value='white', autospec=True)
def test_play_fruit_machine_returns_4_white(mock_choice):
    assert play_fruit_machine() == [
        'white',
        'white',
        'white',
        'white'
    ]
@mock.patch("play_fruit_machine.choice", return_value='green', autospec=True)
def test_play_fruit_machine_returns_4_green(mock_choice):
    assert play_fruit_machine() == [
        'green',
        'green',
        'green',
        'green'
    ]

@mock.patch("play_fruit_machine.choice", return_value='yellow', autospec=True)
def test_play_fruit_machine_returns_4_yellow(mock_choice):
    assert play_fruit_machine() == [
        'yellow',
        'yellow',
        'yellow',
        'yellow'
    ]