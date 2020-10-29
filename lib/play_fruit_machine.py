from random import randint

def play_fruit_machine():
    slots_dict = { 0: 'black', 1: 'white' }
    slot_key = randint(0, 1)
    return [
        slots_dict[slot_key],
        slots_dict[slot_key],
        slots_dict[slot_key],
        slots_dict[slot_key]
    ]