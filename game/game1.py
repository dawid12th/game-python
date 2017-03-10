import pygame, sys
from classes import *
pygame.init()
WIDTH,HEIGHT = 640, 360
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
img_bug=pygame.image.load("bug.png")
clr1 = (22,122,211)
clr2 = (0, 44, 166)
clr3 = (34,55, 245)
i = 0

clock = pygame.time.Clock()
FPS = 24

bug = Bug(0,100, 40, 40, "bug.png")
totalframes = 0
while True:
    # PROCESSES
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # PROCESSES
    # LOGIC

    totalframes += 1
    i += 5
    if i > 255:
        i %= 255

    # LOGIC
    # DRAW
    screen.fill((i, i, 100 ))
    #screen.blit(img_bug, (200,200))
    BaseClass.allsprites.draw(screen)
    pygame.display.flip()
    # DRAW

    clock.tick(FPS)