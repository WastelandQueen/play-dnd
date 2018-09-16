
class CharBackground:
    def __init__(background, name, proficiency1, proficiency2, other_proficiencies):
        background.name = name
        background.proficiency1 = proficiency1
        background.proficiency2 = proficiency2
        background.other_proficiencies = other_proficiencies

    def displayDetails(a_background):
        print("\nBackground: " + a_background.name)
        print("Skill proficiencies:\n(1) " + a_background.proficiency1 + "\n(2) " + a_background.proficiency2)
        print(a_background.other_proficiencies)

Acolyte =       CharBackground("Acolyte",       "Insight",          "Religion",         "Languages: 2 of your choice")
Charlatan =     CharBackground("Charlatan",     "Deception",        "Sleight of Hand",  "Tools: Disguise kit, Forgery kit")
Criminal =      CharBackground("Criminal",      "Deception",        "Stealth",          "Tools: 1 type of gaming set, thieves' tools")
Entertainer =   CharBackground("Entertainer",   "Acrobatics",       "Performance",      "Tools: Disguise kit, 1 type of musical instrument")
Folk_Hero =     CharBackground("Folk Hero",     "Animal Handling",  "Survival",         "Tools: 1 type of artisan's tools, land vehicles")
Guild_Artisan = CharBackground("Guild Artisan", "Insight",          "Persuasion",       "Tools: 1 type of artisan's tools\nLanguages: 1 of your choice")
Hermit =        CharBackground("Hermit",        "Medicine",         "Religion",         "Tools: Herbalism kit\nLanguages: 1 of your choice")
Noble =         CharBackground("Noble",         "History",          "Persuasion",       "Tools: 1 type of gaming set\nLanguages: 1 of your choice")
Outlander =     CharBackground("Outlander",     "Athletics",        "Survival",         "Tools: 1 type of musical instrument\nLanguages: 1 of your choice")
Sage =          CharBackground("Sage",          "Arcana",           "History",          "Languages: 2 of your choice")
Sailor =        CharBackground("Sailor",        "Athletics",        "Perception",       "Tools: Navigator's tools, water vehicles")
Soldier =       CharBackground("Soldier",       "Athletics",        "Intimidation",     "Tools: 1 type of gaming set, land vehicles")
Urchin =        CharBackground("Urchin",        "Sleight of Hand",  "Stealth",          "Tools: Disguise kit, thieves' tools")

background_list = [Acolyte, Charlatan, Criminal, Entertainer, Folk_Hero, Guild_Artisan, Hermit, Noble, Outlander, Sage, Sailor, Soldier, Urchin]
background_names = []
for background in background_list:
    background_names.append(background.name)
