import json
import pygame

#Display and Framerate
pygame.init()
window = pygame.display.set_mode([800, 800])
frame_clock = pygame.time.Clock().tick(60)

with open("spells.json", 'r') as file:
    spell_read = json.load(file)

#spell_search = str(input("Enter spell you would like to look at: "))
spell_search = "test spell"
#Hex -> RGB for pygame
color_hex = spell_read[spell_search]['visual']['color'].lstrip('#')
color_rgb = tuple(int(color_hex[i:i+2], 16) for i in (0, 2, 4))

print("Spell Name:", spell_search)
print("Spell Color:", color_rgb)
print("Spell Damage:", spell_read[spell_search]['properties']['damage']['damage_amount'])    

#Speed calculation: If speed = 1, and framerate is 60, the sprite moves at 1 pixel every 2 frames, so 30 pixels a second
pos_x = 0
pos_y = 100

loop = True
key_pressed = False

if spell_read[spell_search]['properties']['movement']['speed'] < 10:
    print("Speed too low! Setting to default of 10.")
    spell_read[spell_search]['properties']['movement']['speed'] = 10

while loop:
    key_stroke = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
    
    if key_stroke[pygame.K_d]:
        key_pressed = True
            
    if key_pressed and pos_x <= window.get_width() - 20: 
        pos_x += spell_read[spell_search]['properties']['movement']['speed']/frame_clock

    if pos_x == window.get_width() - 20:
        color_hex = "000000"
        color_rgb = tuple(int(color_hex[i:i+2], 16) for i in (0, 2, 4))
        print("Hit!", spell_read[spell_search]['properties']['damage']['damage_amount'], spell_read[spell_search]['properties']['damage']['damage_type'], "Damage")

    window.fill((0, 0, 0))

    pygame.draw.circle(window, (color_rgb), (pos_x, pos_y), 30)
    
    pygame.display.update()