import pygame
from setting import *

vec = pygame.math.Vector2 


'''
    IMPORTANT NOTE:
        // : MEANS TO RETRIVE THE QUOTIENT
        EXAMPLE : 
            10 // 3 = 3
'''

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

        # TO CHECK IF THERE IS A WALL IN THE DIRECCTION OF MOVEMENT
        # IT WILL BE INTIALLY TRUE
        self.able_to_move = True

        # VARIABLE TO STORE THE CURRENT SCORE
        # THIS SCORE WILL INCREMENT ON THE 
        # COSUMPTION OF THE COINS IN THE MAZE
        # INTIALLY IT WILL BE ZERO
        self.current_score = 0



    # METHOD TO GET THE EXACT CELL BLOCK POSITION IN THE GRID MATRIX
    def get_pix_pos(self):
        return vec(
                (self.grid_pos.x * self.app.cell_width) + TOP_BOTTOM_BUFFER//2 + self.app.cell_width//2 , 
                (self.grid_pos.y * self.app.cell_height) + TOP_BOTTOM_BUFFER//2 + self.app.cell_height//2
            )        



    def update(self):

        # IF NO WALL AHEAD
        # UPDATE PACMAN POSITION
        if self.able_to_move :
            # UPDATING THE POSITION OF THE PAC 
            # ACCORDING TO THE DIRECTION GIVEN
            self.pix_pos += self.direction 


        # LOGIC FOR HOLDING THE PAC INTO THE CENTER OF A CELL BLOCK
        # CURRENTLY IT IS A TEMPORARY SOLUTION
        if int(self.pix_pos.x + TOP_BOTTOM_BUFFER//2) % self.app.cell_width == 0:
            # print("X IS IN LINE")
            if self.direction == vec(1,0) or self.direction == vec(-1,0):
                if self.stored_direction != None:
                    self.direction = self.stored_direction
                
                # CHECK IF THERE IS ANY WALL IN THE NEXT MOVE
                self.able_to_move = self.can_move()
        if int(self.pix_pos.y + TOP_BOTTOM_BUFFER//2) % self.app.cell_height == 0:
            # print("X IS IN LINE") 
            if self.direction == vec(0,1) or self.direction == vec(0,-1):
                if self.stored_direction != None:
                    self.direction = self.stored_direction

                # CHECK IF THERE IS ANY WALL IN THE NEXT MOVE
                self.able_to_move = self.can_move()
        
        # METHOD TO EAT THE COIN IF THE 
        # PACMAN IS AT THE GRID POSITION OF THE COIN
        # AND THUS, INCREMENT THE SCORE
        if self.on_coin():
            self.eat_coin()        



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


    # METHOD TO IDENTIFY IF GRID POSITION
    # OF THE PACMAN IS CONTAINING A COIN
    def on_coin(self):
        if self.grid_pos in self.app.coins:
            return True

        return False
    

    # METHOD TO EAT THE COIN
    # I.E TO INCREMENT THE CURRENT SCORE AND
    # REMOVE THE CORRESPONDING COIN FROM THE MAZE 
    def eat_coin(self):
        self.app.coins.remove(self.grid_pos)
        self.current_score += 10



    # FUNCTION TO STORE THE DIRECTION GIVEN 
    def move(self, direction):
        #self.direction = direction
        # ABOVE LINE REPLACED BY :
        # IT IS TO KEEP THE PAC IN RIGHT AND ACCURATE PATH
        self.stored_direction = direction


    # METHOD TO CHECK IF THERE IS A WALL AHEAD OF PACMAN
    def can_move(self):
        # WE WILL CHECK FOR EACH WALL IN THE DEFINED WALL LIST
        for wall in self.app.walls:
            # IF GRID POSITION + DIRECTION IS EQUAL TO ANY WALL 
            # THEN WE RETURN FALSE
            if vec(self.grid_pos + self.direction) == wall:
                return False
        # IF NO WALL IS FOUND THEN WE RETURN TRUE
        # INDICATING THE DIRECTION IS VALID
        return True

    
       









