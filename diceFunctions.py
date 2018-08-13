import random

def roll(numDice, numSides, modifier=0, total='sum'):
# When rolling, specify the number of dice, the sides on the dice, what modifier
# and whether the sum total or a list of rolls is desired.
    sumtotal = 0
    scores = []
    if total == 'sum':
        for times in range(numDice):
            sumtotal += random.randint(1, numSides)
        print('end')
        return sumtotal + modifier
    elif total == 'list':
        for times in range(numDice):
            scores.append(random.randint(1, numSides) + modifier)
        return scores

def rollStats():
# To make a new character, first roll 4d6, six times, and take the highest 3
# each time.
    scores = []
    for i in range(6):
        score = roll(4,6,0,'list')  # Rolls 4d6
        score.remove(min(score))    # Removes the lowest roll
        score = sum(score)          # Sums the remaining 3 rolls
        scores.append(score)        # Adds this sum total to the list of scores
    return scores
