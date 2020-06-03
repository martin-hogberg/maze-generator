import pygame


class Button:

	def __init__(self, screen, color, x, y, width, height, text):
		self.screen = screen
		self.color = color
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.font = pygame.font.SysFont('consolas', 20)
		self.text = text


	def draw(self):
		pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

		pygame.draw.line(self.screen, (0,0,0), (self.x, self.y), (self.x+self.width, self.y))
		pygame.draw.line(self.screen, (0,0,0), (self.x, self.y), (self.x, self.y+self.height))
		pygame.draw.line(self.screen, (0,0,0), (self.x+self.width-1, self.y), (self.x+self.width-1, self.y+self.height))	
		pygame.draw.line(self.screen, (0,0,0), (self.x, self.y+self.height-1), (self.x+self.width-1, self.y+self.height-1))

		text = self.font.render(self.text, 1, (0,0,0))
		self.screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))


	def isOver(self, pos):
		if pos[0] > self.x and pos[0] < self.x + self.width:
			if pos[1] > self.y and pos[1] < self.y + self.height:
				return True
		return False