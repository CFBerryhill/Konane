
class Directions:
  NORTH = 'North'
  SOUTH = 'South'
  EAST = 'East'
  WEST = 'West'
  STOP = 'Stop'

class Move:

    def __init__(self, tile, dir, jumps):
        self.tile = tile
        self.dir = dir
        self.jumps = jumps

    directions = {Directions.NORTH: (0, 2),
                  Directions.SOUTH: (0, -2),
                  Directions.EAST: (2, 0),
                  Directions.WEST: (-2, 0)}

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

    def __getitem__(self, i):
        return self.board[i]

    def __setitem__(self, key, item):
        self.data[key] = item

    def fooBoard(self, board, move):

        return board

    def copyBoard(self, board):

        copy = board

        return copy

    def validMoves(self, board, Plaer):
        ""

    def toString(self, board):
        ""

    def GameOver(self, board):
        ""

    def GenerateSuccessors(self, board):
        ""
