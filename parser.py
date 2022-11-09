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
					os.system('norminette -R checkForbiddenSourceHeader ' + entry)
				elif entry.endswith('.h'):
					os.system('norminette -R checkDefine ' + entry)

			print()

	def parse_function_prototypes(self, dict):
		if input('Press ENTER to continue.') == '':
			os.system('clear')
			print_title('FUNCTION PROTOTYPES')

			c_files = list(filter(lambda x : x.startswith('ft_'), dict.keys()))
	
			res = {}
			for func in c_files:
				if func + '.c' in self.entries:
					res.update(dict[func].check_prototype())
				else:
					res.update({func : f'[{danger_color}FILE NOT DELIVERED{reset}]'})
		
			wrong_headers = list(filter(lambda x : x[1].find('MISMATCHING') or x[1].find('NOT FOUND'), res))
			num_wrong_headers = len(wrong_headers)

			for item in res.items():
				print(f'{item[0].ljust(20)}{item[1]}')
			if num_wrong_headers != 0:
				print_separator('FAILURE', '>', '<', danger_color)
			else:
				print_separator('SUCCESS', '>', '<', correct_color)
				print(f"All function headers are correct! \n")

	def print_files(self, dict, expected, color):	
		dict_list = list(dict.items())
		dict_list.sort()

		count = 0
		for item in dict_list:
			if item[1].wasDelivered == expected:
				print(f'\t{color}{item[0].ljust(20)}{reset}', end='')
				count += 1
				
				if count % 3 == 0:
					print()
		print('\n')

	def print_unknown_files(self, dict):
		print_title('UNKNOWN FILES')

		if len(dict) > 0:
			print(f"You have {danger_color}{len(list(dict.values()))}{reset} unknown file(s): \n")
			self.print_files(dict, True, danger_color)
			print_separator('FAILURE', '>', '<', danger_color)
			
			if input('Proceed anyway (y/n)? ') == 'n':
				exit(-1)
		else:
			print(f"No unknown files were found")
			print_separator('SUCCESS', '>', '<', correct_color)