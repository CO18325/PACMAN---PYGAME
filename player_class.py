import pygame
from setting import *

vec = pygame.math.Vector2 

# PLAYER CLASS TO DEFINE GAME PACMAN
class Player:
    def __init__(self, app, pos):
        self.app = app

        # UNDERSTAND THESE GRID AND PIXEL POSITIONS IN DETAIL LATER
        # ALSO NEED TO UNDERSTAND Vector2 OF PYGAME LIBRARY
        self.grid_pos = pos
        self.pix_pos = vec((self.grid_pos.x * self.app.cell_width) + TOP_BOTTOM_BUFFER//2 + self.app.cell_width//2 , 
        (self.grid_pos.y * self.app.cell_height) + TOP_BOTTOM_BUFFER//2 + self.app.cell_height//2)

        print(self.grid_pos, self.pix_pos)

    def update(self):
        pass

    def draw(self):
        # CONSTRUCT THE PACMAN
        # ARGS : SCREEN, COLOR, POSITION TO BE PLACED, RADIUS 
        # IT WILL BE CHANGED LATER WITH AN IMAGE
        # THE POSITION GIVEN SHOULD BE AN INTEGER ONLY
        pygame.draw.circle(self.app.screen, PLAYER_COLOR, (int(self.pix_pos.x), int(self.pix_pos.y)), self.app.cell_width//2 - 2)
