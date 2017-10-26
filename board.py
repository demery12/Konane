class Board:
	def __init__(self, size):
		self.columnIndex = [x for x in range(1, size+1)]		# This is for displaying the column numbers only
		self.repr = []
		for i in range(size):	# Adds rows to our matrix
			self.repr.append([])
		# Next few lines fill the board with the pieces
		for i in range(size):		
			for j in range(size):
				if i%2 == 0:
					if j%2 == 0:
						self.repr[i].append("x")
					else:
						self.repr[i].append("o")
				else:
					if j%2 == 0:
						self.repr[i].append("o") 
					else:
						self.repr[i].append("x")

	def __str__(self):
		""" Prints the board """
		display = "  "
		for number in self.columnIndex:
			display += str(number)+" "		# Adds column numbers
		display += "\n"
		rowNumber = 1
		for row in self.repr:
			display += str(rowNumber)+" "	# Adds row numbers
			for piece in row:
				display += piece+" "
			display += "\n"
			rowNumber += 1
		return display

	def movePiece(self, from_pos, to_pos):		# Assuming from_pos and to_pos are coordinate tuples
		""" Modifies the game board when moving pieces """
		moved_piece = self.repr[from_pos[0]][from_pos[1]]	# Saves the type of the piece we are moving (whether it is "X" or "O")
		self.repr[from_pos[0]][from_pos[1]] = "."

		x_range = sorted([from_pos[0], to_pos[0]+1])
		y_range = sorted([from_pos[1], to_pos[1]+1])
		for x in range(*x_range):		# In order to iterate between the values of the from and to positions
			for y in range(*y_range):
				# Deletes every piece between the moving piece's starting and ending positions
				self.repr[x][y] = "."
		self.repr[to_pos[0]][to_pos[1]] = moved_piece	# Places the piece in it's final position

	def removePiece(self, pos):		# pos should be a coordinate tuple
		""" Modifies the board by removing a piece at specified coordinate """
		self.repr[pos[0]][pos[1]] = "."

def testie():
	newBoard = Board(8)
	print(newBoard)
	newBoard.removePiece((4,4))
	print(newBoard)
	newBoard.movePiece((2,4), (4,4))
	print(newBoard)


