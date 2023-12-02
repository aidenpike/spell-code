import json
import pygame

pygame.init()
window = pygame.display.set_mode([800, 800])

with open("spells.json", 'r') as file:
    spell_read = json.load(file)

spell_search = str(input("Enter spell you would like to look at: "))
color_hex = spell_read[spell_search]['visual']['color'].lstrip('#')
color_rgb = tuple(int(color_hex[i:i+2], 16) for i in (0, 2, 4))

print("Spell Name:", spell_search)
print("Spell Color:", color_rgb)
print("Spell Damage:", spell_read[spell_search]['properties']['damage']['damage_amount'])    

pygame.draw.rect(window, (color_rgb), pygame.Rect(30, 30, 60, 60))
pygame.display.flip()

input()