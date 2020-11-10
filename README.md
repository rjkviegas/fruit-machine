# Fruit Machine

## Specification

We are going to create a virtual fruit machine. 
To make things easier instead of symbols we are going to use colours: black, white, green, yellow.

Each time a player plays our fruit machine we display four 'slots' each with a randomly selected colour in each slot.

If the colours in each slot are the same then the player wins the jackpot which is all of the money that is currently in the machine.

Implement a basic machine, along with the concept of a player who has a fixed amount of money to play the machine.

## Acceptance Criteria
No acceptance criteria was provided however I created `example.py` to illustrate how the program would work.
Below are some sample outputs of `example.py` being run:
```
white
yellow
green
green
That's two in a row!
You won 5 x the fee amount!

green
yellow
black
white
That's one of each!
You won half the machine's total float!

black
green
black
green
Sorry, no prize this time.
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
- Enjoyed refactoring and using polymorphism for the PrizeCalculator
- Pleased with overall code coverage of 98%
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
