from agents import *
from gameboard import *


gameItr = [0]		# list {1, 2, 3, ..., n} n = number of iterations
bfValues = [0]		# average branching factor for each iteration
cuts = [0] 		# number of cuts for each iteration
staticEvals = [0] 	# number of static evaluations for each iteration

def addBFData():
    global bfValues
    bfValues.append(getAverage())

def addCutsData():
    global cuts
    cuts.append(getCuts())

def addStaticData():
    global staticEvals
    staticEvals.append(getStaticCalc())

def addGameItr(depth):
    global gameItr
    gameItr.append(depth)

def printStats():
    global gameItr, bfValues, cuts, staticEvals

    # print all stats for bf Values
    print "Average Branching Factor"
    print bfValues[0].__str__()

    print "Number of Cuts/n"
    print cuts[0].__str__()

    print "Number of Static Evals"
    print staticEvals[0].__str__()

def clearStats():
    global gameItr, bfValues, cuts, staticEvals
    gameItr = [0]
    bfValues = [0]
    cuts = [0]
    staticEvals = [0]

def run_game(agent1, agent2, board):
    # remove starting tokens
    empty = (-1, -1)
    tile = agent1.getStartingRemoval(board, empty)
    board.removeTile(tile)
    tile2 = agent2.getStartingRemoval(board, tile)
    board.removeTile(tile2)

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
    return board.gameOver((turncnt % 2) + 1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #   HEURISTIC moveable_tiles_diff_heuristic

    board = GameBoard()
    print(board.toString())

    agent1 = MiniMaxAgent(1, moveable_tiles_diff_heuristic, 2)
    agent2 = RandomAgent(2)

    print(board.toString())

    winner = run_game(agent1,agent2, board)

    print winner.__str__() + " has won!"
    # Collecting Stats from this game iteration
    addBFData()
    addCutsData()
    addStaticData()
    addGameItr(1)   # should be changed to the depth of this iteration

    # All game iterations are complete for this test
    printStats()
    clearStats()

    # Test with next algorthim next

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
