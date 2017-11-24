import sys
import pygame
from pacman import *

# Some constants
DISPLAY_HEIGHT = 600
DISPLAY_WIDTH = 800
COLOR_BLACK = (0,0,0)

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

		# Initialize players
		self.pacman = Pacman('../Assets/pacman.png', (50,50))

		self.allsprites = pygame.sprite.Group()
		self.allsprites.add(self.pacman)

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
			self.allsprites.update()
			
			# Draw Everything
			self.allsprites.draw(self.screen)

			# Flip the screen and show what we've drawn
			pygame.display.flip()
			

pygame.init()
Game()
pygame.quit()
sys.exit()