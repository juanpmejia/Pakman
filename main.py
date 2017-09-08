import pygame

def main():
    """
    Main game function.
     in: none
     out: game display
    """
    
    pygame.init()
    # Set game title
    pygame.display.set_caption("Pakman")
    # Initialize game clock
    timing = pygame.time.Clock()

    # Constants for map items
    NONE  = 0
    WALL = 1
    PACM = 2
    # Map representation
    gameMap = [
        [WALL, WALL, WALL, WALL, WALL],
        [WALL, NONE, NONE, NONE, WALL],
        [WALL, NONE, PACM, NONE, WALL],
        [WALL, NONE, NONE, NONE, WALL],
        [WALL, WALL, WALL, WALL, WALL]
    ]
    # Map dimensions
    TILESIZE  = 50
    MAPWIDTH  = 5
    MAPHEIGHT = 5
    # Load assets
    pacman=pygame.transform.scale(pygame.image.load('Assets/pacman.png'),(TILESIZE,TILESIZE))

    # Display game screen
    disp = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))
    
    quit = 0
    while (quit != 1):

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    quit = 1

        # Draw map
        for row in range(MAPHEIGHT):
            for column in range(MAPWIDTH):
                if gameMap[row][column] == WALL:            
                    pygame.draw.rect(disp, (0,0,255), (column*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE))
                elif gameMap[row][column] == PACM:
                    disp.blit(pacman,(column*TILESIZE,row*TILESIZE))           

        pygame.display.flip()

main()