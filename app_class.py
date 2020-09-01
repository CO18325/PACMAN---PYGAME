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
    
    def run(self):
        while self.running:
            if self.state == 'start':
                self.start_events()
                self.start_update()
                self.start_draw()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()

############################## HELPER FUNCTIONS ##########################
    def draw_text(self, words, screen, pos, size, color, font_name):
        # SET THE FONT AND SIZE
        font = pygame.font.SysFont(font_name, size, italic=1) 

        # FORM THE GIVEN TEXT IN THE FONT WE INITIALIZED
        # ARGS: WORDS TO BE DISPLAYED
        #       FALSE FOR ANTIALIAS
        #       COLOR OF THE TEXT
        text = font.render(words, False, color)

        # GET THE SIZE OF THE TEXT WRITTEN
        # RETURNS A TUPLE OF (WIDTH, HEIGHT)
        text_size = text.get_size() 

        # CNETER THE TEXT TO THE GIVEN POSITION
        pos[0] = pos[0] - text_size[0]// 2
        pos[1] = pos[1] - text_size[1]// 2
        screen.blit(text, pos, )


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
        # ARGS : TEXT, SCREEN, POSITION OF TEXT, TEXT SIZE, COLOR OF TEXT, FONT OF TEXT
        self.draw_text('PUSH SPACEBAR', self.screen,[WIDTH//2,HEIGHT//2], START_TEXT_SIZE, ORANGE, START_FONT)
        
        
        pygame.display.update()