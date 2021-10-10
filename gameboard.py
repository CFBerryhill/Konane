
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
        ""

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
