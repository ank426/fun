import pygame

pygame.init()
screen = pygame.display.set_mode((1000,1000))
clock = pygame.time.Clock()
pygame.event.set_allowed([])

white = (255,255,255)
black = (0,0,0)

radius = 10
Gmm = 0.00003
z1 = 300 + 500j
z2 = 700 + 500j
vel1 = 0.0002j
vel2 = -0.0002j

# n = 3
# objs = []
# for i in range(n):
    
#     objs.append([])

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    for i in range(10000):
        vel1 += Gmm * (z2-z1) / abs(z2-z1)**3
        vel2 += Gmm * (z1-z2) / abs(z1-z2)**3

        z1 += vel1
        z2 += vel2

    screen.fill(black)
    pygame.draw.circle(screen, white, (z1.real, z1.imag), radius)
    pygame.draw.circle(screen, white, (z2.real, z2.imag), radius)

    clock.tick(60)
    pygame.display.flip()