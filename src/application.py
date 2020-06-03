import pygame
from maze import Maze
from button import Button


class Application:

	def __init__(self):

		# Initialize the pygame library.
		pygame.init()
		# Set up the drawing window.
		self.screen = pygame.display.set_mode((800, 600))
		# Set the window caption.
		pygame.display.set_caption("Maze generator")
		self.running = True

		# Configuration.
		self.size = (600, 600)
		self.n = 20
		self.delay = 5
		self.filePath = "../output/maze.png"

		# Create components.
		self.maze = Maze(self.screen, self.size, self.n)
		self.maze.setDelay(self.delay)
		self.generateButton = Button(self.screen, (0, 150, 0), 600,   0, 200, 100, "Generate maze")
		self.exportButton   = Button(self.screen, (0, 150, 0), 600, 100, 200, 100, "Export as PNG")
		self.resetButton    = Button(self.screen, (0, 150, 0), 600, 200, 200, 100, "Reset")
		

	def run(self):
		# Run until the user wants to quit.
		while self.running:
			# Delay.
			#pygame.time.delay(100)

			# Check if any new event has occured.
			self.handleEvents()

			# Draw
			self.draw()

			# Flip the display.
			pygame.display.flip()

		# Done! now quit.
		pygame.quit()


	def handleEvents(self):
		for event in pygame.event.get():
			mouse = pygame.mouse.get_pos()

			# Check if user presses exit.
			if event.type == pygame.QUIT:
				self.running = False

			# Check for mouse clicks.
			if event.type == pygame.MOUSEBUTTONDOWN:
				# Generate maze button.
				if self.generateButton.isOver(mouse):
					if not self.maze.solved:
						self.maze.generate()
				# Export button.
				if self.exportButton.isOver(mouse):
					pygame.image.save(self.screen.subsurface(pygame.Rect((0, 0), self.size)), self.filePath)
					print("Exported maze as PNG.")
				# Reset button.
				if self.resetButton.isOver(mouse):
					self.maze = Maze(self.screen, self.size, self.n)
					self.maze.setDelay(self.delay)

			# Check mouse position.
			if event.type == pygame.MOUSEMOTION:
				# Generate maze button.
				if self.generateButton.isOver(mouse):
					self.generateButton.color = (0, 175, 0)
				else:
					self.generateButton.color = (0, 150, 0)
				# Export button.
				if self.exportButton.isOver(mouse):
					self.exportButton.color = (0, 175, 0)
				else:
					self.exportButton.color = (0, 150, 0)
				# Reset button.
				if self.resetButton.isOver(mouse):
					self.resetButton.color = (0, 175, 0)
				else:
					self.resetButton.color = (0, 150, 0)


	def draw(self):
		self.screen.fill((0, 0, 0))
		self.maze.draw()
		self.generateButton.draw()
		self.exportButton.draw()
		self.resetButton.draw()