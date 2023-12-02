spells = open("spells.json", 'r')
spell_read = spells.readline()

while spell_read != "":
    print(spell_read)