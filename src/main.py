import json
import pygame
import os

spell_search = str(input("Enter spell you would like to look at: "))

for file in os.listdir("spells"):
    if file == f"{spell_search}.json":
        with open(f"spells/{spell_search}.json", 'r') as file:
            spell_read = json.load(file)

#Display and Framerate
pygame.init()
window = pygame.display.set_mode([800, 800])
frame_clock = pygame.time.Clock().tick(60)

#Position Variables
pos_x = 0
pos_y = 100

loop = True
pressed_key = False

filepath = f"imgs/{spell_search}/{spell_search}.png"

def activate_on_hit():
    filepath = f"imgs/{spell_search}/{spell_search}_on_hit.png"

    load_image(filepath)

    print("Hit!", spell_read[spell_search]['properties']['damage']['damage_amount'], spell_read[spell_search]['properties']['damage']['damage_type'], "Damage")

def load_image(filepath):
    image = pygame.image.load(filepath).convert()
    window.blit(image, (pos_x, pos_y))

if spell_read[spell_search]['properties']['movement']['speed'] < 10:
    print("Speed too low! Setting to default of 10.")
    spell_read[spell_search]['properties']['movement']['speed'] = 10

#Game Loop
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pressed_key = True
            
    if pressed_key and pos_x <= window.get_width(): 
        pos_x += spell_read[spell_search]['properties']['movement']['speed']/frame_clock

    if pos_x == window.get_width():
        load_image("imgs/test spell/test spell_on_hit.png")

    window.fill((0, 0, 0))

    load_image(filepath)
    
    pygame.display.update()