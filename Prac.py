import sys, pygame
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
color = 0, 0, 0
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Project")

x = pygame.image.load("E:\Microsoft VS code\Python-Codes\Game\google.png")
xrect = x.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    xrect = xrect.move(speed)
    if xrect.left < 0 or xrect.right > width:
        speed[0] = -speed[0]
    if xrect.top < 0 or xrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(color)
    screen.blit(x, xrect)
    pygame.display.flip()