import pygame

# Constants for map items
NONE = 0
WALL = 1
PACM = 2
RED  = 3
ORNG = 4
PINK = 5
BLUE = 6

# Map representation
gameMap = [
    [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL],
    [WALL, PACM, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, WALL],
    [WALL, NONE, WALL, WALL, WALL, NONE, NONE, WALL, NONE, NONE, WALL, WALL, WALL, NONE, WALL],
    [WALL, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, WALL],
    [WALL, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, WALL],
    [WALL, NONE, WALL, NONE, ORNG, NONE, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, WALL],
    [WALL, NONE, WALL, NONE, NONE, NONE, NONE, WALL, BLUE, NONE, NONE, NONE, WALL, NONE, WALL],
    [WALL, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, WALL],
    [WALL, NONE, WALL, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, WALL, NONE, WALL],
    [WALL, NONE, NONE, NONE, NONE, NONE, NONE, WALL, NONE, NONE, NONE, NONE, NONE, NONE, WALL],
    [WALL, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, WALL],
    [WALL, NONE, WALL, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, WALL, NONE, WALL],
    [WALL, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, WALL],
    [WALL, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, WALL],
    [WALL, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, WALL],
    [WALL, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, WALL],
    [WALL, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, WALL],
    [WALL, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, WALL],
    [WALL, NONE, WALL, WALL, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, WALL, NONE, WALL],
    [WALL, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, WALL],
    [WALL, NONE, WALL, WALL, WALL, NONE, NONE, WALL, NONE, NONE, WALL, WALL, WALL, NONE, WALL],
    [WALL, NONE, NONE, RED,  NONE, NONE, NONE, NONE, NONE, NONE, NONE, PINK, NONE, NONE, WALL],
    [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL]
]

# Map dimensions
TILESIZE  = 50
MAPWIDTH  = len(gameMap[0])
MAPHEIGHT = len(gameMap)

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
    ghostOrange = pygame.transform.scale(pygame.image.load('Assets/orange.png'),(TILESIZE,TILESIZE))
    ghostBlue = pygame.transform.scale(pygame.image.load('Assets/blue.png'),(TILESIZE,TILESIZE))
    ghostPink = pygame.transform.scale(pygame.image.load('Assets/pink.png'),(TILESIZE,TILESIZE))

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
            offsetRow = row*TILESIZE
            
            for column in range(MAPWIDTH):
                offsetCol = column*TILESIZE

                if gameMap[row][column] == NONE:
                    pygame.draw.rect(disp, (0,0,0), (offsetCol,offsetRow,TILESIZE,TILESIZE))
                elif gameMap[row][column] == WALL:            
                    pygame.draw.rect(disp, (0,0,255), (offsetCol,offsetRow,TILESIZE,TILESIZE))
                elif gameMap[row][column] == PACM:
                    disp.blit(pacman2,(offsetCol,offsetRow))      
                elif gameMap[row][column] == RED:
                    disp.blit(ghostRed,(offsetCol,offsetRow))
                elif gameMap[row][column] == ORNG:
                    disp.blit(ghostOrange,(offsetCol,offsetRow))
                elif gameMap[row][column] == BLUE:
                    disp.blit(ghostBlue,(offsetCol,offsetRow))
                elif gameMap[row][column] == PINK:
                    disp.blit(ghostPink,(offsetCol,offsetRow)) 

        pygame.display.flip()

main()