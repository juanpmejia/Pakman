# Constants for map definition
NONE = 0
WALL = 1
PACM = 2
RED  = 3
ORNG = 4
PINK = 5
BLUE = 6
DOTS = 7

class Maze:

    # Initialization
    def __init__(self):
        self.gameMap = self.gameMap = [
            [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL],
            [WALL, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, WALL],
            [WALL, NONE, WALL, WALL, WALL, NONE, NONE, WALL, NONE, NONE, WALL, WALL, WALL, NONE, WALL, WALL, WALL, NONE, WALL, WALL, NONE, WALL, NONE, WALL, WALL, NONE, WALL, WALL, NONE, WALL],
            [WALL, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, WALL, WALL, WALL, NONE, WALL, WALL, NONE, WALL, NONE, WALL, WALL, NONE, WALL, WALL, NONE, WALL],
            [WALL, NONE, WALL, NONE, WALL, WALL, NONE, NONE, NONE, WALL, WALL, NONE, WALL, NONE, WALL, WALL, WALL, NONE, WALL, WALL, NONE, WALL, NONE, WALL, WALL, NONE, WALL, WALL, NONE, WALL],
            [WALL, NONE, WALL, NONE, WALL, WALL, NONE, WALL, NONE, WALL, WALL, NONE, WALL, NONE, NONE, NONE, NONE, NONE, WALL, WALL, NONE, WALL, NONE, WALL, WALL, NONE, WALL, WALL, NONE, WALL],
            [WALL, NONE, WALL, NONE, WALL, WALL, NONE, WALL, NONE, WALL, WALL, NONE, WALL, NONE, WALL, WALL, WALL, NONE, WALL, WALL, NONE, WALL, NONE, WALL, WALL, NONE, WALL, WALL, NONE, WALL],
            [WALL, NONE, WALL, NONE, WALL, WALL, NONE, WALL, NONE, WALL, WALL, NONE, WALL, NONE, WALL, WALL, WALL, NONE, NONE, NONE, NONE, WALL, NONE, NONE, NONE, NONE, WALL, WALL, NONE, WALL],
            [WALL, NONE, WALL, NONE, WALL, WALL, NONE, NONE, NONE, WALL, WALL, NONE, WALL, NONE, WALL, WALL, WALL, NONE, WALL, WALL, WALL, WALL, WALL, WALL, NONE, WALL, WALL, WALL, NONE, WALL],
            [WALL, NONE, NONE, NONE, NONE, NONE, NONE, WALL, NONE, NONE, NONE, NONE, NONE, NONE, WALL, WALL, WALL, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, WALL],
            [WALL, NONE, WALL, NONE, WALL, WALL, NONE, WALL, NONE, WALL, WALL, NONE, WALL, NONE, WALL, WALL, WALL, NONE, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, NONE, WALL],
            [WALL, NONE, WALL, NONE, WALL, WALL, NONE, NONE, NONE, WALL, WALL, NONE, WALL, NONE, WALL, WALL, WALL, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, WALL, WALL, WALL, NONE, WALL],
            [WALL, NONE, WALL, NONE, WALL, WALL, NONE, WALL, NONE, WALL, WALL, NONE, WALL, NONE, WALL, WALL, WALL, NONE, WALL, WALL, WALL, WALL, NONE, WALL, NONE, NONE, NONE, NONE, NONE, WALL],
            [WALL, NONE, WALL, NONE, WALL, WALL, NONE, WALL, NONE, WALL, WALL, NONE, WALL, NONE, WALL, WALL, WALL, NONE, WALL, WALL, WALL, WALL, NONE, WALL, NONE, WALL, WALL, WALL, NONE, WALL],
            [WALL, NONE, WALL, NONE, WALL, WALL, NONE, WALL, NONE, WALL, WALL, NONE, WALL, NONE, WALL, WALL, WALL, NONE, NONE, NONE, NONE, WALL, NONE, WALL, NONE, WALL, WALL, WALL, NONE, WALL],
            [WALL, NONE, WALL, NONE, WALL, WALL, NONE, WALL, NONE, WALL, WALL, NONE, WALL, NONE, WALL, WALL, WALL, NONE, WALL, WALL, DOTS, DOTS, DOTS, DOTS, DOTS, DOTS, NONE, NONE, NONE, WALL],
            [WALL, NONE, WALL, NONE, WALL, WALL, NONE, WALL, NONE, WALL, WALL, NONE, WALL, NONE, WALL, WALL, WALL, NONE, WALL, WALL, DOTS, WALL, WALL, WALL, WALL, DOTS, WALL, WALL, NONE, WALL],
            [WALL, NONE, WALL, NONE, WALL, WALL, NONE, WALL, NONE, WALL, WALL, NONE, WALL, NONE, NONE, NONE, NONE, NONE, WALL, WALL, DOTS, WALL, WALL, WALL, WALL, DOTS, WALL, WALL, NONE, WALL],
            [WALL, NONE, WALL, NONE, WALL, WALL, NONE, NONE, NONE, WALL, WALL, NONE, WALL, NONE, WALL, WALL, WALL, NONE, WALL, WALL, DOTS, DOTS, DOTS, DOTS, DOTS, DOTS, WALL, WALL, NONE, WALL],
            [WALL, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, NONE, NONE, NONE, WALL, NONE, WALL, WALL, WALL, NONE, WALL, WALL, DOTS, WALL, WALL, WALL, WALL, DOTS, WALL, WALL, NONE, WALL],
            [WALL, NONE, WALL, WALL, WALL, NONE, NONE, WALL, NONE, WALL, WALL, WALL, WALL, NONE, WALL, WALL, WALL, NONE, WALL, WALL, DOTS, WALL, WALL, WALL, WALL, DOTS, WALL, WALL, NONE, WALL],
            [WALL, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, NONE, DOTS, DOTS, DOTS, DOTS, DOTS, DOTS, NONE, NONE, NONE, WALL],
            [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL],
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
        if self.gameMap[y][x] == NONE or self.gameMap[y][x] == DOTS:
            return True
        else:
            return False

    def hasDot(self, x, y):
        if self.gameMap[y][x] == DOTS:
            return True
        else:
            return False

    def countDots(self):
        x = y = maxDots = temp = 0
        for i in range (2, self.width):
            for j in range (2, self.height):
                if self.hasDot(i  ,j  ): temp+=1
                if self.hasDot(i-1,j  ): temp+=1
                if self.hasDot(i-2,j  ): temp+=1
                if self.hasDot(i  ,j-1): temp+=1
                if self.hasDot(i-1,j-1): temp+=1
                if self.hasDot(i-2,j-1): temp+=1
                if self.hasDot(i  ,j-2): temp+=1
                if self.hasDot(i-1,j-2): temp+=1
                if self.hasDot(i-2,j-2): temp+=1

                if temp > maxDots:
                    maxDots = temp
                    x = i-1
                    y = j-1

        return (x,y)