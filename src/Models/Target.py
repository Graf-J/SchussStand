import pygame

class Target:
    def __init__(self, screen):
        self.screen = screen
        self.x = 390
        self.y = 260
    
    def draw(self):
        pygame.draw.circle(self.screen, (0, 0, 0), (self.x, self.y), 40)
        pygame.draw.circle(self.screen, (255, 0, 0), (self.x, self.y), 39)
        pygame.draw.circle(self.screen, (255, 255, 255), (self.x, self.y), 26)
        pygame.draw.circle(self.screen, (255, 0, 0), (self.x, self.y), 13)
        pygame.draw.circle(self.screen, (0, 0, 0), (self.x, self.y), 5)
        
        
    
