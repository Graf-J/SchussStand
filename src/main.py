import pygame
from Models.Crosshair import Crosshair
from Models.Target_Matrix import Target_Matrix

pygame.init()
screen = pygame.display.set_mode((780, 520))
screen.fill((169, 87, 15))
pygame.display.set_caption('Schiesstand')
clock = pygame.time.Clock()

Crosshair = Crosshair(screen)
Target_Matrix = Target_Matrix(screen)

def redrawGameWindow():
    pygame.display.update()
    screen.fill((169, 87, 15))

# GameLoop
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

    if Crosshair.shot():
        Target_Matrix.checkHit(Crosshair.x, Crosshair.y)

    Target_Matrix.drawTarget()
    Crosshair.draw()
    
    redrawGameWindow()
