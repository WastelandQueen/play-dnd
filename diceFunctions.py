import random

def roll(numDice, numSides, modifier=0):
    """
    x: the number of dice
    y: the number of sides
    mod: the modifier
    """
    total = 0
    for times in range(numDice):
        total += random.randint(1, numSides)

    return total + modifier
