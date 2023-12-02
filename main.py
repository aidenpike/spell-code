import json

with open("spells.json", 'r') as file:
    spell_read = json.load(file)
    
key_input = input("What would  you like to access?: ")

print(spell_read['spell']['visual'][key_input])
