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
				print(f"You have {wrong_color}{len(list(dict.values()))}{Style.RESET_ALL} unknown file(s): \n")
				self.print_files(dict, True, wrong_color)
				print_separator('FAILURE', '>', '<', wrong_color)
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
				print(f'Correct files: {correct_color}{num_correct}{Style.RESET_ALL}\n')
				self.print_files(dict, True, correct_color)
				
				if int(num_correct) == int(num_total):
					print_separator('SUCCESS', '>', '<', correct_color)
					return

			print(f'Missing files: {wrong_color}{num_missing}{Style.RESET_ALL}\n')
			self.print_files(dict, False, Fore.LIGHTRED_EX)
			print_separator('FAILURE', '>', '<', wrong_color)

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

			wrong_headers = []
			for func in list(filter(lambda x : x.find("ft_") != -1, dict.keys())):
				if func + '.c' in self.entries:
					wrong_headers.append(dict[func].check_header())
				else:
					print(f'Cannot parse {wrong_color}{func}' + f'.c{Style.RESET_ALL} file since it doesn\'t exist')
			
			wrong_headers = list(filter(lambda x : x != '', wrong_headers))
			num_wrong_headers = len(wrong_headers)

			if num_wrong_headers != 0:
				print(f"There are {wrong_color}{num_wrong_headers}{Style.RESET_ALL} wrong headers: \n")
				for func in wrong_headers:
					print(f'\t-> {wrong_color}{func}{Style.RESET_ALL}')
				print_separator('FAILURE', '>', '<', wrong_color)
			else:
				print(f"All function headers are correct! \n")
				print_separator('SUCCESS', '>', '<', correct_color)

	def print_files(self, dict, expected, color):	
		dict_list = list(dict.items())
		dict_list.sort()

		count = 0
		for item in dict_list:
			if item[1].wasDelivered == expected:
				print(f'\t{color}{item[0].ljust(20)}{Style.RESET_ALL}', end='')
				count += 1
				
				if count % 3 == 0:
					print()
		print('\n')

	def print_unknown_files(self, dict):
		print_title('UNKNOWN FILES')

		if len(dict) > 0:
			print(f"You have {wrong_color}{len(list(dict.values()))}{Style.RESET_ALL} unknown file(s): \n")
			self.print_files(dict, True, wrong_color)
			print_separator('FAILURE', '>', '<', wrong_color)
			
			if input('Proceed anyway (y/n)? ') == 'n':
				exit(-1)
		else:
			print(f"No unknown files were found")
			print_separator('SUCCESS', '>', '<', correct_color)