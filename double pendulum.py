import pygame
import math

pygame.init()
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
pygame.event.set_allowed([])

white = (255,255,255)
black = (0,0,0)

# Wrong

length = 150
theta = math.pi / 2
phi = math.pi / 2
Vel = 0
vel = 0
g = 0.00005
# friction = 0.001

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    vel -= g * math.sin(phi)
    Vel -= g * math.cos(phi) * math.sin(theta-phi)
    phi += vel
    theta += Vel

    X = 400 + length * math.sin(theta)
    Y = 400 + length * math.cos(theta)
    x = X + length * math.sin(phi)
    y = Y + length * math.cos(phi)

    screen.fill(black)
    pygame.draw.line(screen, white, (400,400), (X,Y))
    pygame.draw.line(screen, white, (X,Y), (x,y))

    print(clock.get_time())
    clock.tick(500)
    pygame.display.flip()
