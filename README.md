# Fruit Machine

## Specification

We are going to create a virtual fruit machine. To make things easier instead of symbols we are going to use colours: black, white, green, yellow.

Each time a player plays our fruit machine we display four 'slots' each with a randomly selected colour in each slot.

If the colours in each slot are the same then the player wins the jackpot which is all of the money that is currently in the machine.

Implement a basic machine, along with the concept of a player who has a fixed amount of money to play the machine.

## Test

Clone repo
```
python3 -m pytest
```

## Design Plan

1. Display 4 colours randomly selected
2. Win condition == all four colours match 
3. `player.play(fruit_machine)` pay out jackpot (fruit machine 'balance' added to Player 'balance') when win condition met
