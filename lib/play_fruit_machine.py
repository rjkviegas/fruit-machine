from random import randint

def play_fruit_machine():
    slots_dict = { 0: 'black', 1: 'white' }
    return [
        slots_dict[randint(0, 1)],
        slots_dict[randint(0, 1)],
        slots_dict[randint(0, 1)],
        slots_dict[randint(0, 1)]
    ]