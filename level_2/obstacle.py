import pygame

class Obstacle(pygame.sprite.Sprite):

	# Initialization
	def __init__(self, color, x, y):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.Surface((50, 50))
		self.image.fill(color)
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)