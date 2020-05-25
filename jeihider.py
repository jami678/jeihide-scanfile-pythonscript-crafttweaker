

import re
import pyperclip
import os
from pathlib import Path


extra_search = 'obelisk'
optionalfolder1 = None
mod = 'strange'
folder_url = "C:\\Users\\Dwas\\Twitch\\Minecraft\\instances\\tg 3\\scripts\\"
enable_disable_crafting_recipes = False

print("Hello World")
f = open("blocks.txt", "r")
pattern = re.compile( r'\b' + mod + ':\b.*\b[,]\b', re.MULTILINE)
read = f.read().split(',')


array = []
for val in read:
    if (re.search(mod + ':', val)):
        if(extra_search != None) :
            if(re.search(extra_search, val)) :
              array.append(val)
        else :
            array.append(val)

array2 = []
for val in array:
    edited = val.replace(mod +':', '') 
    array2.append('JEI.hideItem(<item:' + mod + ':' + edited[1:] + '>);')

array2 = set(array2)

array3 = []
if (enable_disable_crafting_recipes == True) :
    for val in array:
        edited = val.replace(mod +':', '') 
        array3.append('craftingTable.removeRecipe(<item:' + mod + ':' + edited[1:] + '>);')

array3 = set(array3)

folder = folder_url + mod + '\\'

if optionalfolder1 != None :
    folder = folder + optionalfolder1 + '\\'

full_file = folder + mod + ' - ' + extra_search + '.zs'

Path(folder).mkdir(parents=True, exist_ok=True)

if not os.path.isfile(full_file):
    open(full_file, 'w').close()
    File_object = open(full_file,"a")
    File_object.write('import mods.jei.JEI; \n \n' + str(array2).strip('[]').replace("'", '').replace(",", '\n').replace("{", '').replace("}", ''))
    
    if(array3) :
       File_object.write( '\n' + str(array3).strip('[]').replace("'", '').replace(",", '\n').replace("{", '').replace("}", ''))
   
    File_object.close()



