import diceFunctions as dF
import characterChoices as cC

from races import *
#from classes import *
from backgrounds import *

def printPretty(num, pretty_options):
    # This prints the options in a two columns
    i = 0
    while i < num:
        if num % 2 == 0 or i != num-1:
            print(pretty_options[i] + "    " + pretty_options[i+1])
        else:
            print(pretty_options[i])
        i = i+2
    print("\n")

class CharClass:
    def __init__(class_object, name, hit_die, prime_ability, save_throw1, save_throw2, pick_num, skill_prof_options, proficiencies):
        class_object.name = name
        class_object.hit_die = hit_die
        class_object.prime_ability = prime_ability
        class_object.save_throw1 = save_throw1
        class_object.save_throw2 = save_throw2
        class_object.pick_num = pick_num
        class_object.skill_prof_options = skill_prof_options
        class_object.proficiencies = proficiencies

    def pickSomeProficiencies(a_class,a_background):
        all_skills_list_pretty = ["Animal Handling    ", "Athletics          ", "Intimidation       ", "Nature             ", "Perception         ", "Survival           ", "History            ", "Insight            ", "Medicine           ", "Persuasion         ", "Religion           ", "Arcana             ", "Acrobatics         ", "Stealth            ", "Investigation      ", "Deception          ", "Performance        ", "Sleight of Hand    "]

        print("Your background (" + a_background.name + ") grants you the following proficiencies: ")
        print("(1) " + a_background.proficiency1)
        print("(2) " + a_background.proficiency2)

        print("\nChoose " + str(a_class.pick_num) + " additional skill proficiencies from the following list:")

        # need to print all skill options from class options, but remove back-
        # ground-given proficiencies and then allow user to choose from that
        # list

        options_list = []

        for skill in a_class.skill_prof_options:
            if skill not in a_background.proficiency1 and skill not in a_background.proficiency2:
                options_list.append(skill)

        pretty_options_list = []

        # Creates a string of skills
        for pretty_skill in all_skills_list_pretty:
            for skill in options_list:
                if skill in pretty_skill:
                    pretty_options_list.append(pretty_skill)

        printPretty(len(pretty_options_list), pretty_options_list)

        j = 0
        st_nd_rd_th = ["1st", "2nd", "3rd", "4th"]
        skill_proficiencies = [a_background.proficiency1, a_background.proficiency2]
        class_options = a_class.skill_prof_options

        while j < a_class.pick_num:
            found = False
            while found == False:
                # If the input skill matches a valid skill option, set it as the
                # first proficiency choice and update the j counter and go to the
                # next iteration of the loop
                index = 0
                skill = input("Enter your " + st_nd_rd_th[j] + " skill proficiency choice: ")
                for option in class_options:
                    if skill.lower() == option.lower():
                        skill_proficiencies.append(option)
                        class_options.remove(option) # Need to only allow the skill to be chosen once
                        for pretty_skill in all_skills_list_pretty:
                            if skill in pretty_skill:
                                pretty_options_list.remove(pretty_skill)
                        found = True
                        j = j+1
                        break
                    index = index + 1
                # If not try again, do not update j counter
                if found == False:
                    print("\nThat is not a  valid skill option. Please try again. Your remaining options are: ")
                    printPretty(len(pretty_options_list), pretty_options_list)

        index = 0
        print("\n\nYou are now proficient in the following skills: ")
        for skill in skill_proficiencies:
            index = index +1
            print("(" + str(index) + ") " + skill)
        print()

        return skill_proficiencies

# *************************************************************************** #
# Character = name, race, class, background, scores, skills

Fighter =       CharClass("Fighter",    10, "STR or DEX",   "STR", "CON", 2, ["Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation", "Perception", "Survival"],                                                    "All armor, shields, simple\nand martial weapons")

print("\n")
final_scores = [9, 11, 13, 14, 16, 18]
final_score_mods = []
index = 0
for score in final_scores:
    final_score_mods = final_score_mods + [(score-10)//2]
    index = index + 1
ability_scores_string = [ "STR", "DEX", "CON", "INT", "WIS", "CHA" ]
char_name = "Francis"
char_race = Dwarf_Hill
char_class = Fighter
skill_proficiencies = ["Athletics", "Perception"]

print("Race:\t" + char_race.name)
print("Class:\t" + char_class.name + "\n")

char_background = Soldier
char_class.pickSomeProficiencies(char_background)





print("\n")
