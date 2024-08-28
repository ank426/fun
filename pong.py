import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])

white = (255,255,255)
black = (0,0,0)

comicsans = pygame.font.SysFont('comicsans', 50)

left = 260
right = 260
x = 640
y = 360
score = 0

t = random.gauss(math.pi/4, 0.3)
velx = random.choice([-1,1]) * random.gauss(20,2) * math.cos(t)
vely = random.choice([-1,1]) * random.gauss(20,2) * math.sin(t)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        left -= 20
    elif pressed[pygame.K_s]:
        left += 20
    if pressed[pygame.K_UP]:
        right -= 20
    elif pressed[pygame.K_DOWN]:
        right += 20

    x += velx
    y += vely

    if x < 0 or x > 1280:
        done = True
    if y <= 20 or y >= 700:
        vely = -vely
    
    if (x <= 150 and left <= y <= left+200) or (x >= 1160 and right <= y <= right+200):
        velx = -velx
        score += 1

        if velx>0: sign=1
        elif velx<0: sign=-1
        else: sign=0
        velx += random.gauss(sign,1)

        if vely>0: sign=1
        elif vely<0: sign=-1
        else: sign=0
        vely += random.gauss(sign,1)

    if left < 0:
        left = 0
    elif left > 520:
        left = 520
    if right < 0:
        right = 0
    elif right > 520:
        right = 520

    screen.fill(black)

    pygame.draw.rect(screen, white, pygame.Rect(100,left,30,200))
    pygame.draw.rect(screen, white, pygame.Rect(1180,right,30,200))
    pygame.draw.circle(screen, white, (x,y), 20)

    text = comicsans.render(str(score), True, white)
    textbox = text.get_rect()
    textbox.center = (640,100)
    screen.blit(text, textbox)

    clock.tick(30)
    pygame.display.flip()