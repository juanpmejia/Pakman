import pygame

# Some constants
DISPLAY_HEIGHT = 600
DISPLAY_WIDTH = 800

class Powerup(pygame.sprite.Sprite):

	# Initialization
	def __init__(self, image, size):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.transform.scale(pygame.image.load(image).convert_alpha(), (size,size))
		self.rect = self.image.get_rect()
		self.rect.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2)