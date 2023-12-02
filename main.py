import json

with open("spells.json", 'r') as file:
    spell_read = json.load(file)

spell_search = str(input("Enter spell you would like to look at: "))

print("Spell Name:", spell_search)
print("Spell Color:", spell_read[spell_search]['visual']['color'])
print("Spell Damage:", spell_read[spell_search]['properties']['damage']['damage_amount'])    



