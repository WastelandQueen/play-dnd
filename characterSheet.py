def createCharacterSheet(char_name):
    file_name = char_name + ".txt"
    char_sheet = open(file_name,"w+")
    char_sheet.write("****************************************************************\n")
    char_sheet.write("CHARACTER INFO\n")
    char_sheet.write("NAME:\t" + char_name + "\n")
    #char_sheet.write("RACE:\t" + char_race +)
    char_sheet.write("")
    char_sheet.write("")
    char_sheet.write("")
    char_sheet.write("")
    char_sheet.write("")
    char_sheet.write("")
    char_sheet.write("")
    char_sheet.write("")


char_name = "Tiffany"
createCharacterSheet(char_name)
