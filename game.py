from agents import *
from gameboard import *

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

    print board.gameOver((turncnt % 2) + 1).__str__() + " has won!"



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
