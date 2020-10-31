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
3. Fruit machine pays out jackpot (total float) when win condition met
4. Fee to play game
5. More win conditions prize outcomes
   * If each slot has a different colour then the machine should pay out half the current money in the machine.
   * If a given play results in two or more adjacent slots containing the same colour then the machine should pay out a prize of 5 times the cost of a single play.
   * If the machine does not have enought money to pay a prize it should credit the player with a number of free plays equal to the difference between the full prize and the amount of money available. This does not affect a jackpot win.
