import json

with open("spells.json", 'r') as file:
    spell_read = json.load(file)

print(spell_read)    
#spell_search = str(input("Enter spell you would like to look at: "))

print("Spell Name: " + spell_read['spell']['visual']['name'])
    



