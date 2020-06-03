import pygame


class Cell(pygame.Rect):

	def __init__(self, pos, size):
		super().__init__(pos, size)
		self.pos = pos
		self.size = size
		self.color = (200, 200, 200)
		self.walls = {"top": True, "left": True, "right": True, "bottom": True}
		self.visited = False