import sys
import pygame
from maze import *
from pacman import *
from ghost import *

# Some constants
COLOR_BLACK = (0,0,0)
COLOR_BLUE = (0,0,255)

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

    # Initialize players
    pacman = Pacman(1,1,disp,'Assets/pacman.png',tileSize)
    ghostRed = Ghost(3,21,RED,disp,'Assets/red.png',tileSize)
    ghostBlue = Ghost(8,6,BLUE,disp,'Assets/blue.png',tileSize)
    ghostPink = Ghost(11,21,PINK,disp,'Assets/pink.png',tileSize)
    ghostOrange = Ghost(4,5,ORNG,disp,'Assets/orange.png',tileSize)

    # Update map positions
    maze.setTile(1,1,PACM)
    maze.setTile(3,21,RED)
    maze.setTile(8,6,BLUE)
    maze.setTile(11,21,PINK)
    maze.setTile(4,5,ORNG)

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
        disp.fill(COLOR_BLACK)

        for row in range(maze.getHeight()):
            offsetRow = row*tileSize            
            for column in range(maze.getWidth()):
                offsetCol = column*tileSize
                if maze.getTile(column, row) == WALL:            
                    pygame.draw.rect(disp, COLOR_BLUE, (offsetCol,offsetRow,tileSize,tileSize))     

        pacman.draw()
        ghostRed.draw()
        ghostBlue.draw()
        ghostPink.draw()
        ghostOrange.draw()
        pygame.display.update()

main()
pygame.quit()
sys.exit()