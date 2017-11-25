import pygame

# Some constants
DISPLAY_HEIGHT = 600
DISPLAY_WIDTH = 800

class Pacman(pygame.sprite.Sprite):

	# Initialization
	def __init__(self, image, size):
		pygame.sprite.Sprite.__init__(self)

		# Speed in pixels per cycle
		self.base = 10
		self.dx = 0
		self.dy = 0

		self.image = pygame.transform.scale(pygame.image.load(image).convert_alpha(), (size,size))
		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.y = 0

		self.powerup = False
		self.duration = 5000 # 5 seconds
		self.lastPowerup = pygame.time.get_ticks()

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

	def updateSpeed(self, x, y):
		self.dx = self.base * x
		self.dy = self.base * y

	# Movement logic for the player
	def movePlayer(self):
		pressed = pygame.key.get_pressed()   

		if pressed[pygame.K_UP]:
			self.updateSpeed(0, -1)
		elif pressed[pygame.K_RIGHT]:
			self.updateSpeed(1, 0)
		elif pressed[pygame.K_DOWN]:
			self.updateSpeed(0, 1)
		elif pressed[pygame.K_LEFT]:
			self.updateSpeed(-1, 0)
	
	def checkCollision(self, spriteObject):
		if pygame.sprite.collide_rect(self, spriteObject):
			if self.dx > 0:
				self.rect.right = spriteObject.rect.left
			elif self.dx < 0:
				self.rect.left = spriteObject.rect.right
			
			elif self.dy > 0:
				self.rect.bottom = spriteObject.rect.top
			elif self.dy < 0:
				self.rect.top = spriteObject.rect.bottom

			return True

	def setPowerup(self, hasPowerup):
		if hasPowerup:
			self.powerup = True
			self.base = 15
			self.lastPowerup = pygame.time.get_ticks()
		else:
			self.powerup = False
			self.base = 10

		if self.dx > 0:
			self.updateSpeed(1, 0)
		elif self.dx < 0:
			self.updateSpeed(-1, 0)
		elif self.dy > 0:
			self.updateSpeed(0, 1)
		elif self.dy < 0:
			self.updateSpeed(0, -1)

	def checkPowerup(self):
		if self.powerup:
			if pygame.time.get_ticks() - self.lastPowerup > self.duration:
				self.setPowerup(False)