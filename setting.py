from pygame.math import Vector2 as vec

# SCREEN SETTINGS

# DIMENSIONS DOUBLE THAN THE ORIGINAL PROBLEM
WIDTH = 610
HEIGHT = 670

# AMOUNT OF SPACE ABOVE AND BELOW THE MAZE
# TO ADD OTHER NECCESSARY INFORMATION
TOP_BOTTOM_BUFFER = 50

# DIMENSIONS OF THE MAZE
MAZE_WIDTH = WIDTH - TOP_BOTTOM_BUFFER
MAZE_HEIGHT = HEIGHT - TOP_BOTTOM_BUFFER

#FRAMES PER SECOND
FPS = 60 

# COLOR SETTINGS

# RGB FORMAT
BLACK = (0,0,0) 
ORANGE = (170,132,58)
WHITE = (255, 255, 255)
SKYBLUE = (44, 167, 198)
RED = (208,22,22)
GREY = (107, 107, 107)
PLAYER_COLOR = (190, 194, 15)
# FONT SETTINGS
START_TEXT_SIZE = 20
START_FONT = 'Calibri'


# PLAYER SETTINGS

# INITIAL POSITION OF THE PACMAN
# IN THE GRID OF THE MAZE
PLAYER_START_POSITION = vec(1,1)

# MOB SETTINGS
