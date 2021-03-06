import random
import math
from Models.Target import Target

class Target_Matrix:
    def __init__(self, screen):
        self.screen = screen
        self.target_exists = False
        self.Target = Target(screen)

    def drawTarget(self):
        self.Target.draw()

    def changeTargetPosition(self):
        self.Target.x = random.randint(50, 730)
        self.Target.y = random.randint(50, 470)
                 
    def checkHit(self, x, y):
        d = math.sqrt((x - self.Target.x)**2 + (y - self.Target.y)**2)
        if d > 40 + 5: # 5 is the radius of my Bullet
            return -1
        else:
            self.changeTargetPosition()
            if d < 5+5:
                return 3
            elif d < 24+5:
                return 2
            elif d < 41+5:
                return 1
