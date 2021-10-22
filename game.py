from agents import *
from gameboard import *


gameItr = [0]		# list {1, 2, 3, ..., n} n = number of iterations
bfValues = [0]		# average branching factor for each iteration
cuts = [0] 		# number of cuts for each iteration
staticEvals = [0] 	# number of static evaluations for each iteration

def addBFData(gameBoard):
    global bfValues
    bfValues.append(gameBoard.branches)

def addCutsData(agent):
    global cuts
    cuts.append(agent.cuts)

def addStaticData(agent):
    global staticEvals
    staticEvals.append(agent.staticCalcs)

def addGameItr(depth):
    global gameItr
    gameItr.append(depth)

def printStats():
    global gameItr, bfValues, cuts, staticEvals

    # print all stats for bf Values
    print "Average Branching Factor"
    for x in gameItr:
        print x + " " + bfValues[gameItr.index[x]]

    print "Number of Cuts"
    for x in gameItr:
        print x + " " + cuts[gameItr.index[x]]

    print "Number of Static Evals"
    for x in gameItr:
        print x + " " + staticEvals[gameItr.index[x]]

def clearStats():
    global gameItr, bfValues, cuts, staticEvals
    gameItr = [0]
    bfValues = [0]
    cuts = [0]
    staticEvals = [0]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    board = GameBoard()
    print(board.toString())

    agent1 = MiniMaxAgent(1, moveable_tiles_diff_heuristic,4)
    agent2 = MiniMaxAgent(2, move_diff_heuristic,4)

    #remove starting tokens
    empty = (-1, -1)
    tile = agent1.getStartingRemoval(board, empty)
    board.removeTile(tile)
    tile2 = agent2.getStartingRemoval(board, tile)
    board.removeTile(tile2)

    print(board.toString())

    turncnt = 0
    while board.gameOver((turncnt % 2) + 1) == 0:
        print "player ", (turncnt % 2) + 1, "'s turn"
        print(board.toString())
        if turncnt % 2 == 0:
            move = agent2.getMove(board)
            board.fooBoard(move)
            print move.toString()
        else:
            move = agent1.getMove(board)
            board.fooBoard(move)
            print move.toString()
        turncnt += 1
        print "player ", (turncnt % 2) + 1, "'s turn"

    print board.gameOver((turncnt % 2) + 1).__str__() + " has won!"
    # Collecting Stats from this game iteration
    addBFData(board)
    addCutsData(agent1)
    addStaticData(agent1)
    addGameItr(1)   # should be changed to the depth of this iteration

    print board.gameOver().__str__() + " has won!"

    # All game iterations are complete for this test
    printStats()
    clearStats()

    # Test with next algorthim below


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
