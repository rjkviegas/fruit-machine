from PrizeFactory import DefaultPrizeFactory

prize_factory = DefaultPrizeFactory()

def test_is_jackpot_when_slots_all_same_option(monkeypatch):
    jackpot = ('black',) *4
    
    assert prize_factory.is_jackpot(jackpot) == True

def test_is_one_of_each_when_each_slot_option_once(monkeypatch):
    one_of_each = (
        'black',
        'white',
        'green',
        'yellow'
    )

    assert prize_factory.is_one_of_each(one_of_each) == True

def test_is_two_in_a_row(monkeypatch):
    two_in_a_row = (
        'green',
        'yellow',
        'black',
        'black'
    )

    assert prize_factory.is_two_in_a_row(two_in_a_row) == True

