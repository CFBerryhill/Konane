from agents import *
from gameboard import *


bfValues = -1		# average branching factor for each iteration
cuts = -1 		# number of cuts for each iteration
staticEvals = -1 	# number of static evaluations for each iteration

def addBFData():
    "Gets branching factor data from the current gameboard and gets the average"
    global bfValues
    bfValues = getAverage()

def addCutsData():
    "Gets cut count data from current agent"
    global cuts
    cuts = getCuts()

def addStaticData():
    "Gets static evaluation data from current agent"
    global staticEvals
    staticEvals = getStaticCalc()

def printStats():
    "Prints the current statistics held in game"
    global bfValues, cuts, staticEvals

    # print all stats for bf Values
    print "Average Branching Factor"
    print bfValues.__str__()

    print "Number of Cuts"
    print cuts.__str__()

    print "Number of Static Evals"
    print staticEvals.__str__()

def clearStats():
    "clears statistics in game, agents and gameboard"
    global bfValues, cuts, staticEvals
    bfValues = 0
    cuts = 0
    staticEvals = 0

    resetBF()           # Sets the statistic values in the gameboard to 0
    resetAgentStats()   # sets the statistic values in agent to 0

def run_game(agent1, agent2, board):
    """
        agent1      player 1
        agent2      player 2
        board       game board configuration
    run the game with two given agents
    """
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
    winner = board.gameOver((turncnt % 2) + 1)
    print winner.__str__() + " has won!"
    # Collecting Stats from this game iteration
    addBFData()
    addCutsData()
    addStaticData()

    # All game iterations are complete for this test
    printStats()
    clearStats()
    return winner


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #   HEURISTIC moveable_tiles_diff_heuristic

    #   MINIMAX ALPHA BETA 2
    board1 = GameBoard()
    agent1 = MiniMaxAgent(1, moveable_tiles_diff_heuristic, 2)
    randomagent = RandomAgent(2)

    print(board1.toString())

    #   MINIMAX ALPHA BETA 4
    board2 = GameBoard()
    agent2 = MiniMaxAgent(1, moveable_tiles_diff_heuristic, 4)

    print(board2.toString())

    #   MINIMAX ALPHA BETA 6
    board3 = GameBoard()
    agent3 = MiniMaxAgent(1, moveable_tiles_diff_heuristic, 6)

    print(board3.toString())

    #   MINIMAX NO PRUNE 2
    board4 = GameBoard()
    agent4 = MiniMaxAgent_noprune(1, moveable_tiles_diff_heuristic, 2)

    print(board4.toString())

    #   MINIMAX NOPRUNE 4
    board5 = GameBoard()
    agent5 = MiniMaxAgent_noprune(1, moveable_tiles_diff_heuristic, 4)

    print(board5.toString())

    #   MINIMAX ALPHA BETA 6
    board6 = GameBoard()
    agent6 = MiniMaxAgent_noprune(1, moveable_tiles_diff_heuristic, 6)

    print(board6.toString())

    # Test with next algorthim next

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
