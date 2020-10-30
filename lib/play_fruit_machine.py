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
        ),
        (
            'green',
            'green',
            'green',
            'green'
        ),
        (
            'yellow',
            'yellow',
            'yellow',
            'yellow'
        )

    )
    return True if slots in win_combs else False

