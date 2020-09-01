import pygame
from setting import *
import sys

pygame.init()
vec = pygame.math.Vector2


class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        # CLOCK TO CONTROL THE FRAMES PER SECOND
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'intro'
    
    def run(self):
        while self.running:
            if self.state == 'intro':
                self.intro_events()
                self.intro_update()
                self.intro_draw()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()

############################## INTRO FUNCTIONS ##########################

    def intro_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def intro_update(self):
        pass

    def intro_draw(self):
        # self.screen.fill((255,255, 255))
        pygame.display.update()