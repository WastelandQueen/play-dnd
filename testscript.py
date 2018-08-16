import diceFunctions as dF

from races import *
from classes2 import *

char_class = Barbarian
char_class.displayDetails()
skills = char_class.pickProficiencies()
char_class.displayAllDetails(skills)
