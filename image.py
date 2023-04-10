import pygame
import numpy
from itertools import permutations

class Image():
	def __init__(self, image, size):
		self.img = pygame.transform.scale(image, (size, size))
		self.size = size/3
		self.empty_puzzle = pygame.Surface((self.size, self.size))
		self.empty_puzzle.fill((255,255,255))
		self.list = {1:self.img.subsurface(0, 0, self.size, self.size),
		            2:self.img.subsurface(self.size, 0, self.size, self.size),
		            3:self.img.subsurface(2*self.size, 0, self.size, self.size),

		            4:self.img.subsurface(0, self.size, self.size, self.size),
		            5:self.img.subsurface(self.size, self.size, self.size, self.size),
		            6:self.img.subsurface(2*self.size, self.size, self.size, self.size),
		            
		            7:self.img.subsurface(0, 2*self.size, self.size, self.size),
		            8:self.img.subsurface(self.size, 2*self.size, self.size, self.size),
		            9:self.empty_puzzle}

		self.moveAble = [[2,4],
						[1,3,5],
						[2,6],
						[1,5,7],
						[2,4,6,8],
						[3,5,9],
						[4,8],
						[5,7,9],
						[6,8]]

		line_color = (255,255,255)
		for key,img in self.list.items():
		    pygame.draw.line(img, line_color, (0, 0),(self.size, 0), 4)
		    pygame.draw.line(img, line_color, (0, self.size), (self.size, self.size), 4)
		    pygame.draw.line(img, line_color, (0, 0), (0, self.size), 4)
		    pygame.draw.line(img, line_color, (self.size, 0), (self.size, self.size), 4)

# allState = [1,2,3,4,5,6,7,8,9]
# allState = list(permutations(allState))
# numpy.save('allState', allState)


# # POSITION
# img_size = 200
# pos = [(0, 0), (img_size, 0), (2*img_size, 0), 
#         (0, img_size), (img_size, img_size), (2*img_size, img_size),
#         (0, 2*img_size), (img_size, 2*img_size), (2*img_size, 2*img_size)]
# numpy.save('position',pos)
