import sys
from utils import *

class ProjectFile:
	def __init__(self, func, header, allowed_funcs):
		self.func = func
		self.header = header
		self.allowed_funcs = allowed_funcs
		self.wasDelivered = False

	def check_prototype(self):
		f = open(path + self.func + '.c', 'r')

		line = f.readline()
		while line != '':
			line = line.replace('\n', '')

			expected = tokenize(self.header)
			delivered = tokenize(line)
			if delivered == expected:
				f.close()
				return {self.func : f'[{correct_color}CORRECT{reset}]'}

			line = f.readline()
		f.close()
		return {self.func : f'[{warning_color}NOT FOUND{reset}]'}