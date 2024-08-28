import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
pygame.event.set_allowed([])

white = (255,255,255)
black = (0,0,0)

n = 20
vel = 5
radius = 20
randcolor = False

balls = []
for i in range(n):
    z = (random.randrange(radius,800-radius) + random.randrange(radius,800-radius) * 1j)
    t = random.random() * math.tau
    v = vel * (math.cos(t) + math.sin(t) * 1j)
    if randcolor:
        color = (random.randrange(128,256),random.randrange(128,256),random.randrange(128,256))
    else: 
        color = white
    balls.append([z,v,color])

balls = tuple(balls)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    for ball in balls:
        ball[0] += ball[1]

        if ball[0].real < radius:
            ball[1] = abs(ball[1].real) + ball[1].imag * 1j
        elif ball[0].real > 800-radius:
            ball[1] = -abs(ball[1].real) + ball[1].imag * 1j
        if ball[0].imag < radius:
            ball[1] = ball[1].real + abs(ball[1].imag) * 1j
        elif ball[0].imag > 800-radius:
            ball[1] = ball[1].real - abs(ball[1].imag) * 1j
    
    for ball1 in balls:
        for ball2 in balls:
            if ball1 != ball2:
                z1, v1, _ = ball1
                z2, _, _ = ball2
                if abs(z1-z2) < 2 * radius:
                    v1 = - (z1-z2)**2 / v1 * vel**2 / abs(z1-z2)**2
                    ball1[1] = v1
    
    screen.fill(black)
    
    for ball in balls:
        pygame.draw.circle(screen, ball[2], (ball[0].real,ball[0].imag), radius)

    clock.tick(60)
    pygame.display.flip()

    