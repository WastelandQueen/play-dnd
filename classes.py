class CharClass:
    def __init__(class_object, name, hit_die, prime_ability, save_throw1, save_throw2, proficiencies):
        class_object.name = name
        class_object.hit_die = hit_die
        class_object.prime_ability = prime_ability
        class_object.save_throw1 = save_throw1
        class_object.save_throw2 = save_throw2
        class_object.proficiencies = proficiencies

    def displayDetails(a_class):
        print("***** " + a_class.name.upper() + " *****")
        print("Hit die: 1d" + str(a_class.hit_die))
        print("Primary ability: " + a_class.prime_ability)
        print("Saving throw proficiencies: " + a_class.save_throw1 + " and " + a_class.save_throw2)
        print("Armor and weapon proficiencies: " + a_class.proficiencies + "\n\n")

Barbarian =     CharClass("Barbarian",  12, "STR",          "STR", "CON", "Light and medium armor, shields, simple and martial weapons")
Bard =          CharClass("Bard",       8,  "CHA",          "DEX", "CHA", "Light armor, simple weapons, hand crossbows, longswords,\nrapiers, shortswords")
Cleric =        CharClass("Cleric",     8,  "WIS",          "WIS", "CHA", "Light and medium armor, shields, simple weapons")
Druid =         CharClass("Druid",      8,  "WIS",          "INT", "WIS", "Light and medium armor (nonmetal), shields (nonmetal), clubs,\ndaggers, darts, javelins, maces, quarterstaffs, scimitars, sickles, slings, spears")
Fighter =       CharClass("Fighter",    10, "STR or DEX",   "STR", "CON", "All armor, shields, simple and martial weapons")
Monk =          CharClass("Monk",       8,  "DEX and WIS",  "STR", "DEX", "Simple weapons, shortswords")
Paladin =       CharClass("Paladin",    10, "STR and CHA",  "WIS", "CHA", "All armor, shields, simple and martial weapons")
Ranger =        CharClass("Ranger",     10, "DEX and WIS",  "STR", "DEX", "Light and medium armor, shields, simple and martial weapons")
Rogue =         CharClass("Rogue",      8,  "DEX",          "DEX", "INT", "Light armor, simple weapons, hand crossbows, longswords,\nrapiers, shortswords")
Sorcerer =      CharClass("Sorcerer",   6,  "CHA",          "CON", "CHA", "Daggers, darts, slings, quarterstaffs, light crossbows")
Warlock =       CharClass("Warlock",    8,  "CHA",          "WIS", "CHA", "Light armor, simple weapons")
Wizard =        CharClass("Wizard",     6,  "INT",          "INT", "WIS", "Daggers, darts, slings, quarterstaffs, light crossbows")

class_list = [ Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard ]
class_names = []
for class_name in class_list:
    class_names.append(class_name.name)
