import pygame
import math

pygame.init()
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
pygame.event.set_allowed([])

white = (255,255,255)
black = (0,0,0)

length = 300
theta = math.pi / 2
vel = 0
g = 0.0001
friction = 0.001

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    vel -= g * math.sin(theta) + friction * vel
    theta += vel

    x = 400 + length * math.sin(theta)
    y = 400 + length * math.cos(theta)

    screen.fill(black)
    pygame.draw.line(screen, white, (400,400), (x,y))

    print(clock.get_time())
    clock.tick(500)
    pygame.display.flip()