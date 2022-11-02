import os

from pip import main
from colorama import Fore
from colorama import Style
from setuptools import Require

from ProjectFile import ProjectFile

#List the files in the current directory
entries = os.listdir('P00')

# Overrides parser halting when an error pops up
override = True

part1_files = {
	'ft_memset' 	: ProjectFile('ft_memset', 'void\t*ft_memset(void *s, int c, size_t n)', []),
	'ft_bzero' 		: ProjectFile('ft_bzero' , 'void\tft_bzero(void *s, size_t n)', []),
	'ft_memcpy' 	: ProjectFile('ft_memcpy', 'void\t*ft_memcpy(void *dest, const void *src, size_t n)', []),
	'ft_memmove' 	: ProjectFile('ft_memmove', 'void\t*ft_memmove(void *dest, const void *src, size_t n)', []),
	'ft_memchr' 	: ProjectFile('ft_memchr', 'void\t*ft_memchr(const void *s, int c, size_t n)', []),
	'ft_memcmp' 	: ProjectFile('ft_memcmp', 'int\tft_memcmp(const void *s1, const void *s2, size_t n)', []),
	'ft_strlen' 	: ProjectFile('ft_strlen', 'size_t\tft_strlen(char const *str)', []),
	'ft_strlcpy' 	: ProjectFile('ft_strlcpy', 'size_t\tft_strlcpy(char *dst, const char *src, size_t size)', []),
	'ft_strlcat' 	: ProjectFile('ft_strlcat', 'size_t\tft_strlcat(char *dst, const char *src, size_t size)', []),
	'ft_strchr' 	: ProjectFile('ft_strchr', 'char\t*ft_strchr(const char *s, int c)', []),
	'ft_strrchr' 	: ProjectFile('ft_strrchr', 'char\t*ft_strrchr(const char *s, int c)', []),
	'ft_strnstr' 	: ProjectFile('ft_strnstr', 'char\t*ft_strnstr(const char *big, const char *little, size_t len)', []),
	'ft_strncmp' 	: ProjectFile('ft_strncmp', 'int\tft_strncmp(const char *s1, const char *s2, size_t n)', []),
	'ft_atoi' 		: ProjectFile('ft_atoi' ,  'int\tft_atoi(const char *nptr)', []),
	'ft_isalpha' 	: ProjectFile('ft_isalpha', 'int\tft_isalpha(int c)', []),
	'ft_isdigit' 	: ProjectFile('ft_isdigit', 'int\tft_isdigit(int c)', []),
	'ft_isalnum' 	: ProjectFile('ft_isalnum', 'int\tft_isalnum(int c)', []),
	'ft_isascii' 	: ProjectFile('ft_isascii', 'int\tft_isascii(int c)', []),
	'ft_isprint' 	: ProjectFile('ft_isprint', 'int\tft_isprint(int c)', []),
	'ft_toupper' 	: ProjectFile('ft_toupper', 'int\tft_toupper(int c)', []),
	'ft_tolower' 	: ProjectFile('ft_tolower', 'int\tft_tolower(int c)', []),
	'ft_calloc' 	: ProjectFile('ft_calloc', 'void\t*ft_calloc(size_t nmemb, size_t size)', []),
	'ft_strdup' 	: ProjectFile('ft_strdup', 'char\t*ft_strdup(const char *s)', []),
	'Makefile' 		: ProjectFile('Makefile' , None, None),
	'libft.h' 		: ProjectFile('libft.h' , None, None)
}

part2_files = {
	'ft_substr'		: ProjectFile('ft_substr', 'char\t*ft_substr(char const *s, unsigned int start, size_t len)', ['malloc']),
	'ft_strjoin'	: ProjectFile('ft_strjoin', 'char\t*ft_strjoin(char const *s1, char const *s2)', ['malloc']),
	'ft_strtrim'	: ProjectFile('ft_strtrim', 'char\t*ft_strtrim(char const *s1, char const *set)', ['malloc']),
	'ft_split'		: ProjectFile('ft_split' , 'char\t**ft_split(char const *s, char c)', ['malloc', 'free']),
	'ft_itoa'		: ProjectFile('ft_itoa' , 'char\t*ft_itoa(int n)', ['malloc']),
	'ft_strmapi'	: ProjectFile('ft_strmapi', 'char\t*ft_strmapi(char const *s, char (*f)(unsigned int, char))', ['malloc']),
	'ft_striteri'	: ProjectFile('ft_striteri', 'void\tft_striteri(char *s, void (*f)(unsigned int, char*));', None),
	'ft_putchar_fd'	: ProjectFile('ft_putchar_fd', 'void\tft_putchar_fd(char c, int fd)', ['write']),
	'ft_putstr_fd'	: ProjectFile('ft_putstr_fd', 'void\tft_putstr_fd(char *s, int fd)', ['write']),
	'ft_putendl_fd'	: ProjectFile('ft_putendl_fd', 'void\tft_putendl_fd(char *s, int fd)', ['write']),
	'ft_putnbr_fd'	: ProjectFile('ft_putnbr_fd', 'void\tft_putnbr_fd(int n, int fd)', ['write'])
}

bonus_files = {
	'ft_lstnew_bonus' 		: ProjectFile('ft_lstnew' , 't_list\t*ft_lstnew(void *content)', ['malloc']),
	'ft_lstadd_front_bonus' : ProjectFile('ft_lstadd_front', 'void\tft_lstadd_front(t_list **lst, t_list *new)', None),
	'ft_lstsize_bonus' 		: ProjectFile('ft_lstsize' , 'int\tft_lstsize(t_list *lst)', None),
	'ft_lstlast_bonus' 		: ProjectFile('ft_lstlast' , 't_list\t*ft_lstlast(t_list *lst)', None),
	'ft_lstadd_back_bonus' 	: ProjectFile('ft_lstadd_back', 'void\tft_lstadd_back(t_list **lst, t_list *new)', None),
	'ft_lstdelone_bonus' 	: ProjectFile('ft_lstdelone' , 'void\tft_lstdelone(t_list *lst, void (*del)(void*))', ['free']),
	'ft_lstclear_bonus' 	: ProjectFile('ft_lstclear' , 'void\tft_lstclear(t_list **lst, void (*del)(void*))', ['free']),
	'ft_lstiter_bonus' 		: ProjectFile('ft_lstiter' , 'void\tft_lstiter(t_list *lst, void (*f)(void *))', None),
	'ft_lstmap_bonus' 		: ProjectFile('ft_lstmap' , 't_list\t*ft_lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *))', ['malloc', 'free'])
}

extra_files = {}
unknown_files = {}

def print_separator(title, c1, c2, color):
	print('\n\t' + 25*c1 + color + f' {title} ' + Style.RESET_ALL + 25*c2 + '\n')

def read_delivered_files():
	print(entries)
	for entry in entries:
		filename = entry.replace('.c', '')
		#print(part1_files.get(filename))

		if part1_files.get(filename):
			print("Entered this 1 with " + filename)
			part1_files[filename].wasDelivered = True
		elif part2_files.get(filename):
			print("Entered this 2 with " + filename)
			part2_files[filename].wasDelivered = True
		elif bonus_files.get(filename):
			print("Entered this 3 with " + filename)
			bonus_files[filename].wasDelivered = True
		elif filename.endswith('_bonus'):
			print("Entered this 4 with " + filename)
			extra_files[entry] = ProjectFile(filename.replace('_bonus', ''), None, None)
			extra_files[entry].wasDelivered = True
		else:
			print("Entered this 5 with " + filename)
			unknown_files[entry] = ProjectFile(filename, None, None)
			unknown_files[entry].wasDelivered = True

def print_files(dict, expected, color):
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

def parse_filenames(dict):
	num_total = len(list(dict.keys()))
	num_correct = str(len(list(map(lambda x : x.wasDelivered, dict.values()))))
	num_missing = str(len(list(map(lambda x : not x.wasDelivered, dict.values()))))

	print(f'Correct files: {Fore.GREEN}{num_correct}{Style.RESET_ALL}\n')

	if int(num_correct) > 0:
		print_files(dict, True, Fore.LIGHTGREEN_EX)
		
		if int(num_correct) == int(num_total):
			print_separator('SUCCESS', '>', '<', Fore.GREEN)
			return

	print(f'Missing files: {Fore.RED}{num_missing}{Style.RESET_ALL}\n')
	print_files(dict, False, Fore.LIGHTRED_EX)
	print_separator('FAILURE', '>', '<', Fore.RED)
	if not override:
		exit(-1)
	
def parse_headers():
	print(f'{Fore.LIGHTYELLOW_EX}HEADER CHECKING{Style.RESET_ALL}')

	wrong_headers = {}
	full_dict = part1_files
	full_dict.update(part2_files)
	full_dict.update(bonus_files)

	for func in list(filter(lambda x : x.find("ft_") != -1, full_dict.keys())):
		f = open(func + '.c', 'r')

		line = f.readline()
		while line != '':
			if line.find(func + '(') != -1:
				if line != full_dict[func][0] + '\n':
					wrong_headers[func] = (full_dict[func][0], line.replace('\n', ''))
				
				f.close()
				break  

			line = f.readline()

		#wrong_headers[func] = (full_dict[func][0], None)
	

	num_wrong_headers = len(list(wrong_headers.keys()))
	print(f"There are {num_wrong_headers} wrong headers. Please, carefully check the parser's result: \n")
	
	wrong_headers_list = list(wrong_headers.keys())
	if len(wrong_headers_list) != 0:
		for func in wrong_headers_list:
			print(f'\t{Fore.LIGHTCYAN_EX}Expected:{Style.RESET_ALL}\'{wrong_headers[func][0]}\'')
			print(f'\t{Fore.LIGHTRED_EX}Returned:{Style.RESET_ALL}\'{wrong_headers[func][1]}\'\n')
		print_separator('FAILURE', '>', '<', Fore.RED)
	else:
		print_separator('SUCCESS', '>', '<', Fore.GREEN)
	
'''
	1 - Parse filenames and check if those are correct
	2 - Next up, launch a shell command and grab any errors
	3 - Open each file and check for the corresponding header
	4 - Generate tests for each group of functions that can receive the same arguments
 '''

if __name__ == '__main__':
	os.system('clear')
	####################################### 1 #######################################
	read_delivered_files()

	if len(unknown_files) > 0:
		print(f'{Fore.LIGHTYELLOW_EX}UNKNOWN FILES{Style.RESET_ALL}')
		
		print(f"You have {Fore.RED}{len(list(unknown_files.values()))}{Style.RESET_ALL} unknown file(s): \n")
		print_files(unknown_files, True, Fore.RED)
		print_separator('FAILURE', '>', '<', Fore.RED)
		
		if input('Proceed anyway (y/n)? ') == 'n':
			exit(-1)

	if input('-> Press ENTER to continue.') == '':
		os.system('clear')
		print(f'{Fore.LIGHTYELLOW_EX}PART I{Style.RESET_ALL}')
		parse_filenames(part1_files)

	if input('-> Press ENTER to continue.') == '':
		os.system('clear')
		print(f'{Fore.LIGHTYELLOW_EX}PART II{Style.RESET_ALL}')
		parse_filenames(part2_files)

	response = input('Did you implement the bonus part (y/n)? ')
	if response.casefold()[0] == 'y':
		os.system('clear')
		print(f'{Fore.LIGHTYELLOW_EX}BONUS PART{Style.RESET_ALL}')
		parse_filenames(bonus_files)

	if len(extra_files) > 0:
		print(f'{Fore.LIGHTYELLOW_EX}EXTRA FILES{Style.RESET_ALL}')
		print('These files were also found:\n')
		print_files(extra_files, True, Fore.WHITE)

	####################################### 2 #######################################
	
	# TO BE IMPLEMENTED 
	
	####################################### 3 #######################################

	if input('-> Press ENTER to continue.') == '':
		os.system('clear')
		parse_headers()



	
	
	

	

