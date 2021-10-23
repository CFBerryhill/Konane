from agents import *
from gameboard import *


bfValues = -1		# average branching factor for each iteration
cuts = -1 		# number of cuts for each iteration
staticEvals = -1 	# number of static evaluations for each iteration

def addBFData():
    global bfValues
    bfValues = getAverage()

def addCutsData():
    global cuts
    cuts = getCuts()

def addStaticData():
    global staticEvals
    staticEvals = getStaticCalc()

def printStats():
    global bfValues, cuts, staticEvals

    # print all stats for bf Values
    print "Average Branching Factor"
    print bfValues.__str__()

    print "Number of Cuts"
    print cuts.__str__()

    print "Number of Static Evals"
    print staticEvals.__str__()

def clearStats():
    global bfValues, cuts, staticEvals
    bfValues = 0
    cuts = 0
    staticEvals = 0

    resetBF()
    resetAgentStats()

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

    board1 = GameBoard()
    agent1 = MiniMaxAgent(1, moveable_tiles_diff_heuristic, 2)
    randomagent = RandomAgent(2)

    print(board1.toString())

    winner = run_game(agent1, randomagent, board1)

    print winner.__str__() + " has won!"
    # Collecting Stats from this game iteration
    addBFData()
    addCutsData()
    addStaticData()

    # All game iterations are complete for this test
    printStats()
    clearStats()

    board2 = GameBoard()
    agent2 = MiniMaxAgent(1, moveable_tiles_diff_heuristic, 4)

    print(board2.toString())

    winner = run_game(agent2, randomagent, board2)

    print winner.__str__() + " has won!"
    # Collecting Stats from this game iteration
    addBFData()
    addCutsData()
    addStaticData()

    # All game iterations are complete for this test
    printStats()
    clearStats()

    board3 = GameBoard()
    agent3 = MiniMaxAgent(1, moveable_tiles_diff_heuristic, 6)

    print(board3.toString())

    winner = run_game(agent3, randomagent, board3)

    print winner.__str__() + " has won!"
    # Collecting Stats from this game iteration
    addBFData()
    addCutsData()
    addStaticData()

    # All game iterations are complete for this test
    printStats()
    clearStats()

    # Test with next algorthim next

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
