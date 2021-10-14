from game import Agent
from random import randrange
from gameboard import Move


class HumanAgent(Agent):
    "a human player interface"
    def getMove(self, board):
        tile = input("tile to move (x,y):")
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
            validoptions = [(0, 0), (3, 3), (4, 4), (7, 7)]
            return validoptions[randrange(0, len(validoptions))]
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

    def MiniMax(self, board):
        ""

    def Maximize(self, board):
        ""

    def Minimize(self, board):
        ""