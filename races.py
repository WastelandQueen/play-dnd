
class CharRace:
    def __init__(race_object, name, speed, str, dex, con, int, cha, wis, traits):
        race_object.name = name
        race_object.str = str
        race_object.dex = dex
        race_object.con = con
        race_object.int = int
        race_object.cha = cha
        race_object.wis = wis
        race_object.speed = speed
        race_object.traits = traits

    def displayDetails(a_race):
        print("********* " + a_race.name.upper() + " *********")
        print("Speed: " + str(a_race.speed))
        print("Racial bonuses:")
        if a_race.str != 0:
                print("     STR: +" + str(a_race.str))
        if a_race.dex != 0:
                print("     DEX: +" + str(a_race.dex))
        if a_race.con != 0:
                print("     CON: +" + str(a_race.con))
        if a_race.int != 0:
                print("     INT: +" + str(a_race.int))
        if a_race.cha != 0:
                print("     CHA: +" + str(a_race.cha))
        if a_race.wis != 0:
                print("     WIS: +" + str(a_race.wis))
        print("Traits:\n" + a_race.traits + "\n\n")

    def displayAllDetails(a_race):
        print("********* " + a_race.name.upper() + " *********")
        print("Speed: " + str(a_race.speed))
        if a_race.name == "Human":
            print("Languages: Common and one extra language of your choice\n\n")
        else:
            print("Traits:\n" + a_race.traits + "\n")

    def getScores(a_race):
        char_scores = [a_race.str, a_race.dex, a_race.con, a_race.int, a_race.cha, a_race.wis]
        return char_scores

#                                                       S, D, C, I, C, W
Dwarf_Hill =            CharRace("Hill Dwarf",          25, 0, 0, 2, 0, 0, 1, "(1) Darkvision\n(2) Dwarven Resiliance\n(3) Dwarven Combat Training\n(4) Tool Proficiency\n(5) Stonecunning\n(6) Dwarven Toughness\nLanguages: Common and Dwarvish")
Dwarf_Mountain =        CharRace("Mountain Dwarf",      25, 2, 0, 2, 0, 0, 0, "(1) Darkvision\n(2) Dwarven Resiliance\n(3) Dwarven Combat Training\n(4) Tool Proficiency\n(5) Stonecunning\n(6) Dwarven Armor Training\nLanguages: Common and Dwarvish")

Elf_High =              CharRace("High Elf",            30, 0, 2, 0, 1, 0, 0, "(1) Darkvision\n(2) Keen Senses\n(3) Fey Ancestry\n(4) Trance\n(5) Elf Weapon Training\n(6) Cantrip\n(7) Extra Language\nLanguages: Common and Elvish")
Elf_Wood =              CharRace("Wood Elf",            35, 0, 2, 0, 0, 0, 1, "(1) Darkvision\n(2) Keen Senses\n(3) Fey Ancestry\n(4) Trance\n(5) Elf Weapon Training\n(6) Fleet of Foot\n(7) Mask of the Wild\nLanguages: Common and Elvish")
Elf_Dark =              CharRace("Dark Elf",            30, 0, 2, 0, 0, 1, 0, "(1) Superior Darkvision\n(2) Keen Senses\n(3) Fey Ancestry\n(4) Trance\n(5) SunJight Sensitivity\n(6) Drow Magic\n(7) Drow Weapon Training\nLanguages: Common and Elvish")

Halfling_Lightfoot =    CharRace("Lightfoot Halfling",  25, 0, 2, 0, 0, 1, 0, "(1) Lucky\n(2) Brave\n(3) Halfling Nimbleness\n(4) Naturally Stealthy\nLanguages: Common and Halfling")
Halfling_Stout =        CharRace("Stout Halfling",      25, 0, 2, 1, 0, 0, 0, "(1) Lucky\n(2) Brave\n(3) Halfling Nimbleness\n(4) Stout Resiliance\nLanguages: Common and Halfling")

Human =                 CharRace("Human",               30, 1, 1, 1, 1, 1, 1, "No extra traits\nLanguages: Common and one extra language of your choice")
#Human_V =               CharRace("Human Variant",       30, <choice> 1, <choice> 1, "Gain proficiency in one skill of your choice\nGain one feat of your choice\nLanguages: Common and one extra language of your choice")

Dragonborn =            CharRace("Dragonborn",          30, 2, 0, 0, 0, 1, 0, "(1) Draconic Ancestry\n(2) Breath Weapon\n(3) Damage Resistance\nLanguages: Common and Draconic")

Gnome_Forest =          CharRace("Forest Gnome",        25, 0, 1, 0, 2, 0, 0, "(1)Darkvision\n(2) Gnome Cunning\n(3) Natural Illusionist\n(4) Speak with Small Beasts\nLanguages: Common and Gnomish")
Gnome_Rock =            CharRace("Rock Gnome",          25, 0, 0, 1, 2, 0, 0, "(1)Darkvision\n(2) Gnome Cunning\n(3) Artificer's Lore\n(4) Tinker\nLanguages: Common and Gnomish")
Gnome_Deep =            CharRace("Deep Gnome",          25, 0, 1, 0, 2, 0, 0, "(1) Superior Darkvision\n(2) Gnome Cunning\n(3) Stone Camouflage\nLanguages: Common, Gnomish, and Undercommon")

#Half_Elf =              CharRace("Half-Elf",            30, CHA 2, <choice> 1, <choice> 1, "(1) Darkvision\n(2) Fey Ancestry\n(3) Skill Versatility\nLanguages: Common, EIvish, and one extra language of your choice")

Half_Orc =              CharRace("Half-Orc",            30, 2, 0, 1, 0, 0, 0, "(1) Darkvision\n(2) Menacing\n(3) Relentless Endurance\n(4) Savage Attacks\nLanguages: Common and Orc")

Tiefling =              CharRace("Tiefling",            30, 0, 0, 0, 1, 2, 0, "(1) Darkvision\n(2) Hellish Resistance\n(3) Infernal Legacy\nLanguages: Common and Infernal")

Aarakocra =             CharRace("Aarakocra",           25, 0, 2, 0, 0, 0, 1, "(1) Flight\n(2) Talons\nLanguages: Common, Aarakocra, and Auran")

Genasi_Air =            CharRace("Air Genasi",          30, 0, 1, 2, 0, 0, 0, "(1) Unending Breath\n(2) Mingle with the Wind\nLanguages: Common and Primordial")
Genasi_Earth =          CharRace("Earth Genasi",        30, 1, 0, 2, 0, 0, 0, "(1) Earth Walk\n(2) Merge with Stone\nLanguages: Common and Primordial")
Genasi_Fire =           CharRace("Fire Genasi",         30, 0, 0, 2, 1, 0, 0, "(1) Darkvision\n(2) Fire Resistance\n(3) Reach to the Blaze\nLanguages: Common and Primordial")
Genasi_Water =          CharRace("Water Genasi",        30, 0, 0, 2, 0, 0, 1, "(1) Amphibious\n(2) Swim\n(3) Call to the Wave\nLanguages: Common and Primordial")

Goliath =               CharRace("Goliath",             30, 2, 0, 1, 0, 0, 0, "(1) Natural Athlete\n(2) Stone's Endurance\n(3) Powerful Build\n(4) Mountain Born\nLanguages: Common and Giant")


race_list = [ Dwarf_Hill, Dwarf_Mountain, Elf_High, Elf_Wood, Elf_Dark, Halfling_Lightfoot, Halfling_Stout, Human, Dragonborn, Gnome_Forest, Gnome_Rock, Gnome_Deep, Half_Orc, Tiefling, Aarakocra, Genasi_Air, Genasi_Earth, Genasi_Fire, Genasi_Water, Goliath ]
race_names = []
for race_name in race_list:
    race_names.append(race_name.name)
