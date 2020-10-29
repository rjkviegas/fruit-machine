from random import choice

def play_fruit_machine():
    slots = (
        'black',
        'white',
        'green',
        'yellow'
    )
    return [
        choice(slots),
        choice(slots),
        choice(slots),
        choice(slots)
    ]