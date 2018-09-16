import diceFunctions as dF
import characterChoices as cC

from races import *
from classes import *
from backgrounds import *

print("\n\n****************************")
print("**** DUNGEONS & DRAGONS ****")
print("**** CHARACTER CREATION ****")
print("****************************")

print("\nHello! Let's make a new character.")
print("\n*************************************")
print("**** SECTION 1: CHOOSE YOUR RACE ****")
print("*************************************\n")
char_race = cC.chooseRace()


print("\n\n**************************************")
print("**** SECTION 2: CHOOSE YOUR CLASS ****")
print("**************************************\n")
char_class = cC.chooseClass()


print("\n\n*******************************************")
print("**** SECTION 3: CHOOSE YOUR BACKGROUND ****")
print("*******************************************\n")
char_background = cC.chooseBackground()


print("\n\n***********************************************")
print("**** SECTION 4: CHOOSE YOUR ABILITY SCORES ****")
print("***********************************************\n")

final_scores = cC.determineScores(char_race, char_class)

STR = final_scores[0]
DEX = final_scores[1]
CON = final_scores[2]
INT = final_scores[3]
WIS = final_scores[4]
CHA = final_scores[5]

STR_mod = (STR-10)//2
DEX_mod = (DEX-10)//2
CON_mod = (CON-10)//2
INT_mod = (INT-10)//2
WIS_mod = (WIS-10)//2
CHA_mod = (CHA-10)//2

final_score_mods = [STR_mod, DEX_mod, CON_mod, INT_mod, WIS_mod, CHA_mod]


print("\n\n*********************************************")
print("**** SECTION 5: CHOOSE YOUR PROFICINCIES ****")
print("*********************************************\n")
skills = char_class.pickProficiencies(char_background)



"""
A summary of the created character.
"""

char_name = input("What would you like to name your character?: ")

print("\n")

i = 0
aster_string = "*"
while i < len(char_name):
    aster_string = aster_string + "*"
    i = i+1
aster_string = aster_string + "***"

print(aster_string)
print("* " + char_name.upper() + " *")
print(aster_string + "\n")
char_race.displayAllDetails()
char_class.displayAllDetails(skills)

hp_lvl1 = char_class.hit_die + CON_mod

#TODO: print final scores, health, etc
#TODO: add alignment choices

ability_scores_string = [ "STR", "DEX", "CON", "INT", "WIS", "CHA" ]

print("\nSTAT\tSCORE\tMOD")
print("-----\t-----\t---")
index = 0
for score in final_scores:
    if ((score-10)/2) >= 0:
        print(ability_scores_string[index] + ":\t" + str(score) + "\t+" + str(final_score_mods[index]))
        index = index + 1
    else:
        print(ability_scores_string[index] + ":\t" + str(score) + "\t" + str(final_score_mods[index]))
        index = index + 1

print("\n     CHARACTER DETAILS")
print("---------------------------")
print("Level:\t\t\t1") # TODO: allow the user to set level, and level up the character
print("Speed:\t\t\t" + str(char_race.speed))
print("Hit Die:\t\t1d" + str(char_class.hit_die))
print("Proficiency bonus:\t+2")

print("\n")
