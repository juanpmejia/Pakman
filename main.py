import pygame

# Map dimensions
TILESIZE  = 50
MAPWIDTH  = 5
MAPHEIGHT = 5
# Constants for map items
NONE = 0
WALL = 1
PACM = 2
RED  = 3

# Map representation
gameMap = [
    [WALL, WALL, WALL, WALL, WALL],
    [WALL, PACM, NONE, NONE, WALL],
    [WALL, NONE, WALL, NONE, WALL],
    [WALL, NONE, NONE,  RED, WALL],
    [WALL, WALL, WALL, WALL, WALL]
]

# Check for valid movement (tile must be empty)
def isValidMove(posX, posY):
    if gameMap[posY][posX] != NONE:
        return False
    else:
        return True

# Move an item on the map
def move(posX, posY, offsetX, offsetY):
    temp = gameMap[posY][posX]
    gameMap[posY][posX] = NONE
    gameMap[posY+offsetY][posX+offsetX] = PACM

# Main game logic
def main():
    pygame.init()
    # Set game title
    pygame.display.set_caption("Pakman")
    # Initialize game clock
    timing = pygame.time.Clock()

    # Load assets
    pacman = pygame.transform.scale(pygame.image.load('Assets/pacman.png'),(TILESIZE,TILESIZE))
    ghostRed = pygame.transform.scale(pygame.image.load('Assets/red.png'),(TILESIZE,TILESIZE))

    # Display game screen
    disp = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))

    # Initialize game variables
    quit = 0
    posX = 1
    posY = 1
    angle=0
    pacman2=pacman
    while (quit != 1):

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()

            # Keyboard events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    quit = 1

                # Movement logic
                if event.key == pygame.K_UP:
                    if isValidMove(posX, posY-1):
                        move(posX,posY,0,-1)
                        angle=90
                        pacman2=pygame.transform.rotate(pacman,angle)
                        posY -= 1
                if event.key == pygame.K_DOWN:
                    if isValidMove(posX, posY+1):
                        move(posX,posY,0,1)
                        angle=-90
                        pacman2=pygame.transform.rotate(pacman,angle)
                        posY += 1
                if event.key == pygame.K_LEFT:
                    if isValidMove(posX-1, posY):
                        move(posX,posY,-1,0)
                        angle=180
                        pacman2=pygame.transform.rotate(pacman,angle)
                        posX -= 1
                if event.key == pygame.K_RIGHT:
                    if isValidMove(posX+1, posY):
                        angle=0
                        pacman2=pygame.transform.rotate(pacman,angle)
                        move(posX,posY,1,0)
                        posX += 1

        # Draw the map
        for row in range(MAPHEIGHT):
            for column in range(MAPWIDTH):
                if gameMap[row][column] == NONE:
                    pygame.draw.rect(disp, (0,0,0), (column*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE))
                elif gameMap[row][column] == WALL:            
                    pygame.draw.rect(disp, (0,0,255), (column*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE))
                elif gameMap[row][column] == PACM:
                    disp.blit(pacman2,(column*TILESIZE,row*TILESIZE))      
                elif gameMap[row][column] == RED:
                    disp.blit(ghostRed,(column*TILESIZE,row*TILESIZE)) 

        pygame.display.flip()

main()