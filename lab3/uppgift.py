import math
def new_board():
	board = {}
	return board

def is_free(board,x,y):
	retVal = False
	if (x,y) in board:
		pass
	else:
		retVal = True
	return retVal

def place_piece(board,x,y,piece):
	retVal = False
	if is_free(board,x,y):
		board[(x,y)] = piece
		retVal = True		
	return retVal

def get_piece(board,x,y):
	retVal = False
	if not is_free(board,x,y):
		retVal = board[(x,y)]
	return retVal

def count(board, cr,pos, type):
	count = 0
	if cr == "column":
		for k,v in board.items():
			if k[0] == pos and v == type:
				count += 1
	if cr == "row":
		for k,v in board.items():
			if k[1] == pos and v == type:
				count +=1
	return count

def nearest_piece(board,x,y):
	d = math.inf
	coords = 0
	for k,v in board.items():
		newDistance =  math.sqrt((k[0] - x)**2 + (k[1] - y)**2)
		
		if newDistance < d:
			d = newDistance
			
			coords = (k[0],k[1])
			
	return coords

def remove_piece(board,x,y):
	retVal = False
	if not is_free(board,x,y):
		del board[(x,y)]
		retVal = True
	return retVal

def move_piece(board,fromX,fromY,toX,toY):
	retVal = False
	if not is_free(board,fromX,fromY):
		board[toX,toY] = board.pop((fromX,fromY))
		retVal = True
	return retVal	
