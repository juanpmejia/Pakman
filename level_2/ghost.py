import sys, pygame, random, math

# Some constants
DISPLAY_HEIGHT = 600
DISPLAY_WIDTH = 800

class Ghost(pygame.sprite.Sprite):
	def __init__(self, image, size, x, y, leadership):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.transform.scale(pygame.image.load(image).convert_alpha(), (size,size))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		self.velocityX = random.randint(1, 10) / 10.0
		self.velocityY = random.randint(1, 10) / 10.0
		self.maxVelocity = 5

		self.leadership = leadership

	def isLeader(self):
		return self.leadership

	# Return the distance from another ghost
	def distance(self, ghost):
		distX = self.rect.x - ghost.rect.x
		distY = self.rect.y - ghost.rect.y        
		return math.sqrt(distX * distX + distY * distY)

	# Move closer to a target
	def chase(self, target):
		# calculate the average distances from the other ghosts
		avgX = 0
		avgY = 0

		avgX += (self.rect.x - target.rect.x)
		avgY += (self.rect.y - target.rect.y)

		# set our velocity towards the others
		distance = math.sqrt((avgX * avgX) + (avgY * avgY)) * -1.0
	   
		self.velocityX -= (avgX / 100) 
		self.velocityY -= (avgY / 100) 

	# Move closer to a set of ghosts
	def moveCloser(self, ghosts):
		if len(ghosts) < 1: return
			
		# calculate the average distances from the other ghosts
		avgX = 0
		avgY = 0
		for ghost in ghosts:
			if ghost.rect.x == self.rect.x and ghost.rect.y == self.rect.y:
				continue
				
			avgX += (self.rect.x - ghost.rect.x)
			avgY += (self.rect.y - ghost.rect.y)

		avgX /= len(ghosts)
		avgY /= len(ghosts)

		# set our velocity towards the others
		distance = math.sqrt((avgX * avgX) + (avgY * avgY)) * -1.0
	   
		self.velocityX -= (avgX / 100) 
		self.velocityY -= (avgY / 100) 
		
	# Move with a set of ghosts
	def moveWith(self, ghosts):
		if len(ghosts) < 1: return
		# calculate the average velocities of the other ghosts
		avgX = 0
		avgY = 0
				
		for ghost in ghosts:
			avgX += ghost.velocityX
			avgY += ghost.velocityY

		avgX /= len(ghosts)
		avgY /= len(ghosts)

		# set our velocity towards the others
		self.velocityX += (avgX / 40)
		self.velocityY += (avgY / 40)
	
	# Move away from a set of ghosts. This avoids crowding
	def moveAway(self, ghosts, minDistance):
		if len(ghosts) < 1: return
		
		distanceX = 0
		distanceY = 0
		numClose = 0

		for ghost in ghosts:
			distance = self.distance(ghost)
			if  distance < minDistance:
				numClose += 1
				xdiff = (self.rect.x - ghost.rect.x) 
				ydiff = (self.rect.y - ghost.rect.y) 
				
				if xdiff >= 0: xdiff = math.sqrt(minDistance) - xdiff
				elif xdiff < 0: xdiff = -math.sqrt(minDistance) - xdiff
				
				if ydiff >= 0: ydiff = math.sqrt(minDistance) - ydiff
				elif ydiff < 0: ydiff = -math.sqrt(minDistance) - ydiff

				distanceX += xdiff 
				distanceY += ydiff 
		
		if numClose == 0:
			return
			
		self.velocityX -= distanceX / 5
		self.velocityY -= distanceY / 5
		
	# Perform actual movement based on our velocity
	def move(self):
		border = 25

		if self.rect.left < border and self.velocityX < 0:
			self.velocityX = -self.velocityX * random.random()
		if self.rect.right > DISPLAY_WIDTH - border and self.velocityX > 0:
			self.velocityX = -self.velocityX * random.random()

		if self.rect.top < border and self.velocityY < 0:
			self.velocityY = -self.velocityY * random.random()
		elif self.rect.bottom > DISPLAY_HEIGHT - border and self.velocityY > 0:
			self.velocityY = -self.velocityY * random.random()
		
		if abs(self.velocityX) > self.maxVelocity or abs(self.velocityY) > self.maxVelocity:
			scaleFactor = self.maxVelocity / max(abs(self.velocityX), abs(self.velocityY))
			self.velocityX *= scaleFactor
			self.velocityY *= scaleFactor
		
		self.rect.x += self.velocityX
		self.rect.y += self.velocityY

	def checkCollision(self, spriteObject):
		if pygame.sprite.collide_rect(self, spriteObject):
			return True