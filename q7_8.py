"""
# Chapter 7: Object-oriented Design
# Problem 2: 

Othello is played as follows: Each Othello piece is white on one side and black on the other 
When a piece is surrounded by its opponents on both the left and right sides, or both the top and bottom, 
it is said to be captured and its color is flipped On your turn, 
you must capture at least one of your opponent’s pieces The game ends when either user has no more valid moves, 
and the win is assigned to the person with the most pieces Implement the object oriented design for Othello
"""

################################################################################
################################################################################
################################################################################
# SOLUTIONS

"""
Solution 1 : 

designed for 2 players 
only one main class that hides a lot of inner functions
when started, runs continously until game is over

"""


class Question(object) :

	white = 1
	black = 2

	def start(self) :
		"""
		Sets up board into valid starting positions
		"""

	def _won(self) :
		"""
		Retunrns winner if any, else 0
		"""

	def _canGo(self, color) :
		"""
		returns True if color has valid move on his turn, else false
		"""

	def _isValid(self, color, pos) :
		"""
		returns true if pos is local move for color
		"""

	def _getMove(self, color) :
		"""
		prompts player for move, exception is invalid input
		"""

	def _addMove(self, color, pos) :
		"""
		adds valid move to the board, and updates pieces on board
		"""

	def _printBoard(self) :
		"""
		prints current state of board
		"""

	def _game(self) :
		"""
		runs continously until a player wins
		"""
		self._printBoard()
		while(self._won() == 0) :
			valid = False
			while(not valid) :
				try :
					self._getMove()
					valid = True
				except :
					print "enter valid coordinate"
			self._printBoard()

		if self._won() != 3 :
			if self._won() == 1 :
				print "white won"
			else :
				print "black won"
		else :
			print "draw!"

"""
Solution 2 : 

Setting up like we did for the card game in peter norvig's class
"""


class Game(object) :

	def __init__(self) : 

	def newGame(self, numPlayers, size) :

	def getTurn() :

	def isFinished() :

class Board(object) :

	def __init__(self) :

	def getMoves(self, color) :

	def setMove(self, color, loc) :

	def printBoard(self) :

#player is strategy function


