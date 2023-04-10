import pygame

class Button():
	def __init__(self, x, y, w, h, txt, size, color, screen):
		self.button = pygame.Surface((w,h))

		self.txt = pygame.font.SysFont('Comic Sans MS', size).render(txt, False, (0,0,0))
		self.button.fill((255,255,255))

		txtRect = self.txt.get_rect(center = (w/2, h/2))
		self.button.blit(self.txt, txtRect)

		self.rect = self.button.get_rect(center = (x,y))

	def update(self, screen):
		screen.blit(self.button, self.rect)

	def clicked(self):
		x, y = pygame.mouse.get_pos()
		return self.rect.collidepoint(x, y)


# class Button():
# 	def __init__(self, x, y, width, height, text, text_size, color,screen):
# 		self.x = x
# 		self.y = y
# 		self.width = width
# 		self.height = height
# 		self.width_highlight = width*2
# 		self.height_highlight = height*2

# 		self.text = pygame.font.SysFont('Comic Sans MS', text_size).render(text, False, BLACK)
# 		self.text_highlight = pygame.font.SysFont('Comic Sans MS', text_size*2).render(text, False, BLACK)
# 		self.color = color
# 		self.color_highlight = BLUE
# 		self.color_update = color

# 		self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
# 		self.rect_highlight = pygame.Rect(self.x-self.width/2, self.y-self.height/2, self.width_highlight, self.height_highlight)

# 		self.txt_rect = self.text.get_rect(center = (self.x + self.width/2, self.y + self.height/2))
# 		self.txt_rect_highlight = self.text_highlight.get_rect(center = (self.x + self.width/2, self.y + self.height/2))
		
		
# 	def update(self,screen):
# 		mouse_x, mouse_y = pygame.mouse.get_pos()
# 		if self.rect.collidepoint(mouse_x, mouse_y):
# 			self.color_update = self.color_highlight
# 			pygame.draw.rect(screen, self.color_update, self.rect_highlight, 0, 5)
# 			screen.blit(self.text_highlight,self.txt_rect_highlight)

# 		else:
# 			self.color_update = self.color
# 			pygame.draw.rect(screen, self.color_update, self.rect, 0, 5)
# 			screen.blit(self.text,self.txt_rect)