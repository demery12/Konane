from board import Board
import copy
import random

class Game:
	def __init__(self, board_size, board, player=0):
		self.board_size = board_size
		self.board = board
		self.current_player = player
		self.player_symbol = ('x','o')
	def play(self):
		pass
	# Returns a boolean of whether the game is over
	# We need the inputs because we will want it to differ from self when we are down in the minimax tree
	# We might not need self? 
	def end_state(self, board, current_player):
		if empty(self.get_legal_moves(current_player)):	# i.e. if the current_player has no more moves then either: the current_player has no pieces left or has no legal moves
			winning_player = 1 + self.current_player
			print "Player" + str(winning_player) + "wins!"
			return True
		else:
			return False

	# Returns a list of of legal moves, as pairs of pairs e.g [((8,8),(5,8)),...]
	def get_legal_moves(self, current_player):
		# Just check all the things...
		legal_moves = []
		for row in range(self.board_size):
			for col in range(self.board_size):
				if self.board.repr[row][col] == self.player_symbol[current_player]:
					position  = (row,col)
					move_fn_list = [self.north_move,
								 self.east_move,
								 self.south_move,
								 self.west_move]
					for move_fn in move_fn_list:
						move = move_fn(position)
						if self.is_legal_move(current_player,move):
					 		legal_moves.append(move)

					 		# now we are going to check for a double jump!
					 		start = move[0]
					 		cur_end   = move[1]

					 		# Make a copy of the board, and then make the move on that board
					 		new_board = copy.deepcopy(self.board)
					 		new_board.movePiece(start,cur_end)

					 		# Try to move again in the same direction
					 		continue_move = move_fn(cur_end)

					 		# make a whole new game state and check if our move is legal on that 
					 		new_game_state = Game(self.board_size,new_board,current_player)
					 		while(new_game_state.is_legal_move(current_player, continue_move)):
					 			start_cur = cur_end
					 			cur_end = continue_move[1]
					 			legal_moves.append((start,cur_end))

						 		new_board = copy.deepcopy(new_board)

					 			new_board.movePiece(start_cur,cur_end)

					 			continue_move = move_fn(cur_end)
					 			new_game_state = Game(new_game_state.board_size,new_board,current_player)



		# print legal_moves
		return legal_moves

	# Given a move e.g ((8,8),(5,8)), check if that is legal, return true if it is, false otherwise
	def is_legal_move(self, current_player, move):
		# check (again) that the starting position is the right color
		starting_pos = move[0]
		ending_pos   = move[1]
		if ending_pos[0] not in range(self.board_size) or ending_pos[1] not in range(self.board_size):		# Discard any generated moves that fall off of the board
			return False 
		if self.board.repr[starting_pos[0]][starting_pos[1]]!=self.player_symbol[current_player]:
			print "this should never trigger and is redundant"
			return False
		# Check that landing spot is empty
		if self.board.repr[ending_pos[0]][ending_pos[1]]!= '.':
			return False

		# Check the middle spot is the other piece - this should in theory not matter because the pieces alternate

		middle_pos = (starting_pos[0]-(starting_pos[0]-ending_pos[0])/2,starting_pos[1]-(starting_pos[1]-ending_pos[1])/2)
		other_player = 1 - current_player 

		if self.board.repr[middle_pos[0]][middle_pos[1]] != self.player_symbol[other_player]:
			return False 
		return True

	# seqence when it is player's turn
	def player_turn(self):
		is_valid_input = False
		while is_valid_input == False:
			move_coordinates = (input("Please enter start coordinate: "), input("Please enter end coordinate: "))	# should be two tuples entered
			actual_move_coordinates = ((move_coordinates[0][0]-1, move_coordinates[0][1]-1), (move_coordinates[1][0]-1, move_coordinates[1][1]-1))		# to convert user input (which is 1 indexed) to 0 indexed (which our board representation is in)
			is_valid_input = self.is_legal_move(self.current_player, actual_move_coordinates)
		self.board.movePiece(actual_move_coordinates[0], actual_move_coordinates[1])
		print(self.board)
		self.current_player = 1 - self.current_player		# switch player

	# sequence when it is computer's turn (v1.0: computer makes a random legal move)
	def computer_turn(self):
		random_move =  random.choice(self.get_legal_moves(self.current_player))
		self.board.movePiece(random_move[0], random_move[1])
		print(self.board)
		print "Made move: ", ((random_move[0][0]+1, random_move[0][1]+1), (random_move[1][0]+1, random_move[1][1]+1))	# to present the computer's move nicely to player
		self.current_player = 1 - self.current_player

	@staticmethod
	def north_move(pos):
		return (pos,(pos[0]-2,pos[1]))

	@staticmethod
	def east_move(pos):
		return (pos,(pos[0],pos[1]+2))

	@staticmethod
	def south_move(pos):
		return (pos,(pos[0]+2,pos[1]))

	@staticmethod
	def west_move(pos):
		return (pos,(pos[0],pos[1]-2))

def play_game(game_state):
	# Must implement some code here to make the starting move of removing a piece.
	while True: # not game_state.end_state(game_state):
		if game_state.current_player == 0:

			game_state.computer_turn()
		else:
			game_state.player_turn()

def testo():
	mygame = Game(8,Board(8))
	# mygame.board.removePiece((0,0))
	mygame.board.removePiece((3,3))
	# mygame.board.removePiece((5,5))
	# mygame.board.removePiece((7,7))
	# mygame.board.removePiece((2,4))
	play_game(mygame)

testo()

