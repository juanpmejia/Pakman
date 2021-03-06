import pygame

class Pacman:

	# Initialization
	def __init__(self, x, y, surface, sprite, size):
		self.x = x
		self.y = y
		self.surface = surface
		self.size = size
		self.dir = 0
		self.sprite = pygame.transform.scale(pygame.image.load(sprite),(size,size))

	# Draw the sprite
	def draw(self):
		self.surface.blit(self.sprite,(self.x*self.size,self.y*self.size))

	# Get the character's position
	def getPos(self):
		return (self.x, self.y)

	# Update the character's position
	def move(self, x, y):
		self.x += x
		self.y += y