from game import Agent
from random import randrange

class HumanAgent(Agent):
    "a human player interface"
    def getMove(self, board):
        tile = input("tile to move (x,y):")
        dir = input("direction to move (N/S/E/W):")
        jumps = input("number of jumps:")
        #check for validitiy

class RandomAgent(Agent):
    "an agent that takes random valid moves"
    def getMove(self, board):
        legalmoves = board.getValidMoves(self)
        rand = randrange(len(legalmoves))
        return legalmoves[rand]

class MiniMaxAgent(Agent):
    "an agent that searches for moves with minimax"

    def MiniMax(self, board):
        ""

    def Maximize(self, board):
        ""

    def Minimize(self, board):
        ""