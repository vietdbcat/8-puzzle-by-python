import pygame

class Button():
	def __init__(self, x, y, w, h, txt, size, color,color_text, screen):
		self.button = pygame.Surface((w,h))

		self.txt = pygame.font.SysFont('Comic Sans MS', size).render(txt, False, color_text)
		self.button.fill(color)

		txtRect = self.txt.get_rect(center = (w/2, h/2))
		self.button.blit(self.txt, txtRect)

		self.rect = self.button.get_rect(center = (x,y))

	def update(self, screen):
		screen.blit(self.button, self.rect)

	def clicked(self):
		x, y = pygame.mouse.get_pos()
		return self.rect.collidepoint(x, y)


