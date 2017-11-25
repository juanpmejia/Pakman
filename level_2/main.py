import sys
import pygame
from pacman import *
from obstacle import *
from powerup import *

# Some constants
DISPLAY_HEIGHT = 600
DISPLAY_WIDTH = 800

COLOR_BLACK = (0,0,0)
COLOR_RED = (255,0,0)
COLOR_GREEN = (0,255,0)
COLOR_BLUE = (0,0,255)

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
		self.screen = pygame.display.set_mode([DISPLAY_WIDTH,DISPLAY_HEIGHT])

		# Initialize player
		self.pacman = Pacman('../Assets/pacman.png', 50)

		# Initialize objects
		self.obstacle1 = Obstacle(COLOR_RED, DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 3, 50)
		self.obstacle2 = Obstacle(COLOR_GREEN, DISPLAY_WIDTH / 3, DISPLAY_HEIGHT / 3 * 2, 50)
		self.obstacle3 = Obstacle(COLOR_BLUE, DISPLAY_WIDTH / 3 * 2, DISPLAY_HEIGHT / 3 * 2, 50)
		self.powerup = Powerup('../Assets/cherry.png', 50)

		self.allsprites = pygame.sprite.Group()
		self.allsprites.add(self.pacman)
		self.allsprites.add(self.obstacle1)
		self.allsprites.add(self.obstacle2)
		self.allsprites.add(self.obstacle3)
		self.allsprites.add(self.powerup)

		self.mainLoop()

	# Check for game events
	def checkEvents(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:  
				self.quit = 1
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					self.quit = 1
								
	# Main game loop
	def mainLoop(self):

		while (self.quit != 1):
			# Clear the screen
			self.screen.fill(COLOR_BLACK)

			# Cinematic 10 fps
			self.clock.tick(30)

			self.checkEvents()
			self.pacman.movePlayer()
			self.pacman.checkPowerup()
			self.allsprites.update()

			# Check for collisions
			self.pacman.checkCollision(self.obstacle1)
			self.pacman.checkCollision(self.obstacle2)
			self.pacman.checkCollision(self.obstacle3)
			if self.powerup.alive() and self.pacman.checkCollision(self.powerup):
				self.pacman.setPowerup(True)
				self.powerup.kill()

			# Draw Everything
			self.allsprites.draw(self.screen)

			# Flip the screen and show what we've drawn
			pygame.display.flip()


pygame.init()
Game()
pygame.quit()
sys.exit()