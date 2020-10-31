import pygame

pygame.init()
FPS = 60
WIDTH,HEIGHT = 500, 500
clock = pygame.time.Clock()
win = pygame.display.set_mode((WIDTH,HEIGHT))
run = True
while run:
    win.fill((0,0,0))
    pygame.draw.rect(win, (255,255,255), (0, 0, 490, 490))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    