import sets
import math
from maze import *

def heuristic(pointA, pointB):
	return round(math.sqrt(((pointB[0]-pointA[0])**2)+((pointB[1]-pointA[1])**2)),2) 

def isNotEmptySet(a):
	#Tests if a set is empty
    c = a.intersection(a)
    return bool(c)

def reconstruct_path(cameFrom,current,start):
	#Reconstructs the best path recorded during the search
	path=[current]
	while current!=start:
		current=cameFrom[current]
		path.append(current)
	return path

def realDistance(pointA,pointB):
	return abs((pointB[0]-pointA[0])+(pointB[1]-pointA[1]))

def astar(start,goal,maze):
	height = maze.getHeight()
	width = maze.getWidth()

	#Nodes to visit
	openSet=set()
	openSet.add(start)

	#Visited nodes
	closedSet=set()

	#Predecessor
	cameFrom={}

	#Cost until any node from the start
	gscore={}
	for i in range (height):
		for j in range (width):
			gscore[(i,j)] = float('inf')

	#Initialization
	gscore[start]=0

	#For each node, the total cost of getting from the start node to the goal
    #by passing by that node. That value is partly known, partly heuristic.
	fscore={}
	for i in range (height):
		for j in range (width):
			fscore[(i,j)] = float('inf')
	#First estimate for f
	fscore[start]=heuristic(start,goal)


	while isNotEmptySet(openSet):
		#Node with the lowest fscore in openset
		minScore = float('inf')
		for n in openSet:
			if fscore[n] < minScore:
				minScore = fscore[n]
				current = n

		#Goal has been reached
		if(current==goal):
			return reconstruct_path(cameFrom,current,start)

		openSet.remove(current)
		closedSet.add(current)

		neighbors = []
		# Add neighbors
		if current[0]-1 > 0 and maze.getTile(current[0]-1, current[1]) != WALL:
			neighbors.append((current[0]-1, current[1]))
		if current[1]-1 > 0 and maze.getTile(current[0], current[1]-1) != WALL:
			neighbors.append((current[0], current[1]-1)	)
		if current[0]+1 < height and maze.getTile(current[0]+1, current[1]) != WALL:
			neighbors.append((current[0]+1, current[1]))
		if current[1]+1 < width and maze.getTile(current[0], current[1]+1) != WALL:
			neighbors.append((current[0], current[1]+1))

		for n in neighbors:
			#Ignore the neighbor which is already evaluated.
			if n in closedSet:
				continue
			#Discover a new node
			if n not in openSet:
				openSet.add(n)
	        #Gscore from start to neighbor
			t_gscore=gscore[current]+realDistance(current,n)
	        #Not the best path
			if(t_gscore > gscore[n]):
				continue        
	        #Maybe a best path! The path is recorded.
			cameFrom[n]=current
			gscore[n]=t_gscore
			fscore[n]=gscore[n]+heuristic(n,goal)

	#Best path was not found
	return [-1]






