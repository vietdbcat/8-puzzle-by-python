from controller import *
from image import *
import random
import pygame
class Puzzle(Image):
	def __init__(self, image, size, allState, pos):
		Image.__init__(self, image, size)
		self.allState = allState
		self.pos = pos
		self.state = self.allState[random.randint(0,181440)].tolist()
		self.nofmove = 0
		self.win = False

	def push(self, idd):
		if not self.win:
			epi = self.state.index(9)
			if idd in self.moveAble[epi]:
				self.nofmove += 1
				self.state[epi], self.state[idd-1] = self.state[idd-1], self.state[epi]
			else:
				print('This move is not a legal moves.')

	def update(self, screen):
		self.win = (self.state == [1,2,3,4,5,6,7,8,9])
		txt = pygame.font.SysFont('Comic Sans MS', 20).render("Move: "+str(self.nofmove), False, (255,255,255))
		screen.blit(txt, (620, 200))
		txt = pygame.font.SysFont('Comic Sans MS', 20).render("Win: "+str(self.win), False, (255,255,255))
		screen.blit(txt, (620, 230))
		for i in range(0,9):
			screen.blit(self.list[self.state[i]], self.pos[i])

	def reset(self):
		self.state = self.allState[random.randint(0,181440)].tolist()
		self.nofmove = 0

	def Won(self):
		return self.win





# make sure that the first state can be converted to the goal state
# delete states that can not be converted
# n[i] is the number of value that smaller than the value in key[i]

# import numpy as np
# allState = np.load('allState.npy')
# print(allState.shape)
# def checkLegalState(a):
# 	s = 0
# 	for i in range(0,8):
# 		if a[i] != 9:
# 			for j in range(i+1, 9):
# 				if a[j] < a[i]:
# 					s += 1
# 	return s%2==0
# c = 0
# for i in allState:
# 	if not checkLegalState(i):
# 		c += 1
# 		print('Got an illegal state.')
# print(c)
# i = 0
# while i < len(allState):
# 	if not checkLegalState(allState[i]):
# 		print(i)
# 		allState = np.delete(allState, i, 0)
# 	else: i += 1
# print(allState.shape)
# np.save('allState',allState)


