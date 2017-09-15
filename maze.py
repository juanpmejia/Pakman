# Constants for map definition
NONE = 0
WALL = 1
PACM = 2
RED  = 3
ORNG = 4
PINK = 5
BLUE = 6

class Maze:

    # Initialization
    def __init__(self):
        self.gameMap = [
            [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL],
            [WALL, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, WALL],
            [WALL, NONE, WALL, WALL, WALL, NONE, NONE, WALL, NONE, NONE, WALL, WALL, WALL, NONE, WALL],
            [WALL, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, WALL],
            [WALL, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, WALL],
            [WALL, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, WALL],
            [WALL, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, WALL],
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
            [WALL, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, WALL],
            [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL]
        ]
        self.height = len(self.gameMap)
        self.width  = len(self.gameMap[0])

    # Get the size in the Y axis
    def getHeight(self):
        return self.height

    # Get the size in the X axis
    def getWidth(self):
        return self.width

    # Get the contents of a tile
    def getTile(self, x, y):
        return self.gameMap[y][x]

    # Assign an item to a tile
    def setTile(self, item, x, y):
        self.gameMap[y][x] = item

    # Check if a tile has nothing in it
    def isEmptyTile(self, x, y):
        if self.gameMap[y][x] != NONE:
            return False
        else:
            return True