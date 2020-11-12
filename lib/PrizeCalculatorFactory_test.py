from PrizeCalculatorFactory import PrizeCalculatorFactory

prizeCalculatorFactory = PrizeCalculatorFactory()

def test_is_jackpot_when_slots_all_same_option(monkeypatch):
    jackpot = ('black',) *4
    
    assert prizeCalculatorFactory.is_jackpot(jackpot) == True

def test_is_one_of_each_when_each_slot_option_once(monkeypatch):
    one_of_each = (
        'black',
        'white',
        'green',
        'yellow'
    )

    assert prizeCalculatorFactory.is_one_of_each(one_of_each) == True

def test_is_two_in_a_row(monkeypatch):
    two_in_a_row = (
        'green',
        'yellow',
        'black',
        'black'
    )

    assert prizeCalculatorFactory.is_two_in_a_row(two_in_a_row) == True

