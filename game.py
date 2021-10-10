import sys
import inspect
from gameboard import *

import heapq, random

class Agent:
  def __init__(self, index=0):
    self.index = index

  def getMove(self, board):
      raiseNotDefined()

def raiseNotDefined():
  print("Method not implemented: %s" % inspect.stack()[1][3])
  sys.exit(1)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.

#HI PAUL!!!
#Hi CASEY!!!

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    board = GameBoard()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
