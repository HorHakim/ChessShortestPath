import random
import numpy
random.seed(1)

class PathFinder:
	def __init__(self, starting_position, goal_position):
		self.starting_position = starting_position
		self.ending_position = ending_position
		self.current_path = [starting_position]
		self.shortest_path_length = float("inf")


	def is_possible_move(self, current_row, current_col, row_deplacement, col_deplacement):
		knight_move = True if abs(row_deplacement) + abs(col_deplacement) == 3 else False

		inside_grid = current_row + row_deplacement < 8 and\
					  current_row + row_deplacement >= 0 and\
					  current_col + col_deplacement < 8 and\
					  current_col + col_deplacement >= 0
		
		in_current_path = (current_row + row_deplacement, current_col + col_deplacement) in self.current_path
		
		return knight_move and inside_grid and not in_current_path


	def get_possible_moves(self):
		moves = []
		current_row, current_col = self.current_path[-1]
		for row_deplacement in [-2, -1, 1, 2]:
			for col_deplacement in [-2, -1, 1, 2]:

				if self.is_possible_move(current_row, current_col, row_deplacement, col_deplacement):
					potential_postion = current_row + row_deplacement, current_col + col_deplacement
					moves.append(potential_postion)

		return moves


	def get_shortest_path_length(self):
		# fonction de résolution du problème
		if len(self.current_path) > self.shortest_path_length - 1 :
			return None

		for possible_move in self.get_possible_moves():
			self.current_path.append(possible_move)
			
			if possible_move == self.ending_position :
				self.shortest_path_length = len(self.current_path) - 1
				self.print_all_moves_of_current_path()


			self.get_shortest_path_length()
			self.current_path.pop()


	def print_all_moves_of_current_path(self):
		for postion in self.current_path[1:]:
			grid = numpy.zeros(shape=(8, 8), dtype=str)
			grid[:] = "O"
			grid[self.starting_position] = "S"
			grid[self.ending_position] = "E"
			grid[postion] = "🔥"
			print(grid)
			print("_"*50)
		print(f"Path length = {self.shortest_path_length}")
		print("_"*100)
		print("\n")

starting_position = random.randint(0, 8), random.randint(0, 8)
ending_position = random.randint(0, 8), random.randint(0, 8)

PathFinder(starting_position, ending_position).get_shortest_path_length()
