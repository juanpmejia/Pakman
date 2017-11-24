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
		self.dx = 10
		self.dy = 0

		self.image = pygame.transform.scale(pygame.image.load(image).convert_alpha(), size)
		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.y = 0

	# Update the character's position
	def update(self):
		self.rect.x += self.dx
		self.rect.y += self.dy

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
			self.dx = 0
			self.dy = -10
		elif pressed[pygame.K_RIGHT]:
			self.dx = 10
			self.dy = 0
		elif pressed[pygame.K_DOWN]:
			self.dx = 0
			self.dy = 10
		elif pressed[pygame.K_LEFT]:
			self.dx = -10
			self.dy = 0
	
	def checkCollision(self, rectObject):
		if self.rect.colliderect(rectObject.rect):
			if self.dx > 0:
				self.rect.right = rectObject.rect.left
			elif self.dx < 0:
				self.rect.left = rectObject.rect.right
			
			elif self.dy > 0:
				self.rect.bottom = rectObject.rect.top
			elif self.dy < 0:
				self.rect.top = rectObject.rect.bottom