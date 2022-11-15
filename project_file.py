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
		expected = tokenize(self.header)
		while line != '':
			line = line.replace('\n', '')

			delivered = tokenize(line)
			""" if(self.func == 'ft_lstmap'):
				print(delivered) """
			if delivered == expected:
				f.close()
				return {self.func : f'[{correct_color}CORRECT{reset}]'}

			line = f.readline()
		f.close()
		print(expected)
		return {self.header : f'[{warning_color}NOT FOUND{reset}]'}