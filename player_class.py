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
        self.pix_pos = self.get_pix_pos()
        self.direction = vec(1,0)
        # IT WILL BE USED FOR KEEPING THE PAC
        # INSIDE THE CENTER OF THE GRID MATRIX
        self.stored_direction = None
        # print(self.grid_pos, self.pix_pos)


    def update(self):
        self.pix_pos += self.direction 


        # LOGIC FOR HOLDING THE PAC INTO THE CENTER OF A CELL BLOCK
        # CURRENTLY IT IS A TEMPORARY SOLUTION
        if int(self.pix_pos.x + TOP_BOTTOM_BUFFER//2) % self.app.cell_width == 0:
            # print("X IS IN LINE")
            if self.direction == vec(1,0) or self.direction == vec(-1,0):
                if self.stored_direction != None:
                    self.direction = self.stored_direction

        if int(self.pix_pos.y + TOP_BOTTOM_BUFFER//2) % self.app.cell_height == 0:
            # print("X IS IN LINE") 
            if self.direction == vec(0,1) or self.direction == vec(0,-1):
                if self.stored_direction != None:
                    self.direction = self.stored_direction



        # FOR THE RED GRIP MOVEMENT
        self.grid_pos[0] = (self.pix_pos[0] - TOP_BOTTOM_BUFFER + self.app.cell_width//2)// self.app.cell_width + 1
        self.grid_pos[1] = (self.pix_pos[1] - TOP_BOTTOM_BUFFER + self.app.cell_width//2)// self.app.cell_height + 1


    def draw(self):
        # CONSTRUCT THE PACMAN
        # ARGS : SCREEN, COLOR, POSITION TO BE PLACED, RADIUS 
        # IT WILL BE CHANGED LATER WITH AN IMAGE
        # THE POSITION GIVEN SHOULD BE AN INTEGER ONLY
        pygame.draw.circle(self.app.screen, PLAYER_COLOR, (int(self.pix_pos.x), int(self.pix_pos.y)), self.app.cell_width//2 - 2)


        # DRAW A SQUARE TO NOTE DOWN THE CELL IN WHICH THE PACMAN IS CURRENTLY
        # A RED BLOCK CONSTANTLY TRACKING OUR PACMAN
        pygame.draw.rect(self.app.screen, RED, (
            self.grid_pos[0] * self.app.cell_width + TOP_BOTTOM_BUFFER//2 , 
            self.grid_pos[1] * self.app.cell_height + TOP_BOTTOM_BUFFER//2, 
            self.app.cell_width, self.app.cell_height
        ), 1)

    def move(self, direction):
        #self.direction = direction
        # ABOVE LINE REPLACED BY :
        # IT IS TO KEEP THE PAC IN RIGHT AND ACCURATE PATH
        self.stored_direction = direction


    def get_pix_pos(self):
        return vec(
                (self.grid_pos.x * self.app.cell_width) + TOP_BOTTOM_BUFFER//2 + self.app.cell_width//2 , 
                (self.grid_pos.y * self.app.cell_height) + TOP_BOTTOM_BUFFER//2 + self.app.cell_height//2
            )        
    
       









