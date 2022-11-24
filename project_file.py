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
		
		#Initializing the log file
		l = open(logfile, 'a')
		
		##
		line = f.readline()
		expected = tokenize(self.header)
		while line != '':
			line = line.replace('\n', '')

			delivered = tokenize(line)
			if len(delivered) == len(expected):
				if delivered[1] == expected[1]:
					f.close()
					if delivered != expected:
						l.write(f'In {WARNING}{self.func}.c{RESET}:\n')
						self.log(logfile, self.func + '.c',expected, delivered)
						return {delivered[1] : f'[{WARNING}MISMATCHING{RESET}]'}
					else:
						return {delivered[1] : f'[{CORRECT}CORRECT{RESET}]'}
			line = f.readline()
		
		self.log(logfile, expected, f'{DANGER}MISSING{RESET}')
		f.close()
		l.close()
		return {f'{self.func}.c : {self.header}' : f'[{DANGER}MISSING{RESET}]'}

	def find_header_prototypes(self, full_dict) -> dict:
		headers_result = {}
		possible_headers = {}

		#Building the expected results for each prototype
		for func_name, file in full_dict.items():
			if func_name.startswith('ft_'):
				expected = tokenize(file.header.strip('\n'))
				possible_headers.update({func_name.replace('.c', '') : expected})

		#Initializing the log file
		l = open(logfile, 'a')
		l.write(f'In {WARNING}libft.h{RESET}:\n')
		
		#Parsing the libft.h file
		f = open(path + 'libft.h', 'r')
		line = f.readline()
		while line != '':
			# Tokenization of the current line
			delivered = tokenize(line.strip(';\n'))
			
			# If I found a prototype
			if line.endswith(');\n'):
				if delivered[1] in possible_headers.keys():
					if possible_headers[delivered[1]] != delivered:
						self.log(l, possible_headers[delivered[1]], delivered)
						headers_result.update({delivered[1] : f'[{FATAL}MISMATCHING{RESET}]'})
					else:
						headers_result.update({delivered[1] : f'[{CORRECT}CORRECT{RESET}]'})
					possible_headers.pop(delivered[1])
				else:
					self.log(l, possible_headers[delivered[1]], f'{WARNING}UNKNOWN{RESET}')
					headers_result.update({line.strip(';\n') : f'[{WARNING}UNKNOWN{RESET}]'})
			line = f.readline()


		 # Any header that wasn't removed from the dict, wasn't found
		for func in possible_headers.keys():
			self.log(l, possible_headers[func], f'{DANGER}MISSING{RESET}')
			headers_result.update({full_dict[func + '.c'].header : f'[{DANGER}MISSING{RESET}]'})
		
		f.close()
		l.close()
		return headers_result

	def log(self, l, expected, delivered):
		if type(delivered) == str:
			l.write(f'\tExpected: {str(expected)}\n')
			l.write(f'\tDelivered: [{delivered}]\n\n')
			return
		
		string = '\tExpected: ['
		for i in range(len(expected)):
			if i >= len(delivered):
				string += f'\'{CORRECT}{expected[i]}{RESET}\', '
			elif delivered[i] != expected[i]:
				string += f'\'{CORRECT}{expected[i]}{RESET}\', '
			else:
				string += f'\'{expected[i]}\', '
		string += ']\n'
		string = string.replace(', ]', ']')
		l.write(string)

		string = '\tDelivered: ['
		for i in range(len(delivered)):
			if i >= len(expected):
				string += f'\'{DANGER}{delivered[i]}{RESET}\', '
			elif delivered[i] != expected[i]:
				string += f'\'{DANGER}{delivered[i]}{RESET}\', '
			else:
				string += f'\'{delivered[i]}\', '
		string += ']\n\n'
		string = string.replace(', ]', ']')
		l.write(string)


	