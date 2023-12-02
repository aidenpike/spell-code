import json

with open("spells.json", 'r') as file:
    spell_read = json.load(file)

print(spell_read)