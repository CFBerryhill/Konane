# Konane
run through main in game.py

TO RUN: in main in game.py, construct a board and 2 players, 
and run game using run_game(agent1, agent2, board) which
will run the game and print statstics at the end. Submitted
version currently runs against a human player. There are also 
commented out configurations for 6 games, 3 games at depths 2,4,6 for 
the alpha/beta pruning player and no_prune player respectively 
playing against a random agent.

TO CONFIGURE:
a board is constructed simply with GameBoard()

Players are constructed with a playerID, 
which is equal to the play order. (player 1 has ID 1, player 2 has ID 2)

MiniMax agents (prune and no prune) are constructed with (PlayerID, HeuristicFunction, Depth)
which are by default (PlayerID=0, HeuristicFunction=nullHeuristic, Depth=2)

AGENT OPTIONS: 
    Human (terminal I/O)
    Random
    MiniMax_noprune
    MiniMax

Our best heuristic is moveable_tiles_diff_heuristic, this is the one we will use in the tournament

EXAMPLE: 

board = GameBoard()
agent1 = HumanAgent(1)
agent2 = MiniMax_noprune(2, move_diff_heuristic, 4)

run_game(agent1, agent2, board)