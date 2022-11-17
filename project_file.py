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
			if len(delivered) == len(expected):
				if delivered[1] == expected[1]:
					if delivered != expected:
						r = open('results.log', 'a')
						r.write(f'In {self.func}.c:\n')
						r.write(f'\tExpected: {str(expected)}\n')
						r.write(f'\tDelivered: {str(delivered)}\n')
						return {delivered[1] : f'[{WARNING}MISMATCHING{RESET}]'}
					else:
						return {delivered[1] : f'[{CORRECT}CORRECT{RESET}]'}
			line = f.readline()

		f.close()
		return {f'{self.func}.c : {self.header}' : f'[{DANGER}MISSING{RESET}]'}

	def find_header_prototypes(self, full_dict) -> dict:
		headers_result = {}
		possible_headers = {}

		for func_name, file in full_dict.items():
			if func_name.startswith('ft_'):
				expected = tokenize(file.header.strip('\n'))
				possible_headers.update({func_name.replace('.c', '') : expected})

		f = open(path + 'libft.h', 'r')
		line = f.readline()
		while line != '':
			# Tokenization of the current line
			delivered = tokenize(line.strip(';\n'))
			
			# If I found a prototype
			if line.endswith(');\n'):
				if delivered[1] in possible_headers.keys():
					if possible_headers[delivered[1]] != delivered:
						r = open('results.log', 'a')
						r.write(f'In libft.h:\n')
						r.write(f'\tExpected: {str(possible_headers[delivered[1]])}\n')
						r.write(f'\tDelivered: {str(delivered)}\n')
						headers_result.update({delivered[1] : f'[{FATAL}MISMATCHING{RESET}]'})
					else:
						headers_result.update({delivered[1] : f'[{CORRECT}CORRECT{RESET}]'})
					possible_headers.pop(delivered[1])
				else:
					headers_result.update({line.strip(';\n') : f'[{WARNING}UNKNOWN{RESET}]'})
			line = f.readline()

		f.close()

		 # Any header that wasn't removed from the dict, wasn't found
		for func in possible_headers.keys():
			headers_result.update({full_dict[func + '.c'].header : f'[{DANGER}MISSING{RESET}]'})
		
		return headers_result

	