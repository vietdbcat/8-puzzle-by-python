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
FPS = 60

image = pygame.image.load('monalisa.webp')
allState = numpy.load('allState.npy')
pos = numpy.load('position.npy')

puzzle = Puzzle(image = image, size=600, allState = allState, pos = pos)
newimg = pygame.transform.scale(image, (160,160))

##Button
start = Button(700,80,120,50, 'Start', 20, (255,255,255), screen)
restart = Button(700,150,120,50, 'Restart', 20, (255,255,255), screen)
quit = Button(700,220,120,50, 'Quit', 20, (255,255,255), screen)


def AIPlayGame(Player):
	puzzle.reset()

	initial_state = puzzle.state
	player = Player(initial_state)
	came_from, _ = player.solve()

	current = player.goal_state
	path = [current]
	while current != player.initial_state:
		current = came_from[str(current)]
		path.append(current)
	path.reverse()

	i = 0
	started = False
	win = False
	run = True
	while run:
		screen.fill((0,200,150)) #fill screen by color
		clock.tick(FPS) #get the frame rate

		screen.blit(newimg, (620,430))
		start.update(screen)
		restart.update(screen)
		quit.update(screen)

		puzzle.update(screen)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				Exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					menu()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if start.clicked():
					started = True
				if restart.clicked():
					AIPlayGame(Player)
				if quit.clicked():
					menu()
		
		if started:
			puzzle.state = path[i]
			if i < len(path)-1:
				i+=1
				puzzle.nofmove += 1

		pygame.display.flip()
	pygame.quit()

def PlayGame(Player):
	puzzle.reset()
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
					menu()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if restart.clicked():
					PlayGame(Player)
				if quit.clicked():
					menu()
				if event.button == 1:
					puzzle.push(Player(mouse_x, mouse_y, puzzle))
		pygame.display.flip()
	pygame.quit()

def Exit():
	sys.exit()

astar = Button(SCREEN_WIDTH/2,100,200,50, 'A STAR', 20, (255,255,255), screen)
dfs = Button(SCREEN_WIDTH/2,170,200,50, 'DFS', 20, (255,255,255), screen)
bfs = Button(SCREEN_WIDTH/2,240,200,50, 'BFS', 20, (255,255,255), screen)
hmplayer = Button(SCREEN_WIDTH/2,310,200,50, 'HUMAN PLAYER', 20, (255,255,255), screen)
exit = Button(SCREEN_WIDTH/2,380,200,50, 'EXIT', 20, (255,255,255), screen)

def menu():
	run = True
	while run:
		screen.fill((0,200,150)) #fill screen by color
		clock.tick(FPS) #get the frame rate

		astar.update(screen)
		dfs.update(screen)
		bfs.update(screen)
		hmplayer.update(screen)
		exit.update(screen)


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				Exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					Exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if hmplayer.clicked():
					PlayGame(HumanPlayer)
				if astar.clicked():
					AIPlayGame(Astar)
				if dfs.clicked():
					AIPlayGame(DFS)
				if bfs.clicked():
					AIPlayGame(BFS)
				if exit.clicked():
					Exit()

		pygame.display.flip()
	pygame.quit()

if __name__ == "__main__":
	menu()