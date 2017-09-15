import pygame

class Pacman:
	def __init__(self, x, y, surface, sprite, size):
		self.x = x
		self.y = y
		self.surface = surface
		self.size = size
		self.sprite = pygame.transform.scale(pygame.image.load(sprite),(size,size))

	def draw(self):
		self.surface.blit(self.sprite,(self.x*self.size,self.y*self.size))

	def move(self, x, y):
		self.x += x
		self.y += y

	def getPos(self):
		return (self.x, self.y)