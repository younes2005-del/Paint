#Imports 
import pygame
import numpy as np
import json
#init
pygame.init()


#Vars
WIDTH , HEIGHT = 1000, 600
run = True
actual_color = "imgs\RED.png"
WHITE = (255,255,255)
BLACK = (0,0,0)
ORNG = (255,151,14)
RED = (255,0,0)
BLU = (0,255,0)
GRN = (0,0,255)
FPS = 1000000000000000000000000000000000000000000000000000000000000000000000000000
msr = 50
win = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
positions = {(0,0) : "imgs\WIT.png"}
colours = {
    (0,HEIGHT - 50) : "imgs\GRN.png",
    (50,HEIGHT - 50) : "imgs\WT.png",
    (100,HEIGHT - 50) : "imgs\YLW.png",
    (150,HEIGHT - 50) : "imgs\RED.png",
    (200,HEIGHT - 50) : "imgs\ORNG.png",
    (250,HEIGHT - 50) : "imgs\BLU.png"

}
drawing = False

x_for_grid = 0
y_for_grid = -50
for _ in range(int(WIDTH / msr)):
    y_for_grid = -50
    for _ in range(int(HEIGHT /msr)):
        positions[(x_for_grid,y_for_grid)] = "imgs/WIT.png"
        y_for_grid += msr
    x_for_grid += msr 


#Main gam loop
while run:
    keys = pygame.key.get_pressed()
    #draw a grid


 

    for position in positions.items():
        win.blit(pygame.image.load(position[1]), position[0])
    
    for colour in colours.items():
        print(colour[0],colour[1])
        win.blit(pygame.image.load(colour[1]), colour[0])
    pygame.display.update()
    if drawing:
            pos = pygame.mouse.get_pos()
            new_x = int(pos[0] / msr)  * msr
            new_y = int(pos[1] / msr) * msr
            kayna = False
            for position in positions:
                if position == pos:
                    kayna = True
            if kayna == False and new_y != HEIGHT - 50: 
                positions[(new_x,new_y)] = actual_color
            elif new_y == HEIGHT - 50:
                try :
                    colour = colours[(new_x,new_y)]
                    actual_color = colour
                except:
                    pass
    
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if drawing:
                drawing = False
            else:
                drawing = True
    
            
            


    if keys[pygame.K_SPACE]:
        actual_color = "imgs\WIT.png"
        print("Erease !")
    if keys[pygame.K_r]:
        actual_color = "imgs\RED.png"
        print("turn to RED !")
    if keys[pygame.K_y]:
        actual_color = "imgs\YLW.png"
        print("turn to YELLOW !")
    if keys[pygame.K_g]:
        actual_color = "imgs\GRN.png"
        print("turn to GREEN !")
    if keys[pygame.K_s]:
        actual_color = "imgs\WT.png"
        print("turn to whithe !")





    


            



