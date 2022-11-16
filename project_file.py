import sys
from utils import *

class ProjectFile:
	def __init__(self, func, header, allowed_funcs):
		self.func = func
		self.header = header
		self.allowed_funcs = allowed_funcs
		self.wasDelivered = False

	def find_prototype(self):
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

	def find_header_prototypes(self, dict) -> dict:
		headers_result = {}
		possible_headers = {}

		for key, func in dict.items():
			if key.startswith('ft_'):
				normalized_header = ''.join(filter(lambda c : c != '\t' and c != '\n', func.header))
				possible_headers.update({normalized_header : key})
		
		f = open(path + 'libft.h', 'r')
		line = f.readline()
		while line != '':
			# Filter the current line out of tabs, spaces
			tmp = ''.join(filter(lambda c : c != '\t' and c != '\n', line)).strip(';')
			
			if line.endswith(');\n') and tmp not in possible_headers.keys():
				headers_result.update({line.strip('\n') : f'[{warning_color}UNKNOWN{reset}]'})
			elif tmp in possible_headers.keys():
				headers_result.update({possible_headers[tmp].strip('.c') : f'[{correct_color}CORRECT{reset}]'})
				possible_headers.pop(tmp)

			line = f.readline()
		f.close()

		# Any header that wasn't removed from the dict, wasn't found
		for func in possible_headers.values():
			headers_result.update({dict[func].header : f'[{danger_color}NOT FOUND{reset}]'})
		
		return headers_result

	