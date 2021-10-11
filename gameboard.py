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

    directions = {Directions.NORTH: (0, -2),
                  Directions.SOUTH: (0, 2),
                  Directions.EAST: (2, 0),
                  Directions.WEST: (-2, 0)}

    def toString(self):
        return "(" + str(self.tile[0]+1) + ", " + str(self.tile[1]+1) + "), " + str(self.dir) + ", " + str(self.jumps)

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

    def __setitem__(self, key, item):
        self.data[key] = item

    def removeTile(self, tile):
        self.__setitem__(tile,0)

    def fooBoard(self, move):
        color = self.__getitem__(move.tile)
        self.removeTile(move.tile)          # sets start to 0
        for i in range(2 * move.jumps):     # remove all pieces in between start and end
            self.removeTile(move.tile + (i * move.dir))
        self.__setitem__((move.tile + (move.jumps * move.dir)), color)
        return self

    def copy(self):
        return self.copy()

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
                    while y-2 in range(0, self.height) and self.board[x][y - 2] is 0:
                        validmoves.append(Move((r, c), 'North', jump))
                        y = y - 2
                        jump += 1
                    # reset x,y , jump
                    x = r
                    y = c
                    jump = 1
                    # check E
                    while x+2 in range(0, self.width) and self.board[x + 2][y] is 0:
                        validmoves.append(Move((r, c), 'East', jump))
                        x = x + 2
                        jump += 1
                    # reset x,y ,  jump
                    x = r
                    y = c
                    jump = 1
                    # check S
                    while y+2 in range(0, self.height) and self.board[x][y + 2] is 0:
                        validmoves.append(Move((r, c), 'South', jump))
                        y = y + 2
                        jump += 1
                    # reset x, y, jump
                    x = r
                    y = c
                    jump = 1
                    # check W
                    while x-2 in range(0, self.width) and self.board[x - 2][y] is 0:
                        validmoves.append(Move((r, c), 'West', jump))
                        x = x - 2
                        jump += 1
        return validmoves

    def toString(self):
        "turns board into a string"
        str = ""
        for i in range(0, self.width):
            for j in range(0, self.height):
                if self.board[i][j] is 0:
                    str += "_  "
                elif self.board[i][j] is 1:
                    str += "w  "
                elif self.board[i][j] is 2:
                    str += "b  "
            str += "\n"

        return str

    def gameOver(self):
        "checks if game is over"
        return len(self.validMoves(1)) is 0 or len(self.validMoves(2)) is 0

    def generateSuccessors(self, player_index):
        "returns a list of possible next boards given current players index"
        successors = list()
        valid_moves = self.validMoves(player_index)
        for i in valid_moves:
            boardcopy = self.copy()
            newboard = boardcopy.fooBoard(i)
            successors.append(newboard)
        return successors
