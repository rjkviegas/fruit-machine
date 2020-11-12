# Fruit Machine

## Specification

We are going to create a virtual fruit machine. 
To make things easier instead of symbols we are going to use colours: black, white, green, yellow.

Each time a player plays our fruit machine we display four 'slots' each with a randomly selected colour in each slot.

If the colours in each slot are the same then the player wins the jackpot which is all of the money that is currently in the machine.

Implement a basic machine, along with the concept of a player who has a fixed amount of money to play the machine.

## Acceptance Criteria
No acceptance criteria was provided however I created `example.py` to illustrate how the program would work.
Below are some outputs from running `example.py`:
```
Player intial balance:  10
Fruit machine initial balance:  100
Player pays the fee and pulls the lever
Slots returned are:
[ 'white', 'white', 'white', 'white' ]
You hit the jackpot!
You won all the money in the machine!
Player new balance:  110
Fruit machine:  0

Player intial balance:  10
Fruit machine initial balance:  100
Player pays the fee and pulls the lever
Slots returned are:
[ 'green', 'yellow', 'yellow', 'yellow' ]
That's two in a row!
You won 5 x the fee amount!
Player new balance:  14
Fruit machine:  96

Player intial balance:  10
Fruit machine initial balance:  100
Player pays the fee and pulls the lever
Slots returned are:
[ 'green', 'white', 'yellow', 'black' ]
That's one of each!
You won half the machine's total float!
Player new balance:  59.5
Fruit machine:  50.5

Player intial balance:  10
Fruit machine initial balance:  100
Player pays the fee and pulls the lever
Slots returned are:
[ 'black', 'yellow', 'white', 'yellow' ]
Sorry, no prize this time.
Player new balance:  9
Fruit machine:  101
```

## Testing

Clone repo
```
python3 -m pytest
# with coverage
python3 -m pytest --cov lib/
```
## Notes
- Overall I have enjoyed my first experience using Python
- Enjoyed refactoring, using polymorphism and a Factory Method for the PrizeCalculatorprize calculaton
- Pleased with overall code coverage of 90+%
- Enjoyed using recursive calls for checking the win conditions
- Enjoyed using `super` in constructor in FourReelsTurn class

## Design Plan

1. Display 4 colours randomly selected 
2. Fruit machine pays out jackpot (total float) when all four colours match
3. Fee to play game deducted from player
4. More win conditions and prize outcomes:
   * If each slot has a different colour then the machine should pay out half the current money in the machine.
   * If a given play results in two or more adjacent slots containing the same colour then the machine should pay out a prize of 5 times the cost of a single play.

## TO DO
   * If the machine does not have enought money to pay a prize it should credit the player with a number of free plays equal to the difference between the full prize and the amount of money available. This does not affect a jackpot win.
