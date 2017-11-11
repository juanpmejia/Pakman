import sys
import pygame
from pacman import *

# Some constants
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

# Main game class
class Game():

    # Initialization
    def __init__(self):
        # Set game title
        pygame.display.set_caption("Pakman")
        # Initialize game variables
        self.clock = pygame.time.Clock()
        self.quit = 0

        # Initialize game screen
        self.screen = pygame.display.set_mode(DISPLAY_WIDTH,DISPLAY_HEIGHT)

        # Initialize players
        self.pacman = Pacman('Assets/pacman.png')

        allsprites = pygame.sprite.Group()
        allsprites.add(pacman)

        self.mainLoop()

    # Check for game events
    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  
                self.quit = 1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.quit = 1
                    
    # Movement logic for the player
    def movePlayer(self):
        pressed = pygame.key.get_pressed()                     
        dir = 0  

        if pressed[pygame.K_UP]:
            dir = 270
        elif pressed[pygame.K_DOWN]:
            dir = 90
        elif pressed[pygame.K_LEFT]:
            dir = 180
        elif pressed[pygame.K_RIGHT]:
            dir = 0
                
    # Main game loop
    def mainLoop(self):

        while (self.quit != 1):
            # Clear the screen
            screen.fill(black)

            # Cinematic 10 fps
            self.clock.tick(10)

            self.checkEvents()
            pacman.update()
            
            # Draw Everything
            allsprites.draw(screen)

            # Flip the screen and show what we've drawn
            pygame.display.flip()

        text = font.render("Game Over", True, white)
        textpos = text.get_rect(background.get_width()/2)
        textpos.top = 300
        screen.blit(text, textpos)

pygame.init()
Game()
pygame.quit()
sys.exit()
