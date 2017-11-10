from board import Board
import copy
import random
import time

static_eval_count = 0
minimax_calls     = 0
total_branches    = 0
cutoffs           = 0

def minimax(game_state, depth_bound):
	global static_eval_count
	global minimax_calls     
	global total_branches    
	global cutoffs 
	if depth_bound == 1:
		static_eval_count += 1
		return (game_state.static_evaluation(), None) 	# It is irrelevant what we return int second slot
	elif game_state.current_player == 0:	# i.e is AI turn (max node)
		bestmove = None
		minimax_calls += 1
		cbv = float("-inf")
		for successor_game_state in game_state.generate_successors():
			total_branches += 1
			# player_move just gets discarded
			bv, player_move = minimax(successor_game_state, depth_bound+1)
			if bv > cbv:
				cbv = bv
				bestmove = successor_game_state.last_move_made
		return (cbv, bestmove)
	else: 	# i.e looking at player turn (min node)
		bestmove = None
		minimax_calls += 1
		cbv = float("inf")
		for successor_game_state in game_state.generate_successors():
			total_branches += 1
			# computer_move is not relevant, we just need to return both for later
			bv, computer_move = minimax(successor_game_state, depth_bound+1)
			if bv < cbv:
				cbv = bv
				bestmove = successor_game_state.last_move_made
		return (cbv, bestmove)

class Game:
	def __init__(self, board_size, board, player=0, last_move_made = ((),())):
		self.board_size = board_size
		self.board = board
		self.last_move_made = last_move_made
		self.current_player = player
		self.player_symbol = ('x','o')
		self.endgame = 0

	def get_legal_moves(self, current_player):
		""" Returns a list of of legal moves, as pairs of pairs e.g [((8,8),(5,8)),...] """
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
					 		new_board = copy.deepcopy(self.board)	# Make a copy of the board, and then make the move on that board
					 		new_board.movePiece(start,cur_end)
					 		continue_move = move_fn(cur_end)		# Try to move again in the same direction
					 		new_game_state = Game(self.board_size,new_board,current_player)			# make a whole new game state and check if our move is legal on that 
					 		while(new_game_state.is_legal_move(current_player, continue_move)):
					 			start_cur = cur_end
					 			cur_end = continue_move[1]
					 			legal_moves.append((start,cur_end))
						 		new_board = copy.deepcopy(new_board)
					 			new_board.movePiece(start_cur,cur_end)
					 			continue_move = move_fn(cur_end)
					 			new_game_state = Game(new_game_state.board_size,new_board,current_player)
		return legal_moves

	def is_legal_move(self, current_player, move):
		""" Given a move e.g ((8,8),(5,8)), check if that is legal, return true if it is, false otherwise """
		starting_pos = move[0]
		ending_pos   = move[1]
		if ending_pos[0] not in range(self.board_size) or ending_pos[1] not in range(self.board_size):	# Discard any generated moves that fall off of the board
			return False 
		if self.board.repr[starting_pos[0]][starting_pos[1]]!=self.player_symbol[current_player]:
			print "this should never trigger and is redundant"
			return False
		if self.board.repr[ending_pos[0]][ending_pos[1]]!= '.':	# Check that landing spot is empty
			return False
		middle_pos = (starting_pos[0]-(starting_pos[0]-ending_pos[0])/2,starting_pos[1]-(starting_pos[1]-ending_pos[1])/2)	# Check the middle spot is the other piece - this should in theory not matter because the pieces alternate
		other_player = 1 - current_player 
		if self.board.repr[middle_pos[0]][middle_pos[1]] != self.player_symbol[other_player]:
			return False 
		return True

	def generate_successors(self):
		successors = []
		for move in self.get_legal_moves(self.current_player):
			boardCopy = copy.deepcopy(self.board)
			boardCopy.movePiece(move[0], move[1])
			successors.append(Game(self.board_size, boardCopy, 1-self.current_player, move))
		for s in successors:
			if False:
				print s.board
		return successors

	def player_turn(self):
		try:
			legal_moves = self.get_legal_moves(self.current_player)
			print legal_moves
			if len(legal_moves) != 0:
				is_valid_input = False
				while is_valid_input == False:
					move_coordinates = (input("Please enter start coordinate: "), input("Please enter end coordinate: "))	# should be two tuples entered
					actual_move_coordinates = ((move_coordinates[0][0]-1, move_coordinates[0][1]-1), (move_coordinates[1][0]-1, move_coordinates[1][1]-1))	# to convert user input (which is 1 indexed) to 0 indexed (which our board representation is in)
					is_valid_input =  actual_move_coordinates in legal_moves
				self.board.movePiece(actual_move_coordinates[0], actual_move_coordinates[1])
				print(self.board)
				self.last_move_made = move_coordinates
				self.current_player = 1 - self.current_player
			else:
				self.endgame = 1
				print "Player", self.player_symbol[self.current_player], "loses!"
		except KeyboardInterrupt:
			raise
		except:
			print "You messed up, you dingus"
			self.player_turn()

	def computer_turn(self):
		global minimax_calls
		if len(self.get_legal_moves(self.current_player)) != 0:
			computer_move = minimax(self, 0)
			computer_move = computer_move[1]
			print "FROM BOARD:"
			print self.board
			if computer_move is not None:
				self.board.movePiece(computer_move[0], computer_move[1])
				print(self.board)
				print "Made move: ", ((computer_move[0][0]+1, computer_move[0][1]+1), (computer_move[1][0]+1, computer_move[1][1]+1))
				self.last_move_made = computer_move
				self.current_player = 1 - self.current_player
			else:
				random_move =  random.choice(self.get_legal_moves(self.current_player))
				self.board.movePiece(random_move[0], random_move[1])
				print(self.board)
				print "Made move: ", ((random_move[0][0]+1, random_move[0][1]+1), (random_move[1][0]+1, random_move[1][1]+1))	# to present the computer's move nicely to player
				self.last_move_made = computer_move
				self.current_player = 1 - self.current_player
		else:
			self.endgame = 1
			print "Player", self.player_symbol[self.current_player], "loses!"

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

	def static_evaluation(self):
		my_moves = self.get_legal_moves(0)
		opponent_moves = self.get_legal_moves(1)
		if opponent_moves == 0:
			return float("inf")
		if my_moves == 0:
			return float("-inf")
		return len(my_moves) - len(opponent_moves)

def play_game(game_state):
	print game_state.board
	to_remove = input("x remove a piece: ")
	game_state.board.removePiece((to_remove[0]-1,to_remove[1]-1))
	print game_state.board
	to_remove = input("o remove a piece: ")
	game_state.board.removePiece((to_remove[0]-1,to_remove[1]-1))
	while game_state.endgame != 1:
		if game_state.current_player == 0:
			game_state.computer_turn()
		else:
			game_state.computer_turn()

def test_game(game_state):
	game_state.board.removePiece((3,3))
	print game_state.board
	game_state.board.removePiece((3,2))
	print game_state.board
	while game_state.endgame != 1:
		if game_state.current_player == 0:
			game_state.computer_turn()
		else:
			game_state.computer_turn()


if __name__ == '__main__':
	start = time.time()
	test_game(Game(8,Board(8)))
	print "GAME TOOK", time.time() - start, "SECONDS"
	print "NUM STATIC EVALS:", static_eval_count
	print "AVG BRANCHING FACTOR:", total_branches/(minimax_calls+0.0)
	print "NUM CUTOFFS", cutoffs
