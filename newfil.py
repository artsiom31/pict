import pygame
from pygame.draw import *


pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 400))

rect(screen, (135, 206, 235), (0, 0, 600, 200))
rect(screen, ("green"), (0, 200, 600, 200))

# sky
A = [(310, 40), (330, 40), (350, 40), (370, 40), (330, 25), (350, 25)]
for x, y in A:
    circle(screen, ("white"), (x, y), 25)
    circle(screen, ("black"), (x, y), 25, 1)

line(screen, ("black"), (420, 250), (420, 170), 15)

#tree
B = [(420, 125), (400, 140), (440, 140), (420, 155), (400, 170), (440, 170)]
for x, y in B:
    circle(screen, (5, 102, 8), (x, y), 25)
    circle(screen, ("black"), (x, y), 25, 1)

#sun
circle(screen, ("yellow"), (500, 40), 30)

#house
 #build
rect(screen, ("yellow"), (100, 170, 200, 120))
rect(screen, ("black"), (100, 170, 200, 120), 2)

 #roof
polygon(screen, ("green"), ((80, 170), (320, 170), (200, 100)))
polygon(screen, ("black"), ((80, 170), (320, 170), (200, 100)), 3)

 #windows
rect(screen, (135, 206, 235), (140, 200, 40, 50))
rect(screen, ("black"), (140, 200, 40, 50), 2)
rect(screen, (135, 206, 235), (220, 200, 40, 50))
rect(screen, ("black"), (220, 200, 40, 50), 2)







pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
