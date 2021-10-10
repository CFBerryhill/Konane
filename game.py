import sys
import inspect
import heapq, random

class Agent:
  def __init__(self, index=0):
    self.index = index

  def getMove(self, board):
      raiseNotDefined()

def raiseNotDefined():
  print "Method not implemented: %s" % inspect.stack()[1][3]
  sys.exit(1)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.

#HI PAUL!!!

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
