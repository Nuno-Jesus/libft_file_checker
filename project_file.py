from utils import *

class ProjectFile:
	def __init__(self, func, header, allowed_funcs):
		self.func = func
		self.header = header
		self.allowed_funcs = allowed_funcs
		self.wasDelivered = False

	def check_prototype(self):
		found_name = False
		f = open(self.func + '.c', 'r')

		line = f.readline()
		while line != '':
			line = line.replace('\n', '')
			
			if line == self.header:
				f.close()
				return {self.func : f'[{correct_color}CORRECT{reset}]'}

			line = f.readline()
		f.close()
		return {self.func : f'[{danger_color}NOT FOUND{reset}]'}