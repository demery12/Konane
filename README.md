# Konane - Winner of our class AI tournament!

By Dylan Emery and Christopher Villalta

This program is organized into two distinct pieces:

1) A Board class that handles the list of lists representation of our checkers board which includes handling piece movement and board displaying

2) A Game file which holds all the information necessary to run a game of Konane. This includes a Game class which is used as a game state node, the minimax with alpha-beta pruning algorithm for our computer player, a game playing function to initialize a game of Konane with a board setup passed in as a parameter.

===Gameplay===

Gameplay is initialized by calling the game_play() function with board size, a Board instance, and starting player number as arguments.

Once running an instance of gameplay, the initial moves are entirely handled by the human user (i.e. we make the first move for the AI and the first move for us). You can remove whatever you want to, even if it is against the original rules.

Then, depending on the start player, the computer or the player shall make a move. Player input is taken as two tuples: the first representing the piece's starting coordinates and the second the piece's final end coordinates.

===Algorithm===

Konane with board represented as a matrix (python list of lists). Comes with a fully implemented minimax (with alpha-beta pruning) capable game-playing AI. The minimax with alpha-beta pruning has no other deviations from the base algorithm.

The static evaluation function for minimax simply calculates the number of moves the AI has minus the number of moves the player at that node and returns that value unless that node is a win-state or lose-state whereby it will give it a positive infinite value or a negative infinite value respectively.

