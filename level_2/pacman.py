import pygame
import math

class Pacman(pygame.sprite.Sprite):

	# Initialization
	def __init__(self, image, x, y):
		super().__init__

		# Speed in pixels per cycle
		self.speed = 10.0

		# Direction (in degrees)
    	direction = 0

		self.image = pygame.image.load(image).convert()
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	# Get the character's position
	def getPos(self)
		return (self.rect.x, self.rect.y)

	# Update the character's position
	def update(self):
		radians = math.radians(self.direction)
		self.rect.x += self.speed * math.sin(radians)
		self.rect.y -= self.speed * math.cos(radians)