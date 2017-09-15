# Constants for map definition
NONE = 0
WALL = 1
PACM = 2
RED  = 3
ORNG = 4
PINK = 5
BLUE = 6

class Maze:
    def __init__(self, size):
        self.size = size
        self.gameMap = [
            [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL],
            [WALL, PACM, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, WALL],
            [WALL, NONE, WALL, WALL, WALL, NONE, NONE, WALL, NONE, NONE, WALL, WALL, WALL, NONE, WALL],
            [WALL, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, WALL],
            [WALL, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, WALL],
            [WALL, NONE, WALL, NONE, ORNG, NONE, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, WALL],
            [WALL, NONE, WALL, NONE, NONE, NONE, NONE, WALL, BLUE, NONE, NONE, NONE, WALL, NONE, WALL],
            [WALL, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, WALL],
            [WALL, NONE, WALL, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, WALL, NONE, WALL],
            [WALL, NONE, NONE, NONE, NONE, NONE, NONE, WALL, NONE, NONE, NONE, NONE, NONE, NONE, WALL],
            [WALL, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, WALL],
            [WALL, NONE, WALL, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, WALL, NONE, WALL],
            [WALL, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, WALL],
            [WALL, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, WALL],
            [WALL, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, WALL],
            [WALL, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, WALL],
            [WALL, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, WALL],
            [WALL, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, WALL],
            [WALL, NONE, WALL, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, WALL, NONE, WALL],
            [WALL, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, WALL],
            [WALL, NONE, WALL, WALL, WALL, NONE, NONE, WALL, NONE, NONE, WALL, WALL, WALL, NONE, WALL],
            [WALL, NONE, NONE, RED,  NONE, NONE, NONE, NONE, NONE, NONE, NONE, PINK, NONE, NONE, WALL],
            [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL]
        ]
        self.height = len(self.gameMap)
        self.width  = len(self.gameMap[0])

    def getHeight(self):
        return self.height
        
    def getWidth(self):
        return self.width

    def getSize(self):
        return self.size

    def getTile(self, x, y):
        return self.gameMap[y][x]

    def setTile(self, x, y, item):
        self.gameMap[y][x] = item

    # Check if a tile has nothing in it
    def isEmptyTile(self, x, y):
        if self.gameMap[y][x] != NONE:
            return False
        else:
            return True