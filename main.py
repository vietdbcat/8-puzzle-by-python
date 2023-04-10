import pygame, sys
import numpy
import random
from puzzles import *
from button import *

pygame.init()

#create game window
SCREEN_WIDTH = 800 #pixel
SCREEN_HEIGHT = 600 #pixel

# screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("8 PUZZLE")

#set framerate
clock = pygame.time.Clock()
FPS = 300

image = pygame.image.load('monalisa.webp')
allState = numpy.load('allState.npy')
pos = numpy.load('position.npy')

puzzle = Puzzle(image = image, size=600, allState = allState, pos = pos)
newimg = pygame.transform.scale(image, (160,160))

##Button
restart = Button(700,80,120,50, 'Restart', 20, (255,255,255), screen)
quit = Button(700,150,120,50, 'Quit', 20, (255,255,255), screen)

def reset():
	global puzzle
	puzzle = Puzzle(image = image, size=600, allState = allState, pos = pos)

def AIPlayGame(Player):
	win = False
	run = True
	while run:
		screen.fill((0,200,150)) #fill screen by color
		clock.tick(FPS) #get the frame rate

		screen.blit(newimg, (620,430))
		restart.update(screen)
		quit.update(screen)

		puzzle.update(screen)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				Exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					Choice(0)
			if event.type == pygame.MOUSEBUTTONDOWN:
				if restart.clicked():
					puzzle.reset()
				if quit.clicked():
					Choice(0)
		if not puzzle.win:
			move = Player(puzzle)
			puzzle.push(move)
			win = puzzle.Won()

		pygame.display.flip()
	pygame.quit()

def PlayGame(Player):
	run = True
	while run:
		screen.fill((0,200,150)) #fill screen by color
		clock.tick(FPS) #get the frame rate

		screen.blit(newimg, (620,430))
		restart.update(screen)
		quit.update(screen)

		puzzle.update(screen)
		
		mouse_x, mouse_y = pygame.mouse.get_pos()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				Exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					Choice(0)
			if event.type == pygame.MOUSEBUTTONDOWN:
				if restart.clicked():
					puzzle.reset()
				if quit.clicked():
					Choice(0)
				if event.button == 1:
					puzzle.push(Player(mouse_x, mouse_y, puzzle))
		pygame.display.flip()
	pygame.quit()

def Exit():
	sys.exit()


def Choice(choice):
	if choice == 0: Exit()
	if choice == 1:
		reset()
		PlayGame(HumanPlayer)

if __name__ == "__main__":
	PlayGame(HumanPlayer)