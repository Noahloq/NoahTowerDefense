import pygame
from pygame import *

#Initialize pygame
pygame.init()

#We are creating variables to define the dimensions of the window, separately.

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 400
WINDOW_RES = (WINDOW_WIDTH, WINDOW_HEIGHT)

#Create Window
GAME_WINDOW = display.set_mode(WINDOW_RES)
#900 pixels for the width, 400 pixels for the height

display.set_caption("Tower Defense Game")

background_img = image.load('restuarant.jpg')
backgroung_surf = Surface.convert_alpha(background_img)
BACKGROUND = transform.scale(background_surf, (WINDOW_RES))
Banana_img = image.load('Banana.png')
Banana_surf = Surface.convert_alpha(Banana_img)

BANANA_SPRITE = transform.scale(Banana_surf, (100, 100))

#Display the enemy image to the screen
GAME_WINDOW.blit(BANANA_SPRITE, (900, 400))
VAMPIRE_PIZZA = transform.scale(pizza_surf, (100, 100))
draw.circle(GAME_WINDOW, (0, 255, 0), (925, 425), 25, 0)
draw.rect(GAME_WINDOW, (160, 82, 45), (895, 395, 110, 110), 5)
draw.rect(GAME_WINDOW, (160, 82, 45), (895, 295, 110, 110), 0)

GAME_WINDOW.blit(BANANA_SPRITE, (900, 400))
GAME_WINDOW.blit(BACKROUND, (0,0))
GAMEWINDOW.blit(VAMPIRE_PIZZA, (700, 300))


#A tuple is data type that contains data separated by commas, and contained within parentheses

#Start Main Game Loop
game_running = True

while game_running:
    for event in pygame.event.get():
        #Exit the loop on quit
        if event.type == QUIT:
            game_running = False
        display.update()

pygame.quit()
    
