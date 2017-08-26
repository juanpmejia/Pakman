import pygame
from sys import stdin
def main():
    """
    Funcion que retorna la visualizacion de un nivel
    Entradas: Ninguna
    Salidas: Pantalla
    """
    quit=1
    while (quit!=0):
        
        pygame.init() # inicializa todos los modulos de pygame
        disp= pygame.display.set_mode([800,600])# retorna superficie
        pygame.display.set_caption("Pakman") # titulo de la pantalla
        timing = pygame.time.Clock() # Reloj que controla el tiempo (Evita desperdiciar recursos)
        red = (255,100,100) # Variable de color  azul= 0,0,255 negro= 0,0,0 rojo=255,0,0 verde= 0, 255, 0  Blanco= 255, 255, 255
        pac=pygame.image.load('Assets/pacman.png')
        pacman=pygame.transform.scale(pac,(25,25))
        disp.blit(pacman,(400,400))
        pygame.display.update()
        if (stdin.readline().strip()=="q"):
            quit=0

    #pygame.quit()
main()