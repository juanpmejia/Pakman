import pygame

class Obstacle(pygame.sprite.Sprite):

	# Initialization
	def __init__(self, color, x, y, size):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.Surface((size, size))
		self.image.fill(color)
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)