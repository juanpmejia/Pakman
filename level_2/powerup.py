import pygame, random

# Some constants
DISPLAY_HEIGHT = 600
DISPLAY_WIDTH = 800

class Powerup(pygame.sprite.Sprite):

	# Initialization
	def __init__(self, image, size):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.transform.scale(pygame.image.load(image).convert_alpha(), (size,size))
		self.locations = [
			(DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2), 
			(DISPLAY_WIDTH / 3, DISPLAY_HEIGHT / 2),
			(DISPLAY_WIDTH / 3, DISPLAY_HEIGHT / 3),
			(DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 3 * 2),
			(DISPLAY_WIDTH / 3 * 2, DISPLAY_HEIGHT / 2),
			(DISPLAY_WIDTH / 3 * 2, DISPLAY_HEIGHT / 3)
		]

		self.rect = self.image.get_rect()
		self.rect.center = self.locations[0]

		self.lastPowerup = pygame.time.get_ticks()
		self.cooldown = 10000

	def setTimer(self):
		self.lastPowerup = pygame.time.get_ticks()

	def checkRespawn(self):
		if pygame.time.get_ticks() - self.lastPowerup > self.cooldown:
			return True
		else:
			return False

	def respawn(self):
		location = random.choice(self.locations)
		self.rect.center = location