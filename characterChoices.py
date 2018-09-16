import diceFunctions as dF

from races import *
from classes import *
from backgrounds import *

def rollStats():
# To make a new character, first roll 4d6, six times, and take the highest 3
# each time. Note that the reason this function is not in diceFunctions is that
# it will only ever be used to roll up a new character.
    scores = []
    for i in range(6):
        score = dF.roll(4,6,0,'list')   # Rolls 4d6
        score.remove(min(score))        # Removes the lowest roll
        score = sum(score)              # Sums the remaining 3 rolls
        scores.append(score)            # Adds this sum total to the list of scores
    return scores

def chooseRace():
    print("First, you will choose your race. The races include:")
    print("Dwarf (Hill, Mountain)               Elf (High, Wood, Dark)")
    print("Halfling (Lightfoot, Stout)          Human")
    print("Dragonborn                           Gnome(Forest, Rock, Deep)")
    print("Half-Elf(this one doesn't work yet)  Aarakocra")
    print("Half-Orc                             Tiefling")
    print("Genasi (Air, Earth, Fire, Water)     Goliath")

    matches_race = 0            # The number of times a race name matches a race name in the list
    submatches_race = 0         # The number of times a subrace name matches a subrace name in the list
    items_matched_race = []     # The races that match the input
    subitems_matched_race = []  # The subraces that match the input

    found = False
    while found == False:
        race_input = input("\nEnter the race you would like to play (Example: Hill Dwarf or elf): ")
        for race_name in race_names:
            if race_input.lower() in race_name.lower():
                matches_race = matches_race+1
                items_matched_race.append(race_name)
        if matches_race > 1: # More than one match is found between user input and racial possibilities
            print("\nThe race you have chosen has the following subraces: ")
            for item in items_matched_race:
                print(item)
            subrace_input = input("Which subrace would you like to play? (Example: rock gnome or Hill): ")
            for race_name in items_matched_race:
                if subrace_input.lower() in race_name.lower():
                    submatches_race = submatches_race+1
                    subitems_matched_race.append(race_name)
            if submatches_race == 1:
                print("You have chosen to play a(n) " + subitems_matched_race[0] + ".\n")
                chosen_race = subitems_matched_race[0]
                found = True
            else:
                print("Please try again.\n")
        elif matches_race == 1: # Exactly one match is found between user input and racial possibilities
            print("You have chosen to play a(n) " + items_matched_race[0] + ".\n")
            chosen_race = items_matched_race[0]
            found = True
        else: # No matches_race found between user input and racial possibilities
            print("Please try again.\n")

    # The following section finds the index of the chosen race in the list of races
    # found in races. This is to get the actual race ID (for instance,
    # Dwarf_Hill) for use with Race methods.
    # Note that chosen_race is the NAME of the race chosen and char_race refers to
    # the OBJECT INDENTIFIER of that race.
    i = 0
    for race in race_list:
        if chosen_race == race.name:
            index = i
        i = i+1
    char_race = race_list[index]

    char_race.displayDetails()
    return char_race

def chooseClass():
    print("Choose your class. The classes include:")
    print("Barbarian        Bard            Cleric")
    print("Druid            Fighter         Monk")
    print("Paladin          Ranger          Rogue")
    print("Sorcerer         Warlock         Wizard")
    class_found = False
    while class_found == False:
        class_input = input("\nEnter the class you would like to play (Example: monk or Wizard): ")
        for class_name in class_names:
            if class_input.lower() in class_name.lower():
                chosen_class = class_name
                class_found = True

    print("You have chosen to play a(n) " + chosen_class + ".\n")
    # The following section finds the index of the chosen class in the list of
    # classes found in classes. This is to get the actual class ID (for instance,
    # Cleric) for use with Class methods.
    # Note that chosen_class is the NAME of the race chosen and char_class refers to
    # the OBJECT INDENTIFIER of that race.
    i = 0
    for class_name in class_list:
        if chosen_class == class_name.name:
            index = i
        i = i+1
    char_class = class_list[index]

    char_class.displayDetails()
    return char_class

def chooseBackground():
    print("Choose a background for your character. The backgrounds include:")
    print("Acolyte          Charlatan           Criminal        Entertainer")
    print("Folk Hero        Guild Artisan       Hermit          Noble")
    print("Outlander        Sage                Sailor          Soldier")
    print("Urchin")

    found = False
    while found == False:
        background_input = input("\nEnter the background you have chosen for your character: ")
        for background in background_names:
            if background_input.lower() in background.lower():
                chosen_background = background
                found = True

    i = 0
    for background in background_list:
        if chosen_background == background.name:
            index = i
        i = i+1
    char_background = background_list[index]

    char_background.displayDetails()
    return char_background

def makeScoresString(char_scores):
    scores_string = ""
    for score in char_scores:
        scores_string = scores_string + str(score) + " "
    return scores_string

def allocateScores(scores_string, char_scores):
    i = 0
    char_scores_allocated = []
    ability_scores_string = [ "STR", "DEX", "CON", "INT", "WIS", "CHA" ]
    while i < 6:
        if i == 0:  # display all scores
            scores_string = makeScoresString(char_scores)
            print("\nHere are your scores: " + scores_string)
            value = int(input("Which score value would you like to put in " + ability_scores_string[i] + "?: "))
            if value in char_scores:
                char_scores_allocated = char_scores_allocated + [value]
                char_scores.remove(value)
                i = i+1
            else:
                print("You must enter a valid remaining roll. Try again.\n")
        elif i < 5: # display remaining scores
            scores_string = makeScoresString(char_scores)
            print("\nRolls remaining: " + scores_string)
            value = int(input("Which score value would you like to put in " + ability_scores_string[i] + "?: "))
            if value in char_scores:
                char_scores_allocated = char_scores_allocated + [value]
                char_scores.remove(value)
                i = i+1
            else:
                print("You must enter a valid remaining roll. Try again.\n")
        else:       # i == 5: don't display any remaining scores (there's only one) just allocate it to wis
            scores_string = makeScoresString(char_scores)
            print("\nYour final score of " + scores_string + " will be allocated to CHA.")
            char_scores_allocated = char_scores_allocated + [char_scores[0]]
            char_scores.remove(char_scores[0]) # this line really isn't necessary, but what the hell
            i = i+1
    return char_scores_allocated

def determineScores(char_race, char_class):
    print("Now, determine your ability scores. The six ability scores include: ")
    print("STR - Strength           INT - Intelligence")
    print("DEX - Dexterity          WIS - Wisdom")
    print("CON - Constitution       CHA - Charisma\n")

    # Roll scores, with option to reroll if user is unhappy with rolls.
    # TODO: Add a limit to this. Maybe only allow the user three rolls total.
    while True:
        char_scores = rollStats()
        char_scores.sort(reverse=True)
        scores_string = makeScoresString(char_scores)
        print("You rolled the following scores: " + scores_string)
        cond = input("Would you like to reroll (y/n)?: ")
        if cond.lower() == "y":
            print("Rerolling...\n")
        elif cond.lower() == "n":
            break
        else:
            print("Input not recognised. Rerolling scores.")
    print("")

    ability_scores_string = [ "STR", "DEX", "CON", "INT", "WIS", "CHA" ]
    race_score_modifiers = char_race.getScores()
    char_scores_allocated = allocateScores(scores_string, char_scores)
    final_scores = []

    print("\nYour " + char_race.name + " " + char_class.name + "'s final scores are as follows:")
    for i in range(6):
        final_scores.append(race_score_modifiers[i] + char_scores_allocated[i]) # Adds racial bonuses to rolled scores.
        print("     " + ability_scores_string[i] + ": " + str(final_scores[i]))
    print("\n\n")
    return final_scores
