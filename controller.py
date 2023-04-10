size = 200
k = 3
def HumanPlayer(x, y, puzzle): #x,y = mouse_x, mouse_y
	move = 0
	if y < size:
		if x < size: move =  1
		elif x < size*2: move =  2
		elif x < size*3: move =  3
	elif y < size*2:
		if x < size: move =  4
		elif x < size*2: move =  5
		elif x < size*3: move =  6
	elif y < size*3:
		if x < size: move =  7
		elif x < size*2: move =  8
		elif x < size*3: move =  9

	epi = puzzle.state.index(9)
	if move in puzzle.moveAble[epi]:
		return move

import random
def RandomPlayer(puzzle):
	epi = puzzle.state.index(9)
	while True:
		i = random.randint(0,9)
		if i in puzzle.moveAble[epi]:
			return i

class State:
	def __init__(self, current_state, previous_state):
		self.state = current_state
		self.pre_state = previous_state
		self.g = 0
		self.h = 0


mahathan = [[0,1,2,1,2,3,2,3,4],
			 [1,0,1,2,1,2,3,2,3],
			 [2,1,0,3,2,1,4,3,2],
			 [1,2,3,0,1,2,1,2,3],
			 [2,1,2,1,0,1,2,1,2],
			 [3,2,1,2,1,0,3,2,1],
			 [2,3,4,1,2,3,0,1,2],
			 [3,2,3,2,1,2,1,0,1],
			 [4,3,2,3,2,1,2,1,0]]
def heuristic(state):
	h = 0
	for i in range(0,9):
		h += mahathan[state[i]-1][i]
	return h


class Asao:
	def __init__(self, current_state):
		self.open = [current_state]
		self.close = []

	def solve(self):
		while len(self.open) > 0:
			state = min(self.open)

def BfsPlayer():
	pass
def DfsPlayer():
	pass