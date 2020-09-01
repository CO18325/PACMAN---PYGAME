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
        self.state = 'start'

        # CONSIERING 28 PART HORIZONTALLY OF THE SCREEN
        self.cell_width = WIDTH//28
        # CONSIERING 30 PART VERTICALLY OF THE SCREEN
        self.cell_height = HEIGHT//30
        
        # TO LOAD ALL THE IMAGES BEFORE STARTING THE GAME
        # OTHERWISE THE IMAGES WILL LOAD FRAME BY FRAME
        self.load()
    
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
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))


    def draw_grid(self):
        # CONSIDERING THE SCREEN IS DIVIDED INTO 28 PARTS HORIZONTALLY
        for x in range(WIDTH//self.cell_width):
            # FUNCTION TO DRAW A LINE
            # ARGS : SCREEN, COLOR OF LINE, STARTING AND ENDPOINTS
            pygame.draw.line(self.screen, GREY, (x*self.cell_width,0), (x*self.cell_width, HEIGHT) )

        # CONSIDERING THE SCREEN IS DIVIDED INTO 30 PARTS VERTICALLY
        for x in range(HEIGHT//self.cell_height):
            # FUNCTION TO DRAW A LINE
            # ARGS : SCREEN, COLOR OF LINE, STARTING AND ENDPOINTS
            pygame.draw.line(self.screen, GREY, (0, x * self.cell_height), (WIDTH,x*self.cell_height) )

        # SO THIS MADE OUR MAZE DIVIDED INTO A 28 X 30 MATRIX
        # CONSISTING OF WALLS AND OPEN PATH.


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

    
    def playing_update(self):
        pass

    def playing_draw(self):

        # REPRESENT PLAYING ARENA SCREEN WITH THE MAZE IMAGE AT BACKGROUND
        # WE STARTED THE BAKGROUND FROM (0,0) PIXEL
        self.screen.blit(self.background, (0,0))

        # FUNCTION TO SHOW GRID LINES ON THE MAZE
        # TO UNDERSTAND HOW THE PACMAN WILL MOVE
        self.draw_grid()
        pygame.display.update()