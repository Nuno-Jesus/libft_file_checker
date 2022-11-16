import os
from colorama import Style
from colorama import Fore
from utils import *

class Parser:
	def __init__(self, entries, override) -> None:
		self.entries = entries
		self.override = override
		
	def parse_unknown_files(self, dict):
		if input('Press ENTER to continue.') == '':
			os.system('clear')
			print_title('UNKNOWN FILES')
			
			if len(dict) > 0:
				print(f"You have {danger_color}{len(list(dict.values()))}{reset} unknown file(s): \n")
				self.print_files(dict, True, danger_color)
				print_separator('FAILURE', '>', '<', danger_color)
			else:
				print(f"No unknown files were found")
				print_separator('SUCCESS', '>', '<', correct_color)

	def parse_filenames(self, dict, title):
		if input('Press ENTER to continue.') == '':
			os.system('clear')
			print_title(title)
			
			num_total = len(list(dict.keys()))
			num_correct = str(len(list(filter(lambda x : x.wasDelivered == True, dict.values()))))
			num_missing = str(len(list(filter(lambda x : x.wasDelivered == False, dict.values()))))

			if int(num_correct) > 0:
				print(f'Correct files: {correct_color}{num_correct}{reset}\n')
				self.print_files(dict, True, correct_color)
				
				if int(num_correct) == int(num_total):
					print_separator('SUCCESS', '>', '<', correct_color)
					return

			print(f'Missing files: {danger_color}{num_missing}{reset}\n')
			self.print_files(dict, False, Fore.LIGHTRED_EX)
			print_separator('FAILURE', '>', '<', danger_color)

	def parse_norminette_result(self):
		if input('Press ENTER to continue.') == '':
			os.system('clear')
			print_title('NORMINETTE')
			
			for entry in self.entries:
				if entry.endswith('.c'):
					os.system(f'norminette -R checkForbiddenSourceHeader {path}{entry}')
				elif entry.endswith('.h'):
					os.system(f'norminette -R checkDefine {path}{entry}')

			print()

	def parse_function_prototypes(self, dict):
		if input('Press ENTER to continue.') == '':
			os.system('clear')
			print_title('C FILES FUNCTION PROTOTYPES')

			c_files = list(filter(lambda x : x.startswith('ft_'), dict.keys()))
	
			results = {}
			for file in c_files:
				if file in self.entries:
					results.update(dict[file].find_prototype())
				else:
					results.update({file : f'[{danger_color}FILE NOT DELIVERED{reset}]'})

			num_correct = len(list(filter(lambda x : x[1].find('CORRECT') != -1, results.items())))
			num_wrong = len(list(filter(lambda x : x[1].find('NOT FOUND') != -1, results.items())))
			num_not_delivered = len(list(filter(lambda x : x[1].find('FILE NOT DELIVERED') != -1, results.items())))

			print(f'You have {correct_color}{num_correct}{reset} files with the correct prototype, ' 
			f'{danger_color}{num_wrong}{reset} files with a mismatching/not found prototype and '
			f'{warning_color}{num_not_delivered}{reset} non-delivered files.\n')
			

			for (file, result) in results.items():
				print(f'{result.ljust(30)}{file}')
			if num_wrong != 0:
				print_separator('FAILURE', '>', '<', danger_color)
			else:
				print_separator('SUCCESS', '>', '<', correct_color)

	def parse_headerfile_prototypes(self, full_dict):
		if input('Press ENTER to continue.') == '':
			os.system('clear')
			print_title('LIBFT.H FUNCTION PROTOTYPES')
			
			if 'libft.h' not in self.entries:
				print(f'libft.h\t\t[{danger_color}FILE NOT DELIVERED{reset}]')
				return

			headers_result = full_dict['libft.h'].find_header_prototypes(full_dict)
			
			# Print the overall results
			num_unknown = len(list(filter(lambda x : x[1].find('UNKNOWN') != -1, headers_result.items())))
			num_correct = len(list(filter(lambda x : x[1].find('CORRECT') != -1, headers_result.items())))
			num_wrong = len(list(filter(lambda x : x[1].find('NOT FOUND') != -1, headers_result.items())))
			
			print(f'Found {correct_color}{num_correct}{reset} correct prototypes, ' 
			f'{danger_color}{num_wrong}{reset} wrong prototypes and '
			f'{warning_color}{num_unknown}{reset} unknown prototypes.\n')

			for (header, res) in headers_result.items():
				print(res.ljust(20) + ' ' + header)

			if num_wrong != 0:
				print_separator('FAILURE', '>', '<', danger_color)
			else:
				print_separator('SUCCESS', '>', '<', correct_color)

	def print_files(self, dict, expected, color):	
		dict_list = list(dict.items())
		dict_list.sort()

		count = 0
		for (filename, info) in dict_list:
			if info.wasDelivered == expected:
				print(f'\t{color}{filename}{reset}', end='')
				count += 1
				
				if count % 3 == 0:
					print()
		print('\n')