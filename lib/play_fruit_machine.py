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
    return slots == (
        'black',
        'black',
        'black',
        'black'
    )