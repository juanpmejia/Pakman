import sys
import pygame
from maze import *
from pacman import *

# Color constants
BLACK = (0,0,0)
BLUE = (0,0,255)

# Main game logic
def main():
    pygame.init()
    # Set game title
    pygame.display.set_caption("Pakman")
    # Initialize game clock
    timing = pygame.time.Clock()

    # Display game screen
    maze = Maze(25)
    tileSize = maze.getSize()
    disp = pygame.display.set_mode((maze.getWidth()*tileSize,maze.getHeight()*tileSize))

    # Load assets
    pacman = Pacman(1,1,disp,'Assets/pacman.png',tileSize)
    ghostRed = pygame.transform.scale(pygame.image.load('Assets/red.png'),(tileSize,tileSize))
    ghostOrange = pygame.transform.scale(pygame.image.load('Assets/orange.png'),(tileSize,tileSize))
    ghostBlue = pygame.transform.scale(pygame.image.load('Assets/blue.png'),(tileSize,tileSize))
    ghostPink = pygame.transform.scale(pygame.image.load('Assets/pink.png'),(tileSize,tileSize))

    # Initialize game variables
    quit = 0

    while (quit != 1):

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  
                quit = 1

            # Keyboard events
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    quit = 1

                else:                         
                    # Movement logic
                    x = y = 0    
                    currPos = pacman.getPos()

                    if event.key == pygame.K_UP:
                        y = -1
                    elif event.key == pygame.K_DOWN:
                        y = 1
                    elif event.key == pygame.K_LEFT:
                        x = -1
                    elif event.key == pygame.K_RIGHT:
                        x = 1
                    
                    if ((x != 0 or y != 0) and maze.isEmptyTile(currPos[0] + x, currPos[1] + y)):
                        maze.setTile(currPos[0], currPos[1], NONE)
                        pacman.move(x,y)
                        currPos = pacman.getPos()
                        maze.setTile(currPos[0], currPos[1], PACM)

        # Draw the map
        disp.fill(BLACK)

        for row in range(maze.getHeight()):
            offsetRow = row*tileSize
            
            for column in range(maze.getWidth()):
                offsetCol = column*tileSize

                if maze.getTile(column, row) == WALL:            
                    pygame.draw.rect(disp, BLUE, (offsetCol,offsetRow,tileSize,tileSize))     
                
                #temporary
                elif maze.getTile(column, row) == RED:
                    disp.blit(ghostRed,(offsetCol,offsetRow))
                elif maze.getTile(column, row) == ORNG:
                    disp.blit(ghostOrange,(offsetCol,offsetRow))
                elif maze.getTile(column, row) == BLUE:
                    disp.blit(ghostBlue,(offsetCol,offsetRow))
                elif maze.getTile(column, row) == PINK:
                    disp.blit(ghostPink,(offsetCol,offsetRow)) 

        pacman.draw()
        pygame.display.update()

main()
pygame.quit()
sys.exit()