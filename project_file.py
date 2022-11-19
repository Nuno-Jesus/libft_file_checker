import sys
from utils import *

class ProjectFile:
	def __init__(self, func, header, allowed_funcs):
		self.func = func
		self.header = header
		self.allowed_funcs = allowed_funcs
		self.wasDelivered = False

	def find_c_file_prototype(self):
		f = open(path + self.func + '.c', 'r')

		line = f.readline()
		expected = tokenize(self.header)
		while line != '':
			line = line.replace('\n', '')

			delivered = tokenize(line)
			if len(delivered) == len(expected):
				if delivered[1] == expected[1]:
					f.close()
					if delivered != expected:
						self.log('results.log', self.func + '.c',expected, delivered)
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
						self.log('results.log', 'libft.h', possible_headers[delivered[1]], delivered)
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

	def log(self, logfile, filename, expected, delivered):
		f = open(logfile, 'a')
		f.write(f'In {FATAL}{filename}{RESET}:\n')

		str = '\tExpected: ['
		for i in range(len(expected)):
			if i >= len(delivered):
				str += f'\'{CORRECT}{expected[i]}{RESET}\', '
			elif delivered[i] != expected[i]:
				str += f'\'{CORRECT}{expected[i]}{RESET}\', '
			else:
				str += f'\'{expected[i]}\', '
		str += ']\n'
		str = str.replace(', ]', ']')
		f.write(str)

		str = '\tDelivered: ['
		for i in range(len(delivered)):
			if i >= len(expected):
				str += f'\'{DANGER}{delivered[i]}{RESET}\', '
			elif delivered[i] != expected[i]:
				str += f'\'{DANGER}{delivered[i]}{RESET}\', '
			else:
				str += f'\'{delivered[i]}\', '
		str += ']\n'
		str = str.replace(', ]', ']')
		f.write(str)

		f.close()



	