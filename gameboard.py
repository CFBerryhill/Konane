from copy import copy


class Directions:
    NORTH = 'North'
    SOUTH = 'South'
    EAST = 'East'
    WEST = 'West'


class Move:

    def __init__(self, tile, dir, jumps):
        self.tile = tile
        self.dir = dir
        self.jumps = jumps

    directions = {Directions.NORTH: (-2, 0),
                  Directions.SOUTH: (2, 0),
                  Directions.EAST: (0, 2),
                  Directions.WEST: (0, -2)}

    def __eq__(self, other):
        return other.tile[0] == self.tile[0] and \
               other.tile[1] == self.tile[1] and \
               other.dir[0] == self.dir[0] and \
               other.dir[1] == self.dir[1] and \
               other.jumps == self.jumps

    def move(self):
        ""

    def toString(self):
        return "(" + str(self.tile[0]+1) + ", " + str(self.tile[1]+1) + "), " + str(self.dir) + ", " + str(self.jumps)



branches = 0        # sum of all branches
branchCount = 0     # number times a node branched

def addBranchFactor(successors):
    "Accumulates total number of branches and the number of nodes that branched"
    global branches
    branches = branches + len(successors)
    global branchCount
    branchCount += 1

def getAverage():
    global branches, branchCount
    return branches / branchCount
    # reset global varibales for next test
    branches = 0
    branchCount = 0

def resetBF():
    global branches, branchCount
    # reset global varibales for next test
    branches = 0
    branchCount = 0

class GameBoard:

    def __init__(self):
        # w = 1, b = 2, empty = 0
        self.height = 8
        self.width = 8
        self.board = [[0 for y in range(self.height)] for x in range(self.width)]
        count = 2
        for x in range(self.width):
            for y in range(self.height):
                self.board[x][y] = count % 2 + 1
                count = count + 1
            count = count + 1

    def __getitem__(self, tile):
        return self.board[tile[0]][tile[1]]

    def __setitem__(self, tile, item):
        self.board[tile[0]][tile[1]] = item

    initial_removable_tiles = [(0, 0), (3, 3), (4, 4), (7, 7)]

    def removeTile(self, tile):
        self.__setitem__(tile, 0)
        return self

    def fooBoard(self, move):
        color = self.__getitem__(move.tile)
        self.removeTile(move.tile)          # sets start to 0
        for i in range(0, move.jumps):     # remove all pieces in between start and end #DOESNT WORK
            removetile = (move.tile[0] + (((move.dir[0])/2) + (i*move.dir[0])),
                       move.tile[1] + ((move.dir[1])/2) + (i*move.dir[1]))
            self.removeTile(removetile)
        newtile = (move.tile[0] + (move.jumps * move.dir[0]), move.tile[1] + (move.jumps * move.dir[1]))
        self.__setitem__(newtile, color)
        return self

    def copy_board(self):
        newboard = GameBoard()
        for r in range(0, self.height):
            for c in range(0, self.width):
                newboard.__setitem__((r, c), self.board[r][c])
        return newboard

    def validMoves(self, player_index):
        "creates a list of valid moves"

        validmoves = list()

        for r in range(0, self.width):
            for c in range(0, self.height):
                if player_index is self.board[r][c]:
                    # copy coords
                    x = r
                    y = c
                    # jump counter
                    jump = 1
                    # check N
                    while y-2 in range(0, self.height) and \
                            self.board[x][y - 2] is 0 and \
                            (self.board[x][y - 1] is not player_index and self.board[x][y - 1] is not 0):
                        validmoves.append(Move((r, c), Move.directions['West'], jump))
                        y = y - 2
                        jump += 1
                    # reset x,y , jump
                    x = r
                    y = c
                    jump = 1
                    # check E
                    while x+2 in range(0, self.width) and \
                            self.board[x + 2][y] is 0 and \
                            (self.board[x + 1][y] is not player_index and self.board[x + 1][y] is not 0):
                        validmoves.append(Move((r, c), Move.directions['South'], jump))
                        x = x + 2
                        jump += 1
                    # reset x,y ,  jump
                    x = r
                    y = c
                    jump = 1
                    # check S
                    while y+2 in range(0, self.height) and \
                            self.board[x][y + 2] is 0 and \
                            (self.board[x][y + 1] is not player_index and self.board[x][y + 1] is not 0):
                        validmoves.append(Move((r, c), Move.directions['East'], jump))
                        y = y + 2
                        jump += 1
                    # reset x, y, jump
                    x = r
                    y = c
                    jump = 1
                    # check W
                    while x-2 in range(0, self.width) and \
                            self.board[x - 2][y] is 0 and \
                            (self.board[x - 1][y] is not player_index and self.board[x - 1][y] is not 0):
                        validmoves.append(Move((r, c), Move.directions['North'], jump))
                        x = x - 2
                        jump += 1
        return validmoves

    def toString(self):
        "turns board into a string"
        str = ""
        for i in range(-1, self.width): #r
            for j in range(-1, self.height): #c
                if i is -1 and j is -1:
                    str += "0  "
                elif i is -1:
                    str += (j+1).__str__() + "  "
                elif j is -1:
                    str += (i+1).__str__() + "  "
                elif self.board[i][j] is 0:
                    str += "_  "
                elif self.board[i][j] is 1:
                    str += "w  "
                elif self.board[i][j] is 2:
                    str += "b  "
            str += "\n"

        return str

    def gameOver(self, playerindex):
        "checks if game is over, returns 0 if game not over, or player index of winner"
        if len(self.validMoves(playerindex)) is 0:
            return (playerindex % 2) + 1
        else:
            return 0

    def generateSuccessors(self, player_index):
        "returns a list of successor boards  & the actions taken for those boards given current players index"
        successors = list()
        valid_moves = self.validMoves(player_index)
        for i in valid_moves:
            boardcopy = self.copy_board()
            newboard = boardcopy.fooBoard(i)
            successors.append((newboard, i))

        addBranchFactor(successors)

        return successors
