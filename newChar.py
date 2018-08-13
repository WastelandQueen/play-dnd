import diceFunctions as dF
from races import *

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

# Begin main program
print("\n\nHello! Let's make a new character. First, you will choose your race. The races are:")
print("Dwarf (Hill or Mountain)             Elf (High, Wood, Dark)")
print("Halfling (Lightfoot, Stout)          Human")
print("Dragonborn                           Gnome(Forest, Rock, Deep)")
print("Half-Orc                             Tiefling")
print("Genasi (Air, Earth, Fire, Water)     Goliath")

matches = 0             # The number of times a race name matches a race name in the list
submatches = 0          # The number of times a subrace name matches a subrace name in the list
items_matched = []      # The races that match the input
ids_matched = []        # The object identity of the races that match the input
subitems_matched = []   # The subraces that match the input
race_input = raw_input("\nEnter the race you would like to play (Example: Hill Dwarf or elf): ")
for race_name in race_names:
    if race_input.lower() in race_name.lower():
        matches = matches+1
        items_matched.append(race_name)
if matches > 1:
    print("\nThe race you have chosen has the following subraces: ")
    for item in items_matched:
        print(item)
    subrace_input = raw_input("Which subrace would you like to play? (Example: rock gnome or Hill): ")
    for race_name in items_matched:
        if subrace_input.lower() in race_name.lower():
            submatches = submatches+1
            subitems_matched.append(race_name)
    if submatches == 1:
        print("You have chosen to play a(n) " + subitems_matched[0] + ".\n")
        chosen_race = subitems_matched[0]
    else:
        print("Please try again.\n")
elif matches == 1:
    print("You have chosen to play a(n) " + items_matched[0] + ".\n")
    chosen_race = items_matched[0]
else:
    print("Please try again.\n")

# chosen_race.displayDetails()  BUGGER ALL THIS I CAN'T FIGURE THIS PART OUT
