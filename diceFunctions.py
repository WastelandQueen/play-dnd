import random

def roll(numDice, numSides, modifier=0, total='sum'):
# When rolling, specify the number of dice, the sides on the dice, what modifier
# and whether the sum total or a list of rolls is desired.
    sumtotal = 0
    scores = []
    if total == 'sum':
        for times in range(numDice):
            sumtotal += random.randint(1, numSides)
        return sumtotal + modifier
    elif total == 'list':
        for times in range(numDice):
            scores.append(random.randint(1, numSides) + modifier)
        return scores
