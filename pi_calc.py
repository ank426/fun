import pygame
import math

pygame.init()
screen = pygame.display.set_mode((1800,720))
clock = pygame.time.Clock()
pygame.event.set_allowed([])

white = (255,255,255)
black = (0,0,0)
grey = (128,128,128)

size = 100
x = 1500
vel = 0
X = 1800
Vel = -0.0001  # -0.00003
m = 1
M = 100**5  # 6

c = 0
comicsans = pygame.font.SysFont('comicsans', 50)

arial = pygame.font.SysFont('arial', 25)

mtext = arial.render(str(m), True, black)
mbox = mtext.get_rect()
Mtext = arial.render('100^' + str(round(math.log(M, 100))), True, black)
Mbox = Mtext.get_rect()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    for i in range(21859):
        x += vel
        X += Vel

        if x < 50:
            vel = abs(vel)
            c += 1

        if X < x + size:
            vel, Vel = (2*M*Vel + (m-M)*vel) / (m+M), (2*m*vel + (M-m)*Vel) / (m+M)
            c += 1

    screen.fill(black)
    pygame.draw.rect(screen, grey, pygame.Rect(0, 0, 50, 720))
    pygame.draw.rect(screen, grey, pygame.Rect(0, 670, 1800, 50))
    pygame.draw.rect(screen, white, pygame.Rect(x, 670-size, size, size))
    pygame.draw.rect(screen, white, pygame.Rect(X, 670-size, size, size))

    text = comicsans.render(str(c), True, white)
    textbox = text.get_rect()
    textbox.center = (900,100)
    screen.blit(text, textbox)

    mbox.center = (x + size/2, 670 - size/2)
    screen.blit(mtext, mbox)
    Mbox.center = (X + size/2, 670 - size/2)
    screen.blit(Mtext, Mbox)

    print(clock.get_time())
    clock.tick(60)
    pygame.display.flip()