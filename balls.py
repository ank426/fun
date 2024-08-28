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
    x = random.randrange(radius,800-radius)
    y = random.randrange(radius,800-radius)
    t = random.random() * math.tau
    velx = vel * math.cos(t)
    vely = vel * math.sin(t)
    if randcolor:
        color = (random.randrange(128,256),random.randrange(128,256),random.randrange(128,256))
    else: 
        color = white
    balls.append([x,y,velx,vely,color])

balls = tuple(balls)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    for ball in balls:
        ball[0] += ball[2]
        ball[1] += ball[3]

        if ball[0] < radius:
            ball[2] = abs(ball[2])
        elif ball[0] > 800-radius:
            ball[2] = -abs(ball[2])
        if ball[1] < radius:
            ball[3] = abs(ball[3])
        elif ball[1] > 800-radius:
            ball[3] = -abs(ball[3])
    
    for ball1 in balls:
        for ball2 in balls:
            if ball1 != ball2:
                x1,y1,ux1,uy1,color=ball1
                x2,y2,ux2,uy2,color=ball2
                if math.sqrt((y1-y2)**2 + (x1-x2)**2) < 2 * radius:
                    t = 2 * math.atan((y1-y2)/(x1-x2)) - math.atan(uy1/ux1)
                    vx = vel * math.cos(t)
                    vy = vel * math.sin(t)
                    if (x1-x2)*vx + (y1-y2)*vy < 0:
                        vx = -vx
                        vy = -vy
                    ball1[2] = vx
                    ball1[3] = vy
    
    screen.fill(black)
    
    for ball in balls:
        pygame.draw.circle(screen, ball[4], (ball[0],ball[1]), radius)

    clock.tick(60)
    pygame.display.flip()

    