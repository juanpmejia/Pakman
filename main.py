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
    [WALL, NONE, WALL, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, WALL, NONE, WALL],
    [WALL, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, WALL],
    [WALL, NONE, WALL, WALL, WALL, NONE, NONE, WALL, NONE, NONE, WALL, WALL, WALL, NONE, WALL],
    [WALL, NONE, NONE, RED,  NONE, NONE, NONE, NONE, NONE, NONE, NONE, PINK, NONE, NONE, WALL],
    [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL]
]

# Map dimensions
TILESIZE  = 25
MAPWIDTH  = len(gameMap[0])
MAPHEIGHT = len(gameMap)

# Check for valid movement (tile must be empty)
def isValidMove(posX, posY):
    if gameMap[posY][posX] != NONE:
        return False
    else:
        return True

class Pacman:
	def __init__(self, x, y, surface, sprite):
		self.x = x
		self.y = y
		self.angle = 0
		self.surface = surface
		self.sprite = pygame.transform.scale(pygame.image.load(sprite),(TILESIZE,TILESIZE))

	def draw(self):
		self.surface.blit(self.sprite,(self.x*TILESIZE,self.y*TILESIZE))

	def move(self, offsetX, offsetY, angle):
		if isValidMove(self.x + offsetX, self.y + offsetY):
			temp = gameMap[self.y][self.x]
			gameMap[self.y][self.x] = NONE
			self.x += offsetX
			self.y += offsetY
			gameMap[self.y][self.x] = temp
			#self.sprite = pygame.transform.rotate(self.sprite,angle)

# Main game logic
def main():
    pygame.init()
    # Set game title
    pygame.display.set_caption("Pakman")
    # Initialize game clock
    timing = pygame.time.Clock()

    # Display game screen
    disp = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))

    # Load assets
    pacman = Pacman(1,1,disp,'Assets/pacman.png')
    ghostRed = pygame.transform.scale(pygame.image.load('Assets/red.png'),(TILESIZE,TILESIZE))
    ghostOrange = pygame.transform.scale(pygame.image.load('Assets/orange.png'),(TILESIZE,TILESIZE))
    ghostBlue = pygame.transform.scale(pygame.image.load('Assets/blue.png'),(TILESIZE,TILESIZE))
    ghostPink = pygame.transform.scale(pygame.image.load('Assets/pink.png'),(TILESIZE,TILESIZE))

    # Initialize game variables
    quit = 0

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
                    pacman.move(0,-1,90)
                if event.key == pygame.K_DOWN:
                    pacman.move(0,1,-90)
                if event.key == pygame.K_LEFT:
                    pacman.move(-1,0,180)
                if event.key == pygame.K_RIGHT:
                    pacman.move(1,0,0)

        # Draw the map
        disp.fill((0,0,0))

        for row in range(MAPHEIGHT):
            offsetRow = row*TILESIZE
            
            for column in range(MAPWIDTH):
                offsetCol = column*TILESIZE

                if gameMap[row][column] == WALL:            
                    pygame.draw.rect(disp, (0,0,255), (offsetCol,offsetRow,TILESIZE,TILESIZE))     
                elif gameMap[row][column] == RED:
                    disp.blit(ghostRed,(offsetCol,offsetRow))
                elif gameMap[row][column] == ORNG:
                    disp.blit(ghostOrange,(offsetCol,offsetRow))
                elif gameMap[row][column] == BLUE:
                    disp.blit(ghostBlue,(offsetCol,offsetRow))
                elif gameMap[row][column] == PINK:
                    disp.blit(ghostPink,(offsetCol,offsetRow)) 

        pacman.draw()
        pygame.display.update()

main()