import pygame
import math

# Some constants
DISPLAY_HEIGHT = 600
DISPLAY_WIDTH = 800

class Pacman(pygame.sprite.Sprite):

	# Initialization
	def __init__(self, image, size):
		pygame.sprite.Sprite.__init__(self)

		# Speed in pixels per cycle
		self.speed = 10.0

		# Direction (in degrees)
		self.direction = 90

		self.image = pygame.transform.scale(pygame.image.load(image).convert_alpha(), size)
		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.y = 0

	# Get the character's position
	def getPos(self):
		return (self.rect.x, self.rect.y)

	# Update the character's position
	def update(self):
		radians = math.radians(self.direction)
		self.rect.x += self.speed * math.sin(radians)
		self.rect.y -=	  self.speed * math.cos(radians)

		if self.rect.left < 0:
			self.rect.left = 0
		elif self.rect.right > DISPLAY_WIDTH:
			self.rect.right = DISPLAY_WIDTH

		if self.rect.top < 0:
			self.rect.top = 0
		elif self.rect.bottom > DISPLAY_HEIGHT:
			self.rect.bottom = DISPLAY_HEIGHT

	# Movement logic for the player
	def movePlayer(self):
		pressed = pygame.key.get_pressed()   

		if pressed[pygame.K_UP]:
			self.direction = 0   
		elif pressed[pygame.K_RIGHT]:
			self.direction = 90
		elif pressed[pygame.K_DOWN]:
			self.direction = 180
		elif pressed[pygame.K_LEFT]:
			self.direction = 270
		