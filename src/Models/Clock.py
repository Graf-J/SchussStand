import pygame
import time
import threading

class Clock:
    def __init__(self, screen):
        self.screen = screen
        self.time = 60
        pygame.font.init()
        self.clock_font = pygame.font.SysFont('Comic Sans MS', 30)

    def startClockThread(self):
        while self.time != 0:
            time.sleep(1)
            self.time -= 1

    def start(self):
        self.t = threading.Thread(target=self.startClockThread)
        self.t.start()

    def hasTime(self):
        if self.t.is_alive():
            return True
        else:
            return False

    def resetTime(self):
        self.time = 60

    def draw(self):
        textSurface = self.clock_font.render('Time: ' + str(self.time), False, (0, 0, 0))
        self.screen.blit(textSurface, (5, 5))
