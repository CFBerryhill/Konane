import sys
import inspect
from agents import *
from gameboard import *

import heapq, random

class Agent:
  def __init__(self, index=0):
    self.index = index

  def getMove(self, board):
      raiseNotDefined()

  def getStartingRemoval(self, board, tile):
      raiseNotDefined()

def raiseNotDefined():
  print("Method not implemented: %s" % inspect.stack()[1][3])
  sys.exit(1)

#HI PAUL!!!
#Hi CASEY!!!

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    board = GameBoard()
    print(board.toString())

    agent1 = HumanAgent(1)
    agent2 = RandomAgent(2)

    #remove starting tokens
    empty = (-1,-1)
    tile = agent1.getStartingRemoval(board, empty)
    board.removeTile(tile)
    tile2 = agent2.getStartingRemoval(board, tile)
    board.removeTile(tile2)

    print(board.toString())

    turncnt = 1
    while not board.gameOver():
        print turncnt % 2 + 1, " players turn"
        if turncnt % 2 == 0:
            move = agent2.getMove(board)
            board.fooBoard(move)
            print move.toString()
        else:
            move = agent1.getMove(board)
            board.fooBoard(move)
            print move.toString()
        print(board.toString())
        turncnt += 1




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
