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
    def __init__(class_object, name, hit_die, prime_ability, save_throw1, save_throw2, pick_num, skill_prof_options, other_proficiencies):
        class_object.name = name
        class_object.hit_die = hit_die
        class_object.prime_ability = prime_ability
        class_object.save_throw1 = save_throw1
        class_object.save_throw2 = save_throw2
        class_object.pick_num = pick_num
        class_object.skill_prof_options = skill_prof_options
        class_object.other_proficiencies = other_proficiencies

    def displayDetails(a_class):
        all_skills_list_pretty = ["Animal Handling    ", "Athletics          ", "Intimidation       ", "Nature             ", "Perception         ", "Survival           ", "History            ", "Insight            ", "Medicine           ", "Persuasion         ", "Religion           ", "Arcana             ", "Acrobatics         ", "Stealth            ", "Investigation      ", "Deception          ", "Performance        ", "Sleight of Hand    "]
        print("********* " + a_class.name.upper() + " *********")
        print("HIT DIE:         1d" + str(a_class.hit_die))
        print("PRIMARY ABILITY: " + a_class.prime_ability)
        print("SAVING THROWS:   " + a_class.save_throw1 + " and " + a_class.save_throw2)
        print("ARMOR AND WEAPON PROFICIENCIES:  " + a_class.other_proficiencies)
        #print("\nSKILLS (choose " + str(a_class.pick_num) + " skills from the following list):")

    def pickProficiencies(a_class,a_background):
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

    def displayAllDetails(a_class, skills):
        all_skills_list_pretty = ["Animal Handling    ", "Athletics          ", "Intimidation       ", "Nature             ", "Perception         ", "Survival           ", "History            ", "Insight            ", "Medicine           ", "Persuasion         ", "Religion           ", "Arcana             ", "Acrobatics         ", "Stealth            ", "Investigation      ", "Deception          ", "Performance        ", "Sleight of Hand    "]
        print("********* " + a_class.name.upper() + " *********")
        print("HIT DIE:         1d" + str(a_class.hit_die))
        print("PRIMARY ABILITY: " + a_class.prime_ability)
        print("SAVING THROWS:   " + a_class.save_throw1 + " and " + a_class.save_throw2)
        print("ARMOR AND WEAPON PROFICIENCIES:  " + a_class.other_proficiencies)
        print("SKILL PROFICIENCIES: ")
        index = 0
        for skill in skills:
            index = index +1
            print("(" + str(index) + ") " + skill)

all_skills_list_pretty = ["Animal Handling    ", "Athletics          ", "Intimidation       ", "Nature             ", "Perception         ", "Survival           ", "History            ", "Insight            ", "Medicine           ", "Persuasion         ", "Religion           ", "Arcana             ", "Acrobatics         ", "Stealth            ", "Investigation      ", "Deception          ", "Performance        ", "Sleight of Hand    "]
all_skills_list =["Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival", "History", "Insight", "Medicine", "Persuasion", "Religion", "Arcana", "Acrobatics", "Stealth", "Investigation", "Deception", "Performance", "Sleight of Hand"]

Barbarian =     CharClass("Barbarian",  12, "STR",          "STR", "CON", 2, ["Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"],                                                                              "Light and medium armor,\nshields, simple and martial weapons")
Bard =          CharClass("Bard",       8,  "CHA",          "DEX", "CHA", 3, all_skills_list,                                                                                                                                                   "Light armor, simple weapons,\nhand crossbows, longswords, rapiers, shortswords")
Cleric =        CharClass("Cleric",     8,  "WIS",          "WIS", "CHA", 2, ["History", "Insight", "Medicine", "Persuasion", "Religion"],                                                                                                      "Light and medium armor,\nshields, simple weapons")
Druid =         CharClass("Druid",      8,  "WIS",          "INT", "WIS", 2, ["Arcana", "Animal Handling", "Insight", "Medicine", "Nature", "Perception", "Religion", "Survival"],                                                              "Light and medium armor\n(nonmetal), shields (nonmetal), clubs, daggers, darts,\njavelins, maces, quarterstaffs, scimitars, sickles, slings,\nspears")
Fighter =       CharClass("Fighter",    10, "STR or DEX",   "STR", "CON", 2, ["Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation", "Perception", "Survival"],                                                    "All armor, shields, simple\nand martial weapons")
Monk =          CharClass("Monk",       8,  "DEX and WIS",  "STR", "DEX", 2, ["Acrobatics", "Athletics", "History", "Insight", "Religion", "Stealth"],                                                                                          "Simple weapons, shortswords")
Paladin =       CharClass("Paladin",    10, "STR and CHA",  "WIS", "CHA", 2, ["Athletics", "Insight", "Intimidation", "Medicine", "Persuasion", "Religion"],                                                                                    "All armor, shields, simple\nand martial weapons")
Ranger =        CharClass("Ranger",     10, "DEX and WIS",  "STR", "DEX", 3, ["Animal Handling", "Athletics", "Insight", "Investigation", "Nature", "Perception", "Stealth", "Survival"],                                                       "Light and medium armor,\nshields, simple and martial weapons")
Rogue =         CharClass("Rogue",      8,  "DEX",          "DEX", "INT", 4, ["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception", "Performance", "Persuasion", "Sleight of Hand", "Stealth"],     "Light armor, simple weapons,\nhand crossbows, longswords, rapiers, shortswords")
Sorcerer =      CharClass("Sorcerer",   6,  "CHA",          "CON", "CHA", 2, ["Arcana", "Deception", "Insight", "Intimidation", "Persuasion", "Religion"],                                                                                      "Daggers, darts, slings,\nquarterstaffs, light crossbows")
Warlock =       CharClass("Warlock",    8,  "CHA",          "WIS", "CHA", 2, ["Arcana", "Deception", "History", "Intimidation", "Investigation", "Nature", "Religion"], "Light armor, simple weapons")
Wizard =        CharClass("Wizard",     6,  "INT",          "INT", "WIS", 2, ["Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"], "Daggers, darts, slings, quarterstaffs, light crossbows")

class_list = [ Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard ]
class_names = []
for class_name in class_list:
    class_names.append(class_name.name)
