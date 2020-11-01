import pygame
from Nunchuck.Controller import Controller

class Crosshair:
    def __init__(self, screen, shot_cooldown = 10):
        self.screen = screen
        self.shot_cooldown = shot_cooldown
        self.Nunchuck_Controller = Controller()
        self.hole_position = (-10, -10) # 2 Values U simply cant see

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
        
        pygame.draw.circle(self.screen, (255, 255, 255), self.hole_position, 5)

    def shot(self):
        if self.z:
            if self.shot_cooldown == 10:
                self.shot_cooldown = 0
                self.hole_position = (self.x, self.y)
                return True
            
        if self.shot_cooldown != 10:
            self.shot_cooldown += 1

        return False
                
            
        
