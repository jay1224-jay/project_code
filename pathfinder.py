import os

class pathfinder:

	def __init__(self, MAP, START, END):
		self.map = MAP
		self.start = START
		self.end = END
		self.map[self.start[1]][self.start[0]] = 1

		self.print_map()
		print()
		
		#self.test()
		self.find_path()
		self.go_back()

		self.print_map()

	def r8neighbor(self, curr_point):
		NEIGHBOR = []
		x = curr_point[0]
		y = curr_point[1]

		if x>0:
			if self.map[y][x-1] >0:                  
				NEIGHBOR.append([x-1, y])

			if y>0:
				if self.map[y-1][x-1] >0:
					NEIGHBOR.append([x-1, y-1])

		if x+1<len(self.map[y]): 
			if self.map[y][x+1] >0:   
				NEIGHBOR.append([x+1, y])

			if y < len(self.map) - 1 and x>0:
				if self.map[y+1][x-1] > 0:
					NEIGHBOR.append([x-1, y+1])

		if y<len(self.map)-1:
			if self.map[y+1][x] > 0:
				NEIGHBOR.append([x, y+1])

			if x + 1 < len(self.map[y]):
				if self.map[y+1][x+1] >0:
					NEIGHBOR.append([x+1, y+1]) 

		if y>0: 
			if self.map[y-1][x] >0:                  
				NEIGHBOR.append([x, y-1])

			if x + 1 < len(self.map[y]):
				if self.map[y-1][x+1] >0:
					NEIGHBOR.append([x+1, y-1]) 


		return NEIGHBOR

	def neighbor(self, curr_point):

		NEIGHBOR = []
		x = curr_point[0]
		y = curr_point[1]

		if x>0:
			if self.map[y][x-1] == 0:                  
				NEIGHBOR.append([x-1, y])

		if x+1<len(self.map[y]): 
			if self.map[y][x+1] == 0:   
				NEIGHBOR.append([x+1, y])

		if y<len(self.map)-1:
			if self.map[y+1][x] == 0:
				NEIGHBOR.append([x, y+1])

		if y>0: 
			if self.map[y-1][x] == 0:                  
				NEIGHBOR.append([x, y-1])

		return NEIGHBOR

	def print_map(self):
		for y in self.map:
			for x in y:
				if x == -1: 
					print("w  ", end="")
					continue
				print("%-2s " % x, end="")
			print()

	def find_path(self):

		step=1
		discovered_point=[self.start]
		selected_point=[]

		while discovered_point:
			
			step+=1
			for point in discovered_point:
				selected_point+=self.neighbor(point)

			for point in selected_point:
				self.map[point[1]][point[0]] = step
				if [point[0], point[1]] == self.end: 
					return 0
			"""
			self.print_map()
			input()
			os.system("clear")
			"""

			discovered_point = selected_point
			selected_point=[]



	def go_back(self):
		curr_point = self.end
		self.path = []
		while curr_point != self.start:
			for point in self.r8neighbor(curr_point):
				if self.map[point[1]][point[0]] < self.map[curr_point[1]][curr_point[0]]:
					curr_point = point
			if curr_point == self.end: break
			self.path.append(curr_point)

		for point in self.path:
			self.map[point[1]][point[0]] = '-'

		self.map[self.end[1]][self.end[0]] = 'R'


	def test(self):
		node=[0,2]
		self.map[node[1]][node[0]] = 'F'
		print(self.r8neighbor(node))
		for point in self.r8neighbor(node):
			print("in")
			self.map[point[1]][point[0]] = 'f'



road_map = [
			[0, 0, 0, 0, 0, 0, 0],
			[-1, -1, -1, -1, 0, -1, -1],
			[0, 0, 0, -1, 0, 0, 0],
			[0, 0, 0, -1, 0, 0, 0],
			[0, 0, 0, -1, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0],
			]


pathfinder(road_map, [0, 0], [2, 2])
		
