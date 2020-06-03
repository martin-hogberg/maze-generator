import pygame
from cell import Cell


class Grid:
	
	def __init__(self, pos, size, n):
		self.pos = pos
		self.size = size
		self.n = n
		self.grid = []
		self.cellWidth = self.size[0] / self.n

		for y in range(0, n):
			for x in range(0, n):
				cell = Cell( (x*self.cellWidth, y*self.cellWidth) , (self.cellWidth, self.cellWidth) )
				self.grid.append(cell)


	def draw(self, screen):
		for x in range(0, self.n):
			for y in range(0, self.n):
				cell = self.grid[self.getIndex((x, y))]
				# Draw cell.
				pygame.draw.rect(screen, cell.color, cell)
				# Draw walls.
				if cell.walls.get("top"):
					pygame.draw.line(screen, (0,0,0), (cell.pos[0], cell.pos[1]), (cell.pos[0]+cell.size[0], cell.pos[1]))
				if cell.walls.get("left"):
					pygame.draw.line(screen, (0,0,0), (cell.pos[0], cell.pos[1]), (cell.pos[0], cell.pos[1]+cell.size[1]))
				if cell.walls.get("right"):
					pygame.draw.line(screen, (0,0,0), (cell.pos[0]+cell.size[0]-1, cell.pos[1]), (cell.pos[0]+cell.size[0]-1, cell.pos[1]+cell.size[1]))
				if cell.walls.get("bottom"):
					pygame.draw.line(screen, (0,0,0), (cell.pos[0], cell.pos[1]+cell.size[1]-1), (cell.pos[0]+cell.size[0]-1, cell.pos[1]+cell.size[1]-1))


	def mark(self, pos):
		self.grid[self.getIndex(pos)].color = (100, 200, 255)


	def unmark(self, pos):
		self.grid[self.getIndex(pos)].color = (255, 255, 255)


	def setVisited(self, pos):
		self.grid[self.getIndex(pos)].visited = True


	def connectCells(self, pos1, pos2):
		# Horizontal ?
		if pos1[1] == pos2[1]:
			# Left -> Right ?
			if pos1[0] < pos2[0]:
				self.grid[self.getIndex(pos1)].walls["right"] = False #1
				self.grid[self.getIndex(pos2)].walls["left"] = False #2
			# Right -> Left ?
			else:
				self.grid[self.getIndex(pos1)].walls["left"] = False #1
				self.grid[self.getIndex(pos2)].walls["right"] = False #2

		# Vertical ?
		else:
			# Top -> Bottom ? 
			if pos1[1] < pos2[1]:
				self.grid[self.getIndex(pos1)].walls["bottom"] = False #1
				self.grid[self.getIndex(pos2)].walls["top"] = False #2
			# Bottom -> Top ?
			else:
				self.grid[self.getIndex(pos1)].walls["top"] = False #1
				self.grid[self.getIndex(pos2)].walls["bottom"] = False #2


	# Returns list of coordinates to all available neighbours.
	def getAvailableNeighbours(self, pos):
		x, y = pos
		neighbours = []

		for offset_x in [-1, 1]:
			nx = x + offset_x
			if nx >= 0 and nx < self.n:
				cell = self.grid[self.getIndex((nx, y))]
				if not cell.visited:
					neighbours.append((nx, y))

		for offset_y in [-1, 1]:
			ny = y + offset_y
			if ny >= 0 and ny < self.n:
				cell = self.grid[self.getIndex((x, ny))]
				if not cell.visited:
					neighbours.append((x, ny))
		
		return neighbours


	# Matches coordinates to the correct index in list
	# using the formula: index = x + y * width.
	def getIndex(self, pos):
		return pos[0] + pos[1] * self.n