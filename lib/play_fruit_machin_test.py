from play_fruit_machine import play_fruit_machine
from unittest import mock

@mock.patch("play_fruit_machine.randint", return_value=0, autospec=True)
def test_play_fruit_machine_returns_4_black(mock_randint):
    assert play_fruit_machine() == [
        'black',
        'black',
        'black',
        'black'
    ]

@mock.patch("play_fruit_machine.randint", return_value=1, autospec=True)
def test_play_fruit_machine_returns_4_white(mock_randint):
    assert play_fruit_machine() == [
        'white',
        'white',
        'white',
        'white'
    ]