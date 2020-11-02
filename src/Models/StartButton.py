import pygame

class StartButton:
    def __init__(self, screen):
        self.screen = screen
        pygame.font.init()
        self.start_font = pygame.font.SysFont('Comic Sans MS', 50)

    def checkHit(self, x, y):
        if x > 200-5 and x < 600+5:
            if y > 220-5 and y < 320+5:
                return True
            
        return False

    def draw(self):
        textSurface = self.start_font.render('Click here to Start', False, (0, 0, 0))
        pygame.draw.rect(self.screen, (0, 0, 255), [200, 220, 400, 100], False)
        self.screen.blit(textSurface, (250, 250))
