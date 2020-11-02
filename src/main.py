import pygame
from Models.Crosshair import Crosshair
from Models.Target_Matrix import Target_Matrix
from Models.Score import Score
from Models.Clock import Clock
from Models.StartButton import StartButton

pygame.init()
screen = pygame.display.set_mode((780, 520))
screen.fill((169, 87, 15))
pygame.display.set_caption('Schiesstand')
clock = pygame.time.Clock()

Crosshair = Crosshair(screen)
StartButton = StartButton(screen)
Target_Matrix = Target_Matrix(screen)
Score = Score(screen)
Clock = Clock(screen)

def redrawGameWindow():
    pygame.display.update()
    screen.fill((169, 87, 15))

def menuLoop(score = 0):
    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        if Crosshair.shot():
            if(StartButton.checkHit(Crosshair.x, Crosshair.y)):
                run = False
                Clock.resetTime()
                Score.resetScore()
                gameLoop()

        StartButton.draw()
        Score.drawLastScore(score)
        Crosshair.draw()
        
        redrawGameWindow()

# GameLoop
def gameLoop():
    Clock.start()
    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        if Crosshair.shot():
            shot_value = Target_Matrix.checkHit(Crosshair.x, Crosshair.y)
            Score.update(shot_value)

        if not Clock.hasTime():
            run = False
            menuLoop(Score.actual_score)

        Target_Matrix.drawTarget()
        Crosshair.draw()
        Score.draw()
        Clock.draw()
        
        redrawGameWindow()

#Start MenuLoop
menuLoop()
