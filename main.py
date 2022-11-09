import os
import copy

from pip import main
from colorama import Fore
from colorama import Style
from setuptools import Require

from project_file import ProjectFile
from parser import Parser
from utils import *

#List the files in the current directory
entries = os.listdir()

# Overrides parser halting when an error pops up
override = True

part1_files = {
	'ft_memset' 	: ProjectFile('ft_memset', 'void\t*ft_memset(void *s, int c, size_t n)', []),
	'ft_bzero' 		: ProjectFile('ft_bzero' , 'void\tft_bzero(void *s, size_t n)', []),
	'ft_memcpy' 	: ProjectFile('ft_memcpy', 'void\t*ft_memcpy(void *dest, const void *src, size_t n)', []),
	'ft_memmove' 	: ProjectFile('ft_memmove', 'void\t*ft_memmove(void *dest, const void *src, size_t n)', []),
	'ft_memchr' 	: ProjectFile('ft_memchr', 'void\t*ft_memchr(const void *s, int c, size_t n)', []),
	'ft_memcmp' 	: ProjectFile('ft_memcmp', 'int\tft_memcmp(const void *s1, const void *s2, size_t n)', []),
	'ft_strlen' 	: ProjectFile('ft_strlen', 'size_t\tft_strlen(char const *s)', []),
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
	'libft.h' 		: ProjectFile('libft.h' , None, None),
	'.git'			: ProjectFile('.git', None, None)
}

part2_files = {
	'ft_substr'		: ProjectFile('ft_substr', 'char\t*ft_substr(char const *s, unsigned int start, size_t len)', ['malloc']),
	'ft_strjoin'	: ProjectFile('ft_strjoin', 'char\t*ft_strjoin(char const *s1, char const *s2)', ['malloc']),
	'ft_strtrim'	: ProjectFile('ft_strtrim', 'char\t*ft_strtrim(char const *s1, char const *set)', ['malloc']),
	'ft_split'		: ProjectFile('ft_split' , 'char\t**ft_split(char const *s, char c)', ['malloc', 'free']),
	'ft_itoa'		: ProjectFile('ft_itoa' , 'char\t*ft_itoa(int n)', ['malloc']),
	'ft_strmapi'	: ProjectFile('ft_strmapi', 'char\t*ft_strmapi(char const *s, char (*f)(unsigned int, char))', ['malloc']),
	'ft_striteri'	: ProjectFile('ft_striteri', 'void\tft_striteri(char *s, void (*f)(unsigned int, char *))', None),
	'ft_putchar_fd'	: ProjectFile('ft_putchar_fd', 'void\tft_putchar_fd(char c, int fd)', ['write']),
	'ft_putstr_fd'	: ProjectFile('ft_putstr_fd', 'void\tft_putstr_fd(char *s, int fd)', ['write']),
	'ft_putendl_fd'	: ProjectFile('ft_putendl_fd', 'void\tft_putendl_fd(char *s, int fd)', ['write']),
	'ft_putnbr_fd'	: ProjectFile('ft_putnbr_fd', 'void\tft_putnbr_fd(int n, int fd)', ['write'])
}

bonus_files = {
	'ft_lstnew' 		: ProjectFile('ft_lstnew' , 't_list\t*ft_lstnew(void *content)', ['malloc']),
	'ft_lstadd_front' : ProjectFile('ft_lstadd_front', 'void\tft_lstadd_front(t_list **lst, t_list *new)', None),
	'ft_lstsize' 		: ProjectFile('ft_lstsize' , 'int\tft_lstsize(t_list *lst)', None),
	'ft_lstlast' 		: ProjectFile('ft_lstlast' , 't_list\t*ft_lstlast(t_list *lst)', None),
	'ft_lstadd_back' 	: ProjectFile('ft_lstadd_back', 'void\tft_lstadd_back(t_list **lst, t_list *new)', None),
	'ft_lstdelone' 	: ProjectFile('ft_lstdelone' , 'void\tft_lstdelone(t_list *lst, void (*del)(void *))', ['free']),
	'ft_lstclear' 	: ProjectFile('ft_lstclear' , 'void\tft_lstclear(t_list **lst, void (*del)(void *))', ['free']),
	'ft_lstiter' 		: ProjectFile('ft_lstiter' , 'void\tft_lstiter(t_list *lst, void (*f)(void *))', None),
	'ft_lstmap' 		: ProjectFile('ft_lstmap' , 't_list\t*ft_lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *))', ['malloc', 'free'])
}

unknown_files = {}
parser_files = ['parser.py', 'project_file.py', 'test.py', 'utils.py', 'main.py']

def read_delivered_files():
	for entry in entries:
		filename = entry.replace('.c', '')

		if filename in parser_files:
			continue
		elif part1_files.get(filename):
			part1_files[filename].wasDelivered = True
		elif part2_files.get(filename):
			part2_files[filename].wasDelivered = True
		elif bonus_files.get(filename):
			bonus_files[filename].wasDelivered = True
		else:
			unknown_files[entry] = ProjectFile(filename, None, None)
			unknown_files[entry].wasDelivered = True

if __name__ == '__main__':
	os.system('clear')
	print_menu()
	print_options()

	full_dict = copy.deepcopy(part1_files)
	full_dict.update(part2_files)
	full_dict.update(bonus_files)

	read_delivered_files()
	parser = Parser(entries, True)

	option = input('Choose your option: ')
	if option == '1':
		parser.parse_unknown_files(unknown_files)
		parser.parse_filenames(part1_files, 'PART I')
		parser.parse_filenames(part2_files, 'PART II')
		parser.parse_filenames(bonus_files, 'BONUS PART')
		parser.parse_norminette_result()
		parser.parse_function_prototypes(full_dict)
	elif option == '2':
		parser.parse_unknown_files(unknown_files)
	elif option == '3':
		parser.parse_filenames(part1_files, 'PART I')
		parser.parse_filenames(part2_files, 'PART II')
	elif option == '4':
		parser.parse_norminette_result()
	elif option == '5':
		parser.parse_function_prototypes(full_dict)


	
	
	