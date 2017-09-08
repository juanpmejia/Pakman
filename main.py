import pygame
from sys import stdin
def main():
    """
    Main game function.
     in: none
     out: game display
    """

    pygame.init()
    # Display game screen
    disp = pygame.display.set_mode([800,600])
    # Set game title
    pygame.display.set_caption("Pakman")
    # Initialize game clock
    timing = pygame.time.Clock()
    #Load assets
    pacman=pygame.transform.scale(pygame.image.load('Assets/pacman.png'),(25,25))
    
    quit = 0
    while (quit != 1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    quit = 1

        disp.blit(pacman,(400,400))            
        pygame.display.flip()

main()