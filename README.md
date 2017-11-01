# Konane

By Dylan Emery and Christopher Villalta

Konane implementation with board represented as a matrix (python list of lists). Comes with a fully implemented minimax (with alpha-beta pruning) capable game-playing AI. The minimax with alpha-beta pruning has no other deviations from the original algorithm.

We have organized our program into two parts: 
a Board class that handles our representation and piece removal and movement
A Game class that holds game playing methods such as get_legal_moves() , player_move() and computer_move().

Our Game class node keeps track the board size, latest board configuration, current player, and the last move made.

Player input is split into two consecutive tuple inputs: from position coordinates -> to position coordinates

Static evaluation function for minimax simply calculates the number of moves the AI has minus the number of moves the player at that node and returns that value unless that node is a win-state or lose-state whereby it will give it a positive infinite value or a negative infinite value respectively.

Playing is done by calling the play_game() function with a Board as a parameter.

The initial moves are entirely handled by the human user (i.e. we make the first move for the AI and the first move for us). You can remove whatever you want to, even if it is against the original rules.
