class character:
    def __init__(character, name, race, char_class, lvl, alignment, ability_scores, skill_proficiencies):
        character.name = name
        character.race = race
        character.char_class = char_class
        character.lvl = lvl                                 # will need to be converted into a string for printing
        character.alignment = alignment
        character.ability_scores = ability_scores           # will need to be converted into a string for printing
        character.skill_proficiencies = skill_proficiencies # will be a list of strings

    def displayCharacter(char):
        print("CHARACTER DETAILS:")
        print("\nNAME:\t\t" + char.name)
        print("RACE:\t\t" + char.race)
        print("CLASS:\t\t" + char.char_class)
        print("LEVEL:\t\t" + char.lvl)
        print("ALIGNMENT:\t" + char.alignment)
        print("\nSTAT\tSCORE\tMOD\n----\t-----\t---")
        index = 0
        ability_scores_string = [ "STR", "DEX", "CON", "INT", "CHA", "WIS" ]
        for score in char.ability_scores:
            if ((score-10)/2) > 0:
                print(ability_scores_string[index] + ":\t" + str(score) + "\t+" + str((score-10)/2))
                index = index + 1
            else:
                print(ability_scores_string[index] + ":\t" + str(score) + "\t" + str((score-10)/2))
                index = index + 1
        print("\nSKILL PROFICIENCIES\n-------------------")
        counter = 1
        for skill in char.skill_proficiencies:
            print("(" + str(counter) + ") " + skill)
            counter = counter + 1
        print("\n")

Tiffany = character("Tiffany", "Human", "Bard", "1", "NG", [9,12,13,14,15,16], ["Perception","Intimidation"])
Tiffany.displayCharacter()
