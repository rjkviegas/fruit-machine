from FourReelsTurn import FourReelsTurn
import random

slot_opts = (
    'black',
    'white',
    'green',
    'yellow'
)

def test_turn_returns_same_slot_when_random_choice_mocked(monkeypatch):
    def mock_choice(x):
        return slot_opts[0]

    monkeypatch.setattr(random, 'choice', mock_choice)
    x = FourReelsTurn(slot_opts).get_slots()
    assert x == (
            slot_opts[0],
            slot_opts[0],
            slot_opts[0],
            slot_opts[0]
        )
