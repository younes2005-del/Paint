#Imports 
import pygame
import numpy as np
import json
#init
pygame.init()


#Vars
WIDTH , HEIGHT = 1000, 600
run = True
WHITE = (255,255,255)
BLACK = (0,0,0)
ORNG = (255,151,14)
RED = (255,0,0)
BLU = (0,0,255)
GRN = (0,255,0)
YLW = (238,255,0)
PNK = (255,0,208)
GRY = (123,123,123)
BRWN = (106,55,55)
PRPL = (130,0,130)
TRQ =(0,255,255)
BKG_COLOUR =WHITE
actual_color = BKG_COLOUR
FPS = 60
msr = 50
win = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
positions = {(0,0) : WHITE}
colours = {
    (0,HEIGHT - 50) : GRN,
    (50,HEIGHT - 50) : WHITE,
    (100,HEIGHT - 50) : YLW,
    (150,HEIGHT - 50) : RED,
    (200,HEIGHT - 50) : ORNG,
    (250,HEIGHT - 50) : BLU,
    (300,HEIGHT - 50) : PNK,
    (350,HEIGHT - 50) : BLACK,
    (400,HEIGHT - 50) : BRWN,
    (450,HEIGHT - 50) : PRPL,
    (500,HEIGHT - 50) : TRQ,
    (550,HEIGHT - 50) : GRY
}
drawing = False

x_for_grid = 0
y_for_grid = -50
for _ in range(int(WIDTH / msr)):
    y_for_grid = -50
    for _ in range(int(HEIGHT /msr)):
        positions[(x_for_grid,y_for_grid)] = BKG_COLOUR
        y_for_grid += msr
    x_for_grid += msr 


#Main gam loop
while run:
    keys = pygame.key.get_pressed()
    #draw a grid

 

    for position in positions.items():
        pos = position[0]
        pygame.draw.rect(win, position[1], (pos[0], pos[1], msr, msr))

    
    for colour in colours.items():
        pos = colour[0]
        pygame.draw.rect(win, colour[1], (pos[0], pos[1], 50, 50))
    pygame.display.update()
    if drawing:
        pos = pygame.mouse.get_pos()
        new_x = int(pos[0] / msr)  * msr
        new_y = int(pos[1] / msr) * msr
        x_co = int(pos[0] / 50)  * 50
        y_co = int(pos[1] / 50) * 50
        kayna = False

        
        for position in positions:

            if position == pos:
                kayna = True
            if kayna == False and new_y < HEIGHT - 50: 
                print("drawing !!")
                positions[(new_x,new_y)] = actual_color
            else:
                try :
                    if new_x < WIDTH:
                        colourn = colours[(x_co,y_co)]
                        actual_color = colourn
                        drawing = False



                except:
                    """
                    actual_color = BLACK
                    drawing = False
                    """
                    x_for_grid = 0
                    y_for_grid = -50
                    for _ in range(int(WIDTH / msr)):
                        y_for_grid = -50
                        for _ in range(int(HEIGHT /msr)):
                            positions[(x_for_grid,y_for_grid)] = BKG_COLOUR
                            y_for_grid += msr
                        x_for_grid += msr 
                    drawing = False


                


    
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
        actual_color = BKG_COLOUR
        print("Erease !")





    


            



