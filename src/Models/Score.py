import pygame

class Score:
    def __init__(self, screen):
        self.screen = screen
        self.actual_score = 0
        pygame.font.init()
        self.score_font = pygame.font.SysFont('Comic Sans MS', 30)

    def update(self, shot_value):
        self.actual_score += shot_value

    def resetScore(self):
        self.actual_score = 0

    def drawLastScore(self, score):
        textSurface = self.score_font.render('Your Score: ' + str(score), False, (0, 0, 0))
        self.screen.blit(textSurface, (320, 150))

    def draw(self):
        textSurface = self.score_font.render('Score: ' +str(self.actual_score), False, (0, 0, 0))
        self.screen.blit(textSurface, (670, 5))

    
