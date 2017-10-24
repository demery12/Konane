class Board:
	def __init__(self, size):
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
		display = ""
		for row in self.repr:
			for piece in row:
				display += piece+" "
			display += "\n"
		return display

	def modify(self, from_pos, to_pos):		# Assuming from_pos and to_pos are coordinate tuples
		""" Modifies the game board when moving pieces """
		moved_piece = self.repr[from_pos[0]][from_pos[1]]	# Saves the type of the piece we are moving (whether it is "X" or "O")
		self.repr[from_pos[0]][from_pos[1]] = "."
		for x in range(from_pos[0], to_pos[0]+1):		# In order to iterate between the values of the from and to positions
			for y in range(from_pos[1], to_pos[1]+1):	# Deletes every piece between the moving piece's starting and ending positions
				self.repr[x][y] = "."
		self.repr[to_pos[0]][to_pos[1]] = moved_piece	# Places the piece in it's final position

	def removePiece(self, pos):		# pos should be a coordinate tuple
		""" Modifies the board by removing a piece at specified coordinate """
		self.repr[pos[0]][pos[1]] = "."

testBoard = Board(8)
print(testBoard)
testBoard.modify((1,0),(1,4))
print(testBoard)
testBoard2 = Board(6)
testBoard2.modify((2,2),(4,2))
print(testBoard2)
testBoard3 = Board(8)
testBoard3.removePiece((4,4))
print(testBoard3)
print(testBoard3)



