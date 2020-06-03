import pygame
import random
from grid import Grid


class Maze():

	def __init__(self, screen, size, n):
		self.screen = screen
		self.size = size
		self.n = n
		self.grid = Grid((0, 0), self.size, self.n)
		self.delay = 0
		self.solved = False


	def setDelay(self, delay):
		self.delay = delay


	def draw(self):
		self.grid.draw(self.screen)


	def generate(self):
		# Create a stack.
		stack = []

		# Choose a starting cell, mark it as visited & push it to the stack.
		current_cell = (0, 0)
		self.grid.setVisited(current_cell)
		stack.append(current_cell)

		# Loop while stack is not empty.
		while len(stack) > 0:
			# Pop a cell from the stack and make it the current cell.
			current_cell = stack.pop()
			
			# Check if the current cell has any unvisited neighbours.
			unvisited_neighbours = self.grid.getAvailableNeighbours(current_cell)
			
			if len(unvisited_neighbours) > 0:
				# Push the current cell to the stack.
				stack.append(current_cell)
				# Choose one of the unvisited neighbours by random.
				chosen_cell = random.choice(unvisited_neighbours)
				# Remove the wall between the current cell and the chosen cell.
				self.grid.connectCells(current_cell, chosen_cell)
				# Mark the chosen cell as visited and push it to the stack.
				self.grid.setVisited(chosen_cell)
				stack.append(chosen_cell)

			# Call draw to update the visualization.
			pygame.time.delay(self.delay)
			self.grid.mark(current_cell)
			self.draw()
			self.grid.unmark(current_cell)
			pygame.display.flip()

		# Mark maze as solved.
		self.solved = True
