#!/usr/bin/python

from random import randint

board = []
t = [1,2,3,4,5]
i = 0
for i in t:
	board.append(["O"]*5)

#print len(board)

def print_board(board):
	for row in board:
		print " ".join(row)
#		print row
#	i = 0
#	for i in range(0,len(board)):
#		print board[i]

#print len(board)
print_board(board)

def print_board(board):
  for row in board:
    print " ".join(row)

def random_row(board):
	x = 0
	y = len(board) - 1
	randrow = randint(x,y)
	return randrow

def random_col(board):
	x = 0
	y = len(board[0]) -1
	randcol = randint(x,y)
	return randcol

#def random_col(randrow):
#	x = 0
#	y = len(board[randrow]) - 1
#	randcol =  randint(x,y)
#	return randcol

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col

#print str(guess_row) + "," + str(guess_col)
turn = 0
for turn in range(4):
	print "You have " + str(3-turn) + "times left!"
	guess_row = input("Guess Row: ")
	guess_col = input("Guess Column: ")
	if ship_row == guess_row and ship_col == guess_col:
		print "Congratulations! You sank my battleship!"
		break
	else:
		if (len(board)-1 < guess_row) or (len(board[0])-1 < guess_col):
			print "Oops, that's not even in the ocean."
		elif board[guess_row][guess_col] == "X":
			print "You guessed that one already."
		else:
			print "lol fail"
			board[guess_row][guess_col] = "X"
		turn += 1
	if turn < len(range(4)):
		print_board(board)
	else:
		print "Game Over"
