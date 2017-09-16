import pygame

class Ghost:

	# Initialization
	def __init__(self, x, y, surface, sprite, size):
		self.x = x
		self.y = y
		self.surface = surface
		self.size = size
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

class GhostRed(Ghost):
	# Initialization
	def __init__(self, x, y, surface, sprite, size):
		Ghost.__init__(self, x, y, surface, sprite, size)
		self.path = []

	def setPath(self, path):
		self.path = path
		self.path.pop()

	def followPath(self):
		if len(self.path) > 1:
			curr = self.getPos()
			next = self.path.pop()
			dirX = next[0]-curr[0]
			dirY = next[1]-curr[1]
			self.move(dirX, dirY)