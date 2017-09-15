import sys
import pygame
from maze import *
from pacman import *
from ghost import *

# Some constants
COLOR_BLACK = (0,0,0)
COLOR_BLUE = (0,0,255)
TILESIZE = 25

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
        self.maze = Maze()
        self.disp = pygame.display.set_mode((self.maze.getWidth()*TILESIZE,self.maze.getHeight()*TILESIZE))

        # Initialize players
        self.pacman = Pacman(1,1,self.disp,'Assets/pacman.png',TILESIZE)
        self.ghostRed = Ghost(3,21,RED,self.disp,'Assets/red.png',TILESIZE)
        self.ghostBlue = Ghost(8,6,BLUE,self.disp,'Assets/blue.png',TILESIZE)
        self.ghostPink = Ghost(11,21,PINK,self.disp,'Assets/pink.png',TILESIZE)
        self.ghostOrange = Ghost(4,5,ORNG,self.disp,'Assets/orange.png',TILESIZE)

        # Update map positions
        self.maze.setTile(PACM, self.pacman.getPos()[0], self.pacman.getPos()[1])
        self.maze.setTile(RED, self.ghostRed.getPos()[0], self.ghostRed.getPos()[1])
        self.maze.setTile(BLUE, self.ghostBlue.getPos()[0], self.ghostBlue.getPos()[1])
        self.maze.setTile(PINK, self.ghostPink.getPos()[0], self.ghostPink.getPos()[1])
        self.maze.setTile(ORNG, self.ghostOrange.getPos()[0], self.ghostOrange.getPos()[1])

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
        currPos = self.pacman.getPos()
        pressed = pygame.key.get_pressed()                     
        dirX = dirY = 0    

        if pressed[pygame.K_UP]:
            dirY = -1
        elif pressed[pygame.K_DOWN]:
            dirY = 1
        elif pressed[pygame.K_LEFT]:
            dirX = -1
        elif pressed[pygame.K_RIGHT]:
            dirX = 1
                
        if ((dirX != 0 or dirY != 0) and self.maze.isEmptyTile(currPos[0] + dirX, currPos[1] + dirY)):
            self.maze.setTile(NONE, currPos[0], currPos[1])
            self.pacman.move(dirX,dirY)
            currPos = self.pacman.getPos()
            self.maze.setTile(PACM, currPos[0], currPos[1])


    # Movement logic for the orange ghost
    def moveOrange(self):
        currPos = self.ghostOrange.getPos()
        targetPos = self.pacman.getPos()
        dirX = dirY = 0

        if currPos[0] == targetPos[0]:
            if currPos[1] - targetPos[1] < -1:
                dirY += 1
            elif currPos[1] - targetPos[1] > 1:
                dirY -= 1

        elif currPos[1] == targetPos[1]:
            if currPos[0] - targetPos[0] < -1:
                dirX += 1
            elif currPos[0] - targetPos[0] > 1:
                dirX -= 1

        if self.maze.isEmptyTile(currPos[0] + dirX, currPos[1] + dirY): 
            self.maze.setTile(NONE, currPos[0], currPos[1])
            self.ghostOrange.move(dirX, dirY)
            currPos = self.ghostOrange.getPos()
            self.maze.setTile(ORNG, currPos[0], currPos[1])


    # Main game loop
    def mainLoop(self):

        while (self.quit != 1):

            self.checkEvents()        

            # Player and NPC movement
            self.movePlayer()
            self.moveOrange()
        
            # Draw the map
            self.disp.fill(COLOR_BLACK)
            for row in range(self.maze.getHeight()):
                offsetRow = row*TILESIZE 

                for column in range(self.maze.getWidth()):
                    offsetCol = column*TILESIZE

                    if self.maze.getTile(column, row) == WALL:            
                        pygame.draw.rect(self.disp, COLOR_BLUE, (offsetCol,offsetRow,TILESIZE,TILESIZE))     

            # Draw the sprites
            self.pacman.draw()
            self.ghostRed.draw()
            self.ghostBlue.draw()
            self.ghostPink.draw()
            self.ghostOrange.draw()

            pygame.display.update()

            # Cinematic 10 fps
            self.clock.tick(10)

pygame.init()
Game()
pygame.quit()
sys.exit()