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
				print(f"You have {Fore.RED}{len(list(dict.values()))}{Style.RESET_ALL} unknown file(s): \n")
				self.print_files(dict, True, Fore.RED)
				print_separator('FAILURE', '>', '<', Fore.RED)
				
				if input('Proceed anyway (y/n)? ') == 'n':
					exit(-1)
			else:
				print(f"No unknown files were found")
				print_separator('SUCCESS', '>', '<', Fore.GREEN)

	def parse_filenames(self, dict, title):
		if input('Press ENTER to continue.') == '':
			os.system('clear')
			print_title(title)
			
			num_total = len(list(dict.keys()))
			num_correct = str(len(list(filter(lambda x : x.wasDelivered == True, dict.values()))))
			num_missing = str(len(list(filter(lambda x : x.wasDelivered == False, dict.values()))))

			print(f'Correct files: {Fore.GREEN}{num_correct}{Style.RESET_ALL}\n')

			if int(num_correct) > 0:
				self.print_files(dict, True, Fore.LIGHTGREEN_EX)
				
				if int(num_correct) == int(num_total):
					print_separator('SUCCESS', '>', '<', Fore.GREEN)
					return

			print(f'Missing files: {Fore.RED}{num_missing}{Style.RESET_ALL}\n')
			self.print_files(dict, False, Fore.LIGHTRED_EX)
			print_separator('FAILURE', '>', '<', Fore.RED)
			if not self.override:
				exit(-1)

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
				wrong_headers.append(dict[func].check_header())
			
			wrong_headers = list(filter(lambda x : x != '', wrong_headers))
			num_wrong_headers = len(wrong_headers)

			if num_wrong_headers != 0:
				print(f"There are {Fore.RED}{num_wrong_headers}{Style.RESET_ALL} wrong headers: \n")
				for func in wrong_headers:
					print(f'\t-> {Fore.RED}{func}{Style.RESET_ALL}')
				print_separator('FAILURE', '>', '<', Fore.RED)
			else:
				print(f"All function headers are correct! \n")
				print_separator('SUCCESS', '>', '<', Fore.GREEN)

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
			print(f"You have {Fore.RED}{len(list(dict.values()))}{Style.RESET_ALL} unknown file(s): \n")
			self.print_files(dict, True, Fore.RED)
			print_separator('FAILURE', '>', '<', Fore.RED)
			
			if input('Proceed anyway (y/n)? ') == 'n':
				exit(-1)
		else:
			print(f"No unknown files were found")
			print_separator('SUCCESS', '>', '<', Fore.GREEN)