from random import choice

def play_fruit_machine():
    slots = (
        'black',
        'white',
        'green',
        'yellow'
    )
    return (
        choice(slots),
        choice(slots),
        choice(slots),
        choice(slots)
    )

def is_winner(slots):
    win_combs = (
        (
            'black',
            'black',
            'black',
            'black'
        ),
        (
            'white',
            'white',
            'white',
            'white'
        )
    )
    if slots in win_combs:
        return True
    else:
        return False
