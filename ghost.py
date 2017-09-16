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
		# Remove start node
		self.path.pop()

	def followPath(self):
		if len(self.path) > 0:
			curr = self.getPos()
			next = self.path.pop()
			dirX = next[0]-curr[0]
			dirY = next[1]-curr[1]
			return (dirX, dirY)

class GhostOrange(Ghost):
	# Initialization
	def __init__(self, x, y, surface, sprite, size):
		Ghost.__init__(self, x, y, surface, sprite, size)
		self.waypoints = [(28,1), (28,21), (1,21), (1,1)]
		self.currWp = 0

	def getNextWp(self):
		return self.waypoints[self.currWp]

	def setNextWp(self):
		if self.currWp == 3:
			self.currWp = 0
		else:
			self.currWp += 1

	def setPath(self, path):
		self.path = path
		# Remove start node
		self.path.pop()

	def followPath(self):
		if len(self.path) > 0:
			curr = self.getPos()
			next = self.path.pop()
			dirX = next[0]-curr[0]
			dirY = next[1]-curr[1]
			return (dirX, dirY)