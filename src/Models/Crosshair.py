import pygame
from Nunchuck.Controller import Controller

class Crosshair:
    def __init__(self, screen, shot_cooldown = 10):
        self.screen = screen
        self.shot_cooldown = shot_cooldown
        self.Nunchuck_Controller = Controller()


    @property
    def x(self):
        return self.Nunchuck_Controller.x

    @property
    def y(self):
        return self.Nunchuck_Controller.y

    @property
    def z(self):
        return self.Nunchuck_Controller.z

    def draw(self):
        x = self.x
        y = self.y
        
        horizontal_points = [(x-20, y), (x+20, y)]
        vertical_points = [(x, y-20), (x, y+20)]
        pygame.draw.aalines(self.screen, (0, 0, 0), True, horizontal_points)
        pygame.draw.aalines(self.screen, (0, 0, 0), True, vertical_points)


    def shot(self):
        if self.z:
            if self.shot_cooldown == 10:
                self.shot_cooldown = 0
                return True
            
        if self.shot_cooldown != 10:
            self.shot_cooldown += 1

        return False
                
            
        
