from Player import Player
from GameMachine import GameMachine
from FourReelsTurn import FourReelsTurn
from PrizeCalculatorFactory import PrizeCalculatorFactory


player_initial_balance = 10

slot_opts = (
    'black',
    'white',
    'green',
    'yellow'
)

game_machine_initial_balance = 100
game_machine_fee = 1

player = Player(10)
fruit_machine = GameMachine(
    slot_opts, 
    game_machine_initial_balance,
    game_machine_fee,
    FourReelsTurn,
    PrizeCalculatorFactory
)

print("Player intial balance: ", player.get_balance())
print("Fruit machine initial balance: ", fruit_machine.get_balance())

player.play(fruit_machine)

print("Player new balance: ", player.get_balance())
print("Fruit machine: ", fruit_machine.get_balance())
