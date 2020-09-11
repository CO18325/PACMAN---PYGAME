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
        self.direction = vec(0,0)
        # DEFINE THE ENEMY PERSONALITY 
        self.personality = self.set_personality()
        # SPEED VARIABLE FOR THE ENEMY OBJECTS
        # SET TO 1 JUST TO INTIALIZE, 
        # WILL CHANGE AT THE TIME OF PERSONALITY SELECTION
        self.speed = 1 


    def update(self):

        if self.app.player.grid_pos != self.grid_pos:

            self.pix_pos += self.direction * self.speed

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
            if self.direction == vec(1,0) or self.direction == vec(-1,0) or self.direction == vec(0,0):
                return True

        if int(self.pix_pos.y + TOP_BOTTOM_BUFFER//2) % self.app.cell_height == 0:
            # print("X IS IN LINE") 
            if self.direction == vec(0,1) or self.direction == vec(0,-1) or self.direction == vec(0,0):
                return True


    def move(self):
        if self.personality == "random":
            self.direction = self.get_random_direction()
        
        if self.personality == "speedy":
            self.direction = self.get_path_direction()


    # METHOD T SET PATH FOR INTELLIGENT ENEMY
    def get_path_direction(self):
        next_cell = self.find_next_cell_in_path()
        x_dir = next_cell[0] - self.grid_pos[0]
        y_dir = next_cell[1] - self.grid_pos[1]
        return vec(x_dir, y_dir)


    # METHOD TO FINC THE DIRECTION FOR THE INTELLIGIENT GHOST
    # IT USES THE BREADTH FIRST SEARCH ALGORITHM 
    # TO HELP THE ENEMY TO GET CLOSER TO THE PAC
    def find_next_cell_in_path(self):
        # CALL THE BFS METHOD
        # ARGUMENTS :
        #       STARTING POSITION (I.E ENEMY POSITION)
        #       TARGET POSITION (I.E PAC POSITION)
        path = self.BFS(
                [int(self.grid_pos.x), int(self.grid_pos.y)],
                [int(self.app.player.grid_pos.x), int(self.app.player.grid_pos.y)] 
            )

        return path[1]
        

    def BFS(self, start, target):

        # GRID RESEMEBLING OUR GAME MAZE
        grid = [[0 for x in range(28)] for x in range(30)]

        # ADD THE WALL POSITIONS IN THIS GRID
        for cell in self.app.walls:
            if cell.x < 28 and cell.y <30:
                grid[int(cell.y)][int(cell.x)] = 1
            
        # INTIATE THE BFS QUEUE
        queue = [start]
        # TO STORE THE PATHH
        path = []
        # TO STORE THE CELLS WHICH ARE VISITED
        visited = []

        # LOOP UNTIL THE QUEUE IS NOT EMPTY
        while True:
            # CURRENT SOURCE
            current = queue[0]
            # POPPED THE CURRENT SOURCE FROM THE IMPLEMENTATION QUEUE
            queue.remove(queue[0])
            # MARK THE CELL AS VISITED
            visited.append(current)

            if current == target:
                break
            else:
                neighbours = [[0, -1], [1, 0], [0, 1], [-1, 0]]
                for neighbour in neighbours:
                    if neighbour[0] + current[0] >= 0 and neighbour[0] + current[0] < len(grid[0]):
                       if neighbour[1] + current[1] >= 0 and neighbour[1] + current[1] < len(grid):
                            next_cell = [neighbour[0] + current[0], neighbour[1] + current[1]]
                            if next_cell not in visited:
                                if grid[next_cell[1]][next_cell[0]] != 1:
                                    queue.append(next_cell)
                                    path.append({"Current": current, "Next": next_cell})
                                    
        shortest = [target]
        while target != start:
            for step in path:
                if step["Next"] == target:
                    target = step["Current"]
                    shortest.insert(0, step["Current"])
                                
        return shortest






    # GET THE DIRECTION FOR THE RANDOM ENEMY
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

            # IF NEXT CELL DUE TO RANDOM IS NOT A WALL 
            # BREAK FROM THE LOOP AND RETURN THE PIXEL POSITION
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
        if self.number == 0 or self.number == 1:
            return RED
        elif self.number == 2 or self.number == 3:
            return SKYBLUE


    # METHOD TO SET THE PERSONALITY OF THE ENEMY 
    # BASED ON THE NUMBER ASSIGNED TO IT
    def set_personality(self):
        if self.number == 0 or self.number == 1:
            # ENEMY 0 AND 3 WILL CONSIST OF SPEEDY AND DIRECTED MOVEMENT
            # DIRECTED ENEMY WILL HAVE NORMAL/SLOW SPEED
            self.speed = 1
            return "speedy"
        elif self.number == 3 or self.number == 2:
            # ENEMY 1 AND 2 WILL CONSIST OF RANDOM MOVEMENT
            # RANDOM ONE WILL BE THE FASTER ONES
            self.speed = 2
            return "random"
