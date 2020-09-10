import pygame
from setting import *
from player_class import *
from enemy_class import *
import sys

pygame.init()
vec = pygame.math.Vector2


class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        
        # CLOCK TO CONTROL THE FRAMES PER SECOND
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'start'

        
        # CONSIERING 28 PART HORIZONTALLY OF THE SCREEN
        self.cell_width = MAZE_WIDTH//28
        
        # CONSIERING 30 PART VERTICALLY OF THE SCREEN
        self.cell_height = MAZE_HEIGHT//30
        
        # INTIALIZING THE WALL ARRAY
        self.walls = []
        
        # INTIALIZE THE COINS ARRAY
        self.coins = []

        # INTIALIZE A LIST OF ENIMIES
        self.enemies = []

        # INTILIZE THE LIST OF STARTING POSITION
        # OF ALL THE FOUR ENEMIES
        self.e_pos = []

        # INITIAL POSITION OF THE PACMAN
        # IN THE GRID OF THE MAZE
        # SET IN THE LOAD FUNCTION
        # BASED ON THE WALLS.TXT
        self.p_pos = None
        
        # TO LOAD ALL THE IMAGES BEFORE STARTING THE GAME
        # OTHERWISE THE IMAGES WILL LOAD FRAME BY FRAME
        self.load()

        # INITIALIZE THE PLAYER(PACMAN)
        # ARGS : STARTING COORDINATES
        # PASS THE APP ITSELF
        # INCE THE STARTING COORDINATES ARE PROVIDED IN THE LOAD FUNCTION
        # THAN THE PLAYER CLASS IS INTITIALIZED AFTER CALLING THE RETURN FUNCTION
        self.player = Player(self, self.p_pos)   

        # FUNCTION TO CREATE THE ENEMIES
        self.create_enemies()     
    


    def run(self):
        while self.running:
            if self.state == 'start':
                self.start_events()
                self.start_update()
                self.start_draw()
            elif self.state == 'playing':
                self.playing_events()
                self.playing_update()
                self.playing_draw() 
            else:
                self.running = False

            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()

############################## HELPER FUNCTIONS ##########################
    def draw_text(self, words, screen, pos, size, color, font_name, centered = False):
        # SET THE FONT AND SIZE
        font = pygame.font.SysFont(font_name, size, italic=1, bold=1) 

        # FORM THE GIVEN TEXT IN THE FONT WE INITIALIZED
        # ARGS: WORDS TO BE DISPLAYED
        #       FALSE FOR ANTIALIAS
        #       COLOR OF THE TEXT
        text = font.render(words, False, color)

        # GET THE SIZE OF THE TEXT WRITTEN
        # RETURNS A TUPLE OF (WIDTH, HEIGHT)
        text_size = text.get_size() 
        if centered:
            # CENETER THE TEXT TO THE GIVEN POSITION
            pos[0] = pos[0] - text_size[0]// 2
            pos[1] = pos[1] - text_size[1]// 2

        # FUNCTION TO DISPLAY ON THE SCREEN 
        screen.blit(text, pos)

    def load(self):
        # SET THE BACKGROUND IMAGE TO THE MAZE 
        self.background = pygame.image.load('maze.png')
        # SCALE THE BACKGROUND TO THE WIDTH AND HEIGHT OF THE SCREEN WINDOW
        self.background = pygame.transform.scale(self.background, (MAZE_WIDTH, MAZE_HEIGHT))

        # LOAD THE WALL MATRIX TEXT FILE
        # CREATING THE WALL LIST
        with open("walls.txt", 'r') as file:
            for y_index, line in enumerate(file):
                for x_index, char in enumerate(line):
                    # IF CHAR EQUAL TO 1
                    # IT REFERS TO A WALL
                    # APPEND IT TO THE WALL LIST
                    if char == "1":
                        self.walls.append(vec(x_index, y_index))
                    elif char == "C":
                        # IF CHAR EQUAL TO 2
                        # IT REFERS TO A COIN
                        # APPEND IT TO THE COINT LIST
                        self.coins.append(vec(x_index, y_index))
                    elif char == "P":
                        # IF CHAR EQUALS TO P THEN
                        # IT REFERS TO THE START POSITION OF THE PACMAN
                        # MARK THIS POSITION AS THE STARTING POINT
                        self.p_pos = vec(x_index, y_index)
                        # PLAYER_START_POSITION = vec(x_index, y_index)
                    elif char in ["2","3","4","5"]:
                        # IF CHAR IS THIS LIST
                        # THAN THE CHAR REFERS TO THE STARTING POSTION
                        # OF ANY ONE OF THE ENEMIES
                        self.e_pos.append(vec(x_index, y_index))
                    



    # METHOD TO INTIALIZE A ENEMY OBJECT
    # FROM THE ENEMY CLASS DEFINED IN ENEMY_CLASS.PY
    # ARGS : APP CLASS VARIABLE, STARTING POSITION OF THE ENEMY
    def create_enemies(self):
        for index, pos in enumerate(self.e_pos):
            self.enemies.append(Enemy(self, pos, index))


    def draw_grid(self):
        # CONSIDERING THE SCREEN IS DIVIDED INTO 28 PARTS HORIZONTALLY
        # SO THIS MADE OUR MAZE DIVIDED INTO A 28 X 30 MATRIX
        # CONSISTING OF WALLS AND OPEN PATH.
        for x in range(WIDTH//self.cell_width):
            # FUNCTION TO DRAW A LINE
            # ARGS : SCREEN, COLOR OF LINE, STARTING AND ENDPOINTS
            # HERE SCREEN REFERS TO THE MAZE BACKGROUND
            pygame.draw.line(self.background, GREY, (x*self.cell_width,0), (x*self.cell_width, HEIGHT) )

        # CONSIDERING THE SCREEN IS DIVIDED INTO 30 PARTS VERTICALLY
        for x in range(HEIGHT//self.cell_height):
            # FUNCTION TO DRAW A LINE
            # ARGS : SCREEN, COLOR OF LINE, STARTING AND ENDPOINTS
            # HERE SCREEN REFERS TO THE MAZE BACKGROUND
            pygame.draw.line(self.background, GREY, (0, x * self.cell_height), (WIDTH,x*self.cell_height) )


        # VISUALIZE THE WALLS ADDED FROM THE WALLS TEXT FILE
        for wall in self.walls:
            # DRAW AN OPAQUE RECTANGLE AT EVERY CORRDINATE OF THE WALL
            pygame.draw.rect(
                self.background, GREY, 
                (wall.x * self.cell_width, wall.y * self.cell_height, self.cell_width, self.cell_height)
            )

        # # VISUALIZE THE COINS ADDED FROM THE WALLS TEXT FILE
        # for coin in self.coins:
        #     # DRAW AN OPAQUE RECTANGLE AT EVERY CORRDINATE OF THE COIN
        #     pygame.draw.rect(
        #         self.background, ORANGE, 
        #         (
        #             coin.x * self.cell_width, 
        #             coin.y * self.cell_height, 
        #             self.cell_width, 
        #             self.cell_height
        #         )
        #     )

############################## INTRO FUNCTIONS ##########################

    def start_events(self):
        for event in pygame.event.get():
            # IF EVENT QUIT THEN STOP THE GAME
            if event.type == pygame.QUIT:
                self.running = False
            # IF SPACEBAR IS PRESSED THEN GAME IS STARTED
            # I.E. THE MODE IS SET TO PLAYING 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = 'playing'
    
    def start_update(self):
        pass

    def start_draw(self):

        # SET SCREEN COLOR TO BLACK
        # BLACK IS DEFINED IN SETTING FILE
        self.screen.fill(BLACK)

        # HELPER FUNCTION TO DRAW TEXT ON THE PASSED SCREEN
        # ARGS : TEXT, SCREEN, POSITION OF TEXT, TEXT SIZE, COLOR OF TEXT, FONT OF TEXT, CENTERED 
        self.draw_text('HIGH SCORE', self.screen,[5,10], START_TEXT_SIZE, WHITE, START_FONT,centered = False)


        self.draw_text('PUSH SPACEBAR', self.screen,[WIDTH//2,HEIGHT//2 - 50], START_TEXT_SIZE, ORANGE, START_FONT,centered = True)
        self.draw_text('1 PLAYER ONLY', self.screen,[WIDTH//2,HEIGHT//2 + 50], START_TEXT_SIZE, WHITE, START_FONT, centered = True)
        self.draw_text('CAPIP INNOVATIONS', self.screen,[WIDTH//2,HEIGHT//2 + 100], START_TEXT_SIZE, SKYBLUE, START_FONT, centered = True)
        
        pygame.display.update()


############################## PLAYING FUNCTIONS ##########################

    def playing_events(self):
        for event in pygame.event.get():
            
            # IF EVENT QUIT THEN STOP THE GAME
            if event.type == pygame.QUIT:
                self.running = False

            # FOR THE ARROW KEY PRESS EVENT
            if event.type == pygame.KEYDOWN:
                # IF LEFT ARROW IS PRESSED 
                if event.key == pygame.K_LEFT:
                    # PASSING A VEC(-1,0)
                    # RESEMBLING MOVEMENT TO LEFT FROM ORIGIN
                    self.player.move(vec(-1,0))

                # IF LEFT ARROW IS PRESSED 
                if event.key == pygame.K_RIGHT:
                    # PASSING A VEC(1,0)
                    # RESEMBLING MOVEMENT TO RIGHT FROM ORIGIN                    
                    self.player.move(vec(1,0))

                # IF UP ARROW IS PRESSED                 
                if event.key == pygame.K_UP:
                    # PASSING A VEC(0,-1)
                    # RESEMBLING MOVEMENT TO UP FROM ORIGIN  
                    # WHEN YOU G UP PIEL POSITION REDUCES
                    # THUS, Y IS NEGATIVE                    
                    self.player.move(vec(0,-1))

                # IF DOWN ARROW IS PRESSED
                if event.key == pygame.K_DOWN:
                    # PASSING A VEC(0,1)
                    # RESEMBLING MOVEMENT TO DOWN FROM ORIGIN                        
                    self.player.move(vec(0,1))

    
    def playing_update(self):

        # UPDATING THE PLAYER ON THE MAZE SCREEN
        self.player.update()

       # UPDATING ALL THE ENEMIES ON THE MAZE SCREEN
        for enemy in self.enemies:
            enemy.update()


    def playing_draw(self):
        # NEED T0 FILL THE SCREEN WITH BLACK
        # SO THAT PREVIOUS WINDOW CONTENT IS FLUSHED OUT
        self.screen.fill(BLACK)



        # REPRESENT PLAYING ARENA SCREEN WITH THE MAZE IMAGE AT BACKGROUND
        # WE STARTED THE BAKGROUND FROM (TOP_BOTTOM_BUFFER//2,TOP_BOTTOM_BUFFER//2) PIXEL
        # TO CENTER THE MAZE IMAGE IN THE GAME WINDOW
        self.screen.blit(self.background, (TOP_BOTTOM_BUFFER//2, TOP_BOTTOM_BUFFER//2))
       
       
        # FUNCTION TO SHOW THE COINS
        self.draw_coins()


        # FUNCTION TO SHOW GRID LINES ON THE MAZE
        # TO UNDERSTAND HOW THE PACMAN WILL MOVE
        self.draw_grid()

        # TO SHOW THE HIGH SCORE IN THE GAME PLAYING AREA
        self.draw_text('HIGH SCORE : 000', self.screen, [30,5], 18, WHITE, START_FONT, centered=False)

        # TO SHOW THE CURRENT SCORE IN THE GAME PLAYING AREA
        self.draw_text('CURRENT SCORE : {}'.format(self.player.current_score), self.screen, [420,5], 18, WHITE, START_FONT, centered=False)

        # CONSTRUCT PLAYER ON THE MAZE SCREEN
        self.player.draw()

        # CONSTRUCT ALL THE ENEMIES ON THE MAZE SCREEN
        for enemy in self.enemies:
            enemy.draw()

        pygame.display.update()


    def draw_coins(self):
        for coin in self.coins:
            pygame.draw.circle(
                self.screen,
                ORANGE,
                (
                    int(coin.x * self.cell_width) + self.cell_width//2 + TOP_BOTTOM_BUFFER//2,
                    int(coin.y * self.cell_height) + self.cell_height//2 + TOP_BOTTOM_BUFFER//2
                ),
                5
            )