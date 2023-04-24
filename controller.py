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

import numpy
allState = numpy.load('allState.npy')

from queue import PriorityQueue
class Astar:
	def __init__(self, initial_state):
		self.initial_state = initial_state
		self.goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 9]

	def solve(self):
		open_list = PriorityQueue()
		open_list.put((0, self.initial_state))
		came_from = {}
		cost_so_far = {}
		came_from[str(self.initial_state)] = None
		cost_so_far[str(self.initial_state)] = 0

		while not open_list.empty():
			current = open_list.get()[1]

			if current == self.goal_state:
				break

			for next in self.get_neighbors(current):
				new_cost = cost_so_far[str(current)] + 1
				if str(next) not in cost_so_far or new_cost < cost_so_far[str(next)]:
					cost_so_far[str(next)] = new_cost
					priority = new_cost + self.heuristic(next)
					open_list.put((priority, next))
					came_from[str(next)] = current

		return came_from, cost_so_far

	def get_neighbors(self, state):
		neighbors = []
		zero_index = state.index(9)
		if zero_index in [3, 4, 5, 6, 7, 8]:
			new_state = state[:]
			new_state[zero_index], new_state[zero_index - 3] = new_state[zero_index - 3], new_state[zero_index]
			neighbors.append(new_state)
		if zero_index in [0, 1, 2, 3, 4, 5]:
			new_state = state[:]
			new_state[zero_index], new_state[zero_index + 3] = new_state[zero_index + 3], new_state[zero_index]
			neighbors.append(new_state)
		if zero_index in [1, 2, 4, 5, 7, 8]:
			new_state = state[:]
			new_state[zero_index], new_state[zero_index - 1] = new_state[zero_index - 1], new_state[zero_index]
			neighbors.append(new_state)
		if zero_index in [0, 1, 3, 4, 6, 7]:
			new_state = state[:]
			new_state[zero_index], new_state[zero_index + 1] = new_state[zero_index + 1], new_state[zero_index]
			neighbors.append(new_state)
		return neighbors

	def heuristic(self,state):
		distance=0
		for i in range(1,len(state)):
			x,y=divmod(state.index(i),3)
			x1,y1=divmod(self.goal_state.index(i),3)
			distance+=abs(x-x1)+abs(y-y1)
		return distance


from collections import deque
class DFS:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    def is_goal(self, state):
        return state == self.goal_state

    def get_next_states(self, state):
        next_states = []
        zero_index = state.index(9)
        zero_row = zero_index // 3
        zero_col = zero_index % 3
        for move in self.moves:
            next_row = zero_row + move[0]
            next_col = zero_col + move[1]
            if next_row >= 0 and next_row < 3 and next_col >= 0 and next_col < 3:
                new_state = state.copy()
                swap_index = next_row * 3 + next_col
                new_state[zero_index], new_state[swap_index] = new_state[swap_index], new_state[zero_index]
                next_states.append(new_state)
        return next_states

    def solve(self):
        stack = deque([self.initial_state])
        came_from = {}
        visited = set()
        while stack:
            current_state = stack.pop()
            if self.is_goal(current_state):
                current = current_state
                path = [current]
                while current != self.initial_state:
                    current = came_from[str(current)]
                    path.append(current)
                path.reverse()
                return came_from, len(path) - 1
            if tuple(current_state) not in visited:
                visited.add(tuple(current_state))
                next_states = self.get_next_states(current_state)
                for next_state in next_states:
                    if str(next_state) not in came_from:
                        came_from[str(next_state)] = current_state
                    stack.append(next_state)
        return came_from, float('inf')


class BFS:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    def is_goal(self, state):
        return state == self.goal_state

    def get_next_states(self, state):
        next_states = []
        zero_index = state.index(9)
        zero_row = zero_index // 3
        zero_col = zero_index % 3
        for move in self.moves:
            next_row = zero_row + move[0]
            next_col = zero_col + move[1]
            if next_row >= 0 and next_row < 3 and next_col >= 0 and next_col < 3:
                new_state = state.copy()
                swap_index = next_row * 3 + next_col
                new_state[zero_index], new_state[swap_index] = new_state[swap_index], new_state[zero_index]
                next_states.append(new_state)
        return next_states

    def solve(self):
        queue = deque([self.initial_state])
        came_from = {}
        visited = set()
        while queue:
            current_state = queue.popleft()
            if self.is_goal(current_state):
                current = current_state
                path = [current]
                while current != self.initial_state:
                    current = came_from[str(current)]
                    path.append(current)
                path.reverse()
                return came_from, len(path) - 1
            if tuple(current_state) not in visited:
                visited.add(tuple(current_state))
                next_states = self.get_next_states(current_state)
                for next_state in next_states:
                    if str(next_state) not in came_from:
                        came_from[str(next_state)] = current_state
                    queue.append(next_state)
        return came_from, float('inf')