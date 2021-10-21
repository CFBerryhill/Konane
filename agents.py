from random import randrange
from gameboard import Move
from gameboard import GameBoard

import heapq, random
import sys
import inspect


def null_heuristic(self, board):
    "returns a-non heuristic evaluation of the board"
    return board.gameOver

class Agent:
  def __init__(self, index=0, heuristic=null_heuristic):
    self.index = index
    self.heuristic = heuristic

  def getMove(self, board):
      raiseNotDefined()

  def getStartingRemoval(self, board, tile):
      raiseNotDefined()

def raiseNotDefined():
  print("Method not implemented: %s" % inspect.stack()[1][3])
  sys.exit(1)

class HumanAgent(Agent):
    "a human player interface"
    def getMove(self, board):
        tile = input("tile to move (row,col):")
        dir = raw_input("direction to move (North/South/East/West):")
        jumps = input("number of jumps:")
        #check for validitiy
        try:
            Move.directions[dir]
        except KeyError:
            print "invalid direction"
            self.getMove(board)
        move = Move((tile[0]-1, tile[1]-1), Move.directions[dir], jumps)
        validmoves = board.validMoves(self.index)
        if move in validmoves:
            return move
        else:
            print "invalid move"
            self.getMove(board)

    def getStartingRemoval(self, board, tile):
        if tile[0] is -1 and tile[1] is -1:
            tile = input("tile to remove [1,1],[4,4],[5,5],[8,8] (input format  x, y ):")
            if tile is (1, 1) or (4, 4) or (5, 5) or (8, 8):
                return tile[0] - 1, tile[1] - 1
            else:
                print("invalid option")
                return self.getStartingRemoval(board, tile)
        else:
            tile = input("N/S/E/W of " + str(tile))
            if tile is "N":
                return tile[0] - 1, tile[1]
            elif tile is "S":
                return tile[0] + 1, tile[1]
            elif tile is "E":
                return tile[0], tile[1] - 1
            elif tile is "W":
                return tile[0], tile[1] + 1
            else:
                return self.getStartingRemoval(board, tile)



class RandomAgent(Agent):
    "an agent that takes random valid moves"
    def getMove(self, board):
        legalmoves = board.validMoves(self.index)
        rand = randrange(len(legalmoves))
        return legalmoves[rand]

    def getStartingRemoval(self, board, tile):
        if tile[0] is -1 and tile[1] is -1:
            return board.initial_removable_tiles[randrange(0, len(board.initial_removable_tiles))]
        else:
            validoptions = list()
            if tile[0] - 1 >= 0:
                validoptions.append((tile[0] - 1, tile[1]))
            if tile[0] + 1 <= 7:
                validoptions.append((tile[0] + 1, tile[1]))
            if tile[1] - 1 >= 0:
                validoptions.append((tile[0], tile[1] - 1))
            if tile[1] + 1 <= 7:
                validoptions.append((tile[0], tile[1] + 1))
            return validoptions[randrange(0, len(validoptions))]



class MiniMaxAgent(Agent):
    "an agent that searches for moves with minimax"

    #maxdepth 'macro'
    init_depth = 6

    def getMove(self, board):
        ""
        return self.miniMax(board, self.init_depth, self.index, -69, 69)  #no max/min ints in python

    def getStartingRemoval(self, board, tile):
        if tile[0] is -1 and tile[1] is -1:
            boards = self.initial_boardstates()
            maxsucc = boards[0]
            currmax = -69
            for b in boards:
                v = self.maximize(b[0], self.init_depth, self.index, -69, 69) #max or minimize?
                if currmax < v:
                    currmax = v
                    maxsucc = b
            return maxsucc[1]
        else:
            boards = self.secondary_initial_boardstates(board, tile)
            maxsucc = boards[0]
            currmax = -69
            for b in boards:
                v = self.maximize(b[0], self.init_depth, self.index, -69, 69) #max or minimize?
                if currmax < v:
                    currmax = v
                    maxsucc = b
            return maxsucc[1]

    def miniMax(self, board, depth, player_index, alpha, beta):
        ""
        successors = board.generateSuccessors(player_index)
        # currmax
        currmax = -69
        maxsucc = successors[0]
        for s in successors:
            v = self.minimize(s[0], depth - 1, (player_index % 2) + 1, alpha, beta)
            if currmax < v:
                currmax = v
                maxsucc = s
        return maxsucc[1]


    def maximize(self, board, depth, player_index, alpha, beta):
        ""
        #terminal test
        if depth is 0 or board.gameOver():
            return self.heuristic(self, board)
        successors = board.generateSuccessors(player_index)
        #currmax
        currmax = -69
        for s in successors:
            currmax = max(currmax, self.minimize(s[0], depth-1, (player_index % 2)+1, alpha, beta))
        return currmax

    def minimize(self, board, depth, player_index, alpha, beta):
        ""
        # terminal test
        if depth is 0 or board.gameOver() is not 0:
            return self.heuristic(self, board)
        successors = board.generateSuccessors(player_index)
        # currmin
        currmin = 69
        for s in successors:
            currmin = min(currmin, self.maximize(s[0], depth - 1, (player_index % 2)+1, alpha, beta))
        return currmin

    def self_heuristic(self, board):
        return len(board.validMoves(self.index))

    def else_heuristic(self, board):
        return len(board.validMoves((self.index % 2) + 1))

    def move_diff_heuristic(self, board):
        return len(board.validMoves(self.index)) - len(board.validMoves((self.index % 2) + 1))

    def moveable_tiles_else_heuristic(self, board):
        validmoves = board.validMoves((self.index % 2) + 1)
        tiles = list()
        for v in validmoves:
            if v.tile not in tiles:
                tiles.append(v.tile)
        return len(tiles)

    def moveable_tiles_self_heuristic(self, board):
        validmoves = board.validMoves(self.index)
        tiles = list()
        for v in validmoves:
            if v.tile not in tiles:
                tiles.append(v.tile)
        return len(tiles)

    def moveable_tiles_diff_heuristic(self, board):
        return self.moveable_tiles_self_heuristic(board) - self.moveable_tiles_else_heuristic(board)

    def initial_boardstates(self):
        board = GameBoard()
        options = board.initial_removable_tiles
        boards = list()
        for tile in options:
            boardcopy_0 = board.copy_board()
            newboard = boardcopy_0.removeTile(tile)
            boards.__iadd__(self.secondary_initial_boardstates(newboard, tile))
        return boards

    def secondary_initial_boardstates(self, board, tile):
        boards = list()
        if tile[0] - 1 >= 0:
            newtile = (tile[0] - 1, tile[1])
            boardcopy = board.copy_board()
            boards.append((boardcopy.removeTile((tile[0] - 1, tile[1])), newtile))
        if tile[0] + 1 <= 7:
            newtile = (tile[0] + 1, tile[1])
            boardcopy = board.copy_board()
            boards.append((boardcopy.removeTile((tile[0] + 1, tile[1])), newtile))
        if tile[1] - 1 >= 0:
            newtile = (tile[0], tile[1] - 1)
            boardcopy = board.copy_board()
            boards.append((boardcopy.removeTile((tile[0], tile[1] - 1)), newtile))
        if tile[1] + 1 <= 7:
            newtile = (tile[0], tile[1] + 1)
            boardcopy = board.copy_board()
            boards.append((boardcopy.removeTile((tile[0], tile[1] + 1)), newtile))
        return boards