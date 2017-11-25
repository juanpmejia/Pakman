import sys, pygame, random
from pacman import *
from obstacle import *
from powerup import *
from ghost import *

# Some constants
DISPLAY_HEIGHT = 600
DISPLAY_WIDTH = 800

COLOR_BLACK = (0,0,0)
COLOR_WHITE = (255,255,255)
COLOR_RED = (255,0,0)
COLOR_GREEN = (0,255,0)
COLOR_BLUE = (0,0,255)

# Main game class
class Game():

	# Initialization
	def __init__(self):
		# Set game title
		pygame.display.set_caption("Pakman")
		# Initialize game variables
		self.clock = pygame.time.Clock()
		self.quit = 0
		self.numGhosts = 5
		self.ghosts = []
		self.allsprites = pygame.sprite.Group()

		# Initialize game screen
		self.screen = pygame.display.set_mode([DISPLAY_WIDTH,DISPLAY_HEIGHT])

		# Initialize player
		self.pacman = Pacman('../Assets/pacman.png', 50)		
		self.allsprites.add(self.pacman)

		# Initialize objects
		self.obstacle1 = Obstacle(COLOR_RED, DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 3, 50)
		self.obstacle2 = Obstacle(COLOR_GREEN, DISPLAY_WIDTH / 3, DISPLAY_HEIGHT / 3 * 2, 50)
		self.obstacle3 = Obstacle(COLOR_BLUE, DISPLAY_WIDTH / 3 * 2, DISPLAY_HEIGHT / 3 * 2, 50)
		self.powerup = Powerup('../Assets/cherry.png', 50)
		self.allsprites.add(self.obstacle1)
		self.allsprites.add(self.obstacle2)
		self.allsprites.add(self.obstacle3)
		self.allsprites.add(self.powerup)

		# Initialize leader
		self.ghosts.append(Ghost('../Assets/red.png', 40, random.randint(DISPLAY_WIDTH / 3, DISPLAY_WIDTH), random.randint(DISPLAY_HEIGHT / 3, DISPLAY_HEIGHT), True))   
		self.allsprites.add(self.ghosts[0])

		# Initialize ghosts
		for i in range(self.numGhosts):
			self.ghosts.append(Ghost('../Assets/blue.png', 30, random.randint(0, DISPLAY_WIDTH), random.randint(0, DISPLAY_HEIGHT), False))   
			self.allsprites.add(self.ghosts[len(self.ghosts)-1])

		self.mainLoop()

	# Check for game events
	def checkEvents(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:  
				self.quit = 1
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					self.quit = 1

	def leaderControl(self):
		self.ghosts[0].chase(self.pacman)
		self.ghosts[0].move()

	def flockControl(self):
		for ghost in self.ghosts:
			if not(ghost.isLeader()):
				closeGhosts = []
				for otherGhost in self.ghosts:
					if otherGhost == ghost: continue

					distance = ghost.distance(otherGhost)
					if distance < 200:
						closeGhosts.append(otherGhost)
				
				ghost.chase(self.ghosts[0])
				ghost.moveWith(closeGhosts)  
				ghost.moveAway(closeGhosts, 30)  
				ghost.move()
								
	# Main game loop
	def mainLoop(self):

		while (self.quit != 1):
			# Clear the screen
			self.screen.fill(COLOR_BLACK)

			# FPS
			self.clock.tick(30)
			self.checkEvents()

			if not(self.powerup.alive()) and self.powerup.checkRespawn():
				self.powerup.respawn()
				self.allsprites.add(self.powerup)

			self.pacman.checkPowerup()
			self.pacman.movePlayer()
			self.leaderControl()
			self.flockControl()
			self.allsprites.update()

			# Check for collisions
			for ghost in self.ghosts:
				if self.pacman.checkCollision(ghost):
					text = FONT.render("GAME OVER", True, COLOR_WHITE)
					self.screen.blit(text, (DISPLAY_WIDTH / 2.5, DISPLAY_HEIGHT / 6 ))
					self.quit = 1

			self.pacman.checkCollision(self.obstacle1)
			self.pacman.checkCollision(self.obstacle2)
			self.pacman.checkCollision(self.obstacle3)

			if self.powerup.alive():
				if self.pacman.checkCollision(self.powerup):
					self.pacman.setPowerup(True)
					self.powerup.setTimer()
					self.powerup.kill()
					self.ghosts[len(self.ghosts)-1].kill()
					self.ghosts.pop()
				elif self.ghosts[0].checkCollision(self.powerup):
					self.powerup.setTimer()
					self.powerup.kill()
					self.ghosts.append(Ghost('../Assets/blue.png', 30, random.randint(0, DISPLAY_WIDTH), random.randint(0, DISPLAY_HEIGHT), False))   
					self.allsprites.add(self.ghosts[len(self.ghosts)-1])					

			# Check victory conditions
			if len(self.ghosts) == 1:
				text = FONT.render("YOU WIN", True, COLOR_WHITE)
				self.screen.blit(text, (DISPLAY_WIDTH / 2.5, DISPLAY_HEIGHT / 6 ))
				self.quit = 1

			# Draw Everything
			self.allsprites.draw(self.screen)

			# Flip the screen and show what we've drawn
			pygame.display.flip()

pygame.init()
FONT = pygame.font.SysFont("monospace", 30)
Game()
event = pygame.event.wait()
if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
	pygame.quit()
	sys.exit()