from Player import Player
from FruitMachine import FruitMachine
from FourReelsTurn import FourReelsTurn

slot_opts = (
    'black',
    'white',
    'green',
    'yellow'
)
player = Player(10)
fruit_machine = FruitMachine(slot_opts, 100, 1, FourReelsTurn)

player.play(fruit_machine)
