from Player import Player
from GameMachine import GameMachine
from TurnGenerator import FourReelsTurnGenerator
from PrizeFactory import DefaultPrizeFactory


player_initial_balance = 10
game_machine_initial_balance = 100
game_machine_fee = 1

slot_opts = (
    'black',
    'white',
    'green',
    'yellow'
)

player = Player(10)
fruit_machine = GameMachine(
    slot_opts, 
    game_machine_initial_balance,
    game_machine_fee,
    TurnGenerator,
    DefaultPrizeFactory
)

print("Player intial balance: ", player.get_balance())
print("Fruit machine initial balance: ", fruit_machine.get_balance())

print("Player pays the fee and pulls the lever")
print('Slots returned are:')
player.play(fruit_machine)

print("Player new balance: ", player.get_balance())
print("Fruit machine: ", fruit_machine.get_balance())
