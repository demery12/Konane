from board import Board

class Game:
	def __init__(self, board_size, start_player=0):
		self.board_size = board_size
		self.board = Board(board_size)
		self.current_player = start_player
		self.player_symbol = ('x','o')
	def play(self):
		pass
	# Returns a boolean of whether the game is over
	# We need the inputs because we will want it to differ from self when we are down in the minimax tree
	# We might not need self? 
	def end_state(self, board, current_player):
		return False

	# Returns a list of of legal moves, as pairs of pairs e.g [((8,8),(5,8)),...]
	def get_legal_moves(self, current_player):
		# Just check all the things...
		legal_moves = []
		for row in range(self.board_size):
			for col in range(self.board_size):
				if self.board.repr[row][col] == self.player_symbol[current_player]:
					position  = (row,col)
					move_list = [self.north_move(position),
								 self.east_move(position),
								 self.south_move(position),
								 self.west_move(position)]

					for move in move_list:
						if self.is_legal_move(current_player,move):
					 		legal_moves.append(move)

		print legal_moves
		return list()

	# Given a move e.g ((8,8),(5,8)), check if that is legal, return true if it is, false otherwise
	def is_legal_move(self,current_player, move):
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
		# Check the middle spot is the other piece


		return True

	# seqence when it is player's turn
	def player_turn():
		pass

	# sequence when it is computer's turn
	def computer_turn():
		pass

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

def testo():
	mygame = Game(8)
	print(mygame.board)
	mygame.board.removePiece((0,0))
	mygame.board.removePiece((4,4))
	mygame.board.removePiece((5,5))
	mygame.board.removePiece((7,7))
	print(mygame.board)
	mygame.get_legal_moves(0)

testo()