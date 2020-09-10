import pygame
import random
from setting import *

vec = pygame.math.Vector2

class Enemy:

    def __init__(self, app, pos, number):
        
        self.app = app
        # POSITION ON THE WINDOW
        self.grid_pos = pos
        # CELL BLOCK POSITION IN THE MAZE
        self.pix_pos = self.get_pix_pos()
        # DEFINES WHICH TYPE OF PERSONALITY THE ENEMY COMPRISES
        self.number = number
        # DEFINE COLOR FOR DIFFERENT TYPES OF ENEMY
        self.color = self.set_color()
        # DIRECTION VARIABLE FOR THE ENEMY MOVEMENT
        self.direction = vec(0,-1)
        # DEFINE THE ENEMY PERSONALITY 
        self.personality = self.set_personality()

    def update(self):
        self.pix_pos += self.direction

        if self.time_to_move():
            self.move()


        # SETTING GRID POSITION IN REFERENCE TO THE PIXEL POSTION
        self.grid_pos[0] = (self.pix_pos[0] - TOP_BOTTOM_BUFFER + self.app.cell_width//2)// self.app.cell_width + 1
        self.grid_pos[1] = (self.pix_pos[1] - TOP_BOTTOM_BUFFER + self.app.cell_width//2)// self.app.cell_height + 1






    def draw(self):
        # CONSTRUCT THIS ENEMY AT THE GIVEN PIXEL POSITION
        pygame.draw.circle(
            self.app.screen, 
            self.color, 
            (int(self.pix_pos.x), int(self.pix_pos.y)), 
            9
        )

    def time_to_move(self):
        # LOGIC FOR HOLDING THE PAC INTO THE CENTER OF A CELL BLOCK
        # CURRENTLY IT IS A TEMPORARY SOLUTION
        if int(self.pix_pos.x + TOP_BOTTOM_BUFFER//2) % self.app.cell_width == 0:
            # print("X IS IN LINE")
            if self.direction == vec(1,0) or self.direction == vec(-1,0):
                return True

        if int(self.pix_pos.y + TOP_BOTTOM_BUFFER//2) % self.app.cell_height == 0:
            # print("X IS IN LINE") 
            if self.direction == vec(0,1) or self.direction == vec(0,-1):
                return True


    def move(self):
        if self.personality == "random":
            self.direction = self.get_random_direction()

    def get_random_direction(self):
        # LOOP TO MAKE SURE THAT 
        # EVEN IF THE GHOST HIT A WALL
        # IT DOESN'T STOP I.E.
        # NEW DIRECTION IS GIVEN
        while True:
            self.number = random.randint(-2,1)
            if self.number == -2:
                x_dir, y_dir = 1, 0
            elif self.number == -1:
                x_dir, y_dir = 0, 1
            elif self.number == 0:
                x_dir, y_dir = -1, 0
            else:
                x_dir, y_dir = 0, -1
            
            next_pos = vec(self.grid_pos.x + x_dir, self.grid_pos.y + y_dir)

            if next_pos not in self.app.walls:
                break

        return vec(x_dir, y_dir)






    # METHOD TO GET THE EXACT CELL BLOCK POSITION IN THE GRID MATRIX
    def get_pix_pos(self):
        return vec(
                (self.grid_pos.x * self.app.cell_width) 
                + TOP_BOTTOM_BUFFER//2 + self.app.cell_width//2 , 
                (self.grid_pos.y * self.app.cell_height) 
                + TOP_BOTTOM_BUFFER//2 + self.app.cell_height//2
            )  


    # METHOD TO SET THE COLOR OF THE ENEMY
    # BASED ON THE NUMBER ASSIGNED TO IT
    def set_color(self):
        if self.number == 0 or self.number == 3:
            return RED
        elif self.number == 1 or self.number == 2:
            return SKYBLUE


    # METHOD TO SET THE PERSONALITY OF THE ENEMY 
    # BASED ON THE NUMBER ASSIGNED TO IT
    def set_personality(self):
        if self.number == 0 or self.number == 3:
            # ENEMY 0 AND 3 WILL CONSIST OF SPEEDY AND DIRECTED MOVEMENT
            return "speedy"
        elif self.number == 1 or self.number == 2:
            # ENEMY 1 AND 2 WILL CONSIST OF RANDOM MOVEMENT
            return "random"
