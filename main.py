from project_file import ProjectFile
from parser import Parser
from utils import *

#List the files in the current directory
entries = os.listdir(path)

# The following dictionaries map filenames to an object containing the necessary information about it
part1_files = {
	'ft_memset.c' 	: ProjectFile('ft_memset', 'void\t*ft_memset(void *s, int c, size_t n)', []),
	'ft_bzero.c' 		: ProjectFile('ft_bzero' , 'void\tft_bzero(void *s, size_t n)', []),
	'ft_memcpy.c' 	: ProjectFile('ft_memcpy', 'void\t*ft_memcpy(void *dest, const void *src, size_t n)', []),
	'ft_memmove.c' 	: ProjectFile('ft_memmove', 'void\t*ft_memmove(void *dest, const void *src, size_t n)', []),
	'ft_memchr.c' 	: ProjectFile('ft_memchr', 'void\t*ft_memchr(const void *s, int c, size_t n)', []),
	'ft_memcmp.c' 	: ProjectFile('ft_memcmp', 'int\tft_memcmp(const void *s1, const void *s2, size_t n)', []),
	'ft_strlen.c' 	: ProjectFile('ft_strlen', 'size_t\tft_strlen(char const *s)', []),
	'ft_strlcpy.c' 	: ProjectFile('ft_strlcpy', 'size_t\tft_strlcpy(char *dst, const char *src, size_t size)', []),
	'ft_strlcat.c' 	: ProjectFile('ft_strlcat', 'size_t\tft_strlcat(char *dst, const char *src, size_t size)', []),
	'ft_strchr.c' 	: ProjectFile('ft_strchr', 'char\t*ft_strchr(const char *s, int c)', []),
	'ft_strrchr.c' 	: ProjectFile('ft_strrchr', 'char\t*ft_strrchr(const char *s, int c)', []),
	'ft_strnstr.c' 	: ProjectFile('ft_strnstr', 'char\t*ft_strnstr(const char *big, const char *little, size_t len)', []),
	'ft_strncmp.c' 	: ProjectFile('ft_strncmp', 'int\tft_strncmp(const char *s1, const char *s2, size_t n)', []),
	'ft_atoi.c' 		: ProjectFile('ft_atoi' ,  'int\tft_atoi(const char *nptr)', []),
	'ft_isalpha.c' 	: ProjectFile('ft_isalpha', 'int\tft_isalpha(int c)', []),
	'ft_isdigit.c' 	: ProjectFile('ft_isdigit', 'int\tft_isdigit(int c)', []),
	'ft_isalnum.c' 	: ProjectFile('ft_isalnum', 'int\tft_isalnum(int c)', []),
	'ft_isascii.c' 	: ProjectFile('ft_isascii', 'int\tft_isascii(int c)', []),
	'ft_isprint.c' 	: ProjectFile('ft_isprint', 'int\tft_isprint(int c)', []),
	'ft_toupper.c' 	: ProjectFile('ft_toupper', 'int\tft_toupper(int c)', []),
	'ft_tolower.c' 	: ProjectFile('ft_tolower', 'int\tft_tolower(int c)', []),
	'ft_calloc.c' 	: ProjectFile('ft_calloc', 'void\t*ft_calloc(size_t nmemb, size_t size)', []),
	'ft_strdup.c' 	: ProjectFile('ft_strdup', 'char\t*ft_strdup(const char *s)', []),
	'Makefile' 		: ProjectFile('Makefile' , None, None),
	'libft.h' 		: ProjectFile('libft.h' , None, None),
	'.git'			: ProjectFile('.git', None, None)
}

part2_files = {
	'ft_substr.c'		: ProjectFile('ft_substr', 'char\t*ft_substr(char const *s, unsigned int start, size_t len)', ['malloc']),
	'ft_strjoin.c'	: ProjectFile('ft_strjoin', 'char\t*ft_strjoin(char const *s1, char const *s2)', ['malloc']),
	'ft_strtrim.c'	: ProjectFile('ft_strtrim', 'char\t*ft_strtrim(char const *s1, char const *set)', ['malloc']),
	'ft_split.c'		: ProjectFile('ft_split' , 'char\t**ft_split(char const *s, char c)', ['malloc', 'free']),
	'ft_itoa.c'		: ProjectFile('ft_itoa' , 'char\t*ft_itoa(int n)', ['malloc']),
	'ft_strmapi.c'	: ProjectFile('ft_strmapi', 'char\t*ft_strmapi(char const *s, char (*f)(unsigned int, char))', ['malloc']),
	'ft_striteri.c'	: ProjectFile('ft_striteri', 'void\tft_striteri(char *s, void (*f)(unsigned int, char *))', None),
	'ft_putchar_fd.c'	: ProjectFile('ft_putchar_fd', 'void\tft_putchar_fd(char c, int fd)', ['write']),
	'ft_putstr_fd.c'	: ProjectFile('ft_putstr_fd', 'void\tft_putstr_fd(char *s, int fd)', ['write']),
	'ft_putendl_fd.c'	: ProjectFile('ft_putendl_fd', 'void\tft_putendl_fd(char *s, int fd)', ['write']),
	'ft_putnbr_fd.c'	: ProjectFile('ft_putnbr_fd', 'void\tft_putnbr_fd(int n, int fd)', ['write'])
}

bonus_files = {
	'ft_lstnew.c' 		: ProjectFile('ft_lstnew' , 't_list\t*ft_lstnew(void *content)', ['malloc']),
	'ft_lstadd_front.c' 	: ProjectFile('ft_lstadd_front', 'void\tft_lstadd_front(t_list **lst, t_list *new)', None),
	'ft_lstsize.c' 		: ProjectFile('ft_lstsize' , 'int\tft_lstsize(t_list *lst)', None),
	'ft_lstlast.c' 		: ProjectFile('ft_lstlast' , 't_list\t*ft_lstlast(t_list *lst)', None),
	'ft_lstadd_back.c' 	: ProjectFile('ft_lstadd_back', 'void\tft_lstadd_back(t_list **lst, t_list *new)', None),
	'ft_lstdelone.c' 		: ProjectFile('ft_lstdelone' , 'void\tft_lstdelone(t_list *lst, void (*del)(void *))', ['free']),
	'ft_lstclear.c' 		: ProjectFile('ft_lstclear' , 'void\tft_lstclear(t_list **lst, void (*del)(void *))', ['free']),
	'ft_lstiter.c' 		: ProjectFile('ft_lstiter' , 'void\tft_lstiter(t_list *lst, void (*f)(void *))', None),
	'ft_lstmap.c' 		: ProjectFile('ft_lstmap' , 't_list\t*ft_lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *))', ['malloc', 'free'])
}

# Dictionary to be filled with extra files found when parsing
unknown_files = {}

# Flips the boolean value in each entry of the dictionary if the file is found
def read_delivered_files():
	entries.sort()

	for entry in entries:
		if part1_files.get(entry):
			part1_files[entry].wasDelivered = True
		elif part2_files.get(entry):
			part2_files[entry].wasDelivered = True
		elif bonus_files.get(entry):
			bonus_files[entry].wasDelivered = True
		else:
			unknown_files[entry] = ProjectFile(entry, None, None)
			unknown_files[entry].wasDelivered = True

if __name__ == '__main__':
	print_menu()

	# Merges all 3 dictionaries into a new one to be easily used on prototype parsing
	full_dict = copy.deepcopy(part1_files)
	full_dict.update(part2_files)
	full_dict.update(bonus_files)

	read_delivered_files()
	parser = Parser(entries, True)

	option = input('Choose your option: ')
	if option == '1':
		parser.parse_unknown_files(unknown_files)
	elif option == '2':
		parser.parse_filenames(part1_files, 'PART I')
		parser.parse_filenames(part2_files, 'PART II')
	elif option == '3':
		parser.parse_filenames(bonus_files, 'BONUS PART')
	elif option == '4':
		parser.parse_norminette_result()
	elif option == '5':
		parser.parse_function_prototypes(full_dict)
	elif option == '6':
		pass	
	elif option == '7':
		parser.parse_unknown_files(unknown_files)
		parser.parse_filenames(part1_files, 'PART I')
		parser.parse_filenames(part2_files, 'PART II')
		parser.parse_filenames(bonus_files, 'BONUS PART')
		parser.parse_norminette_result()
		parser.parse_function_prototypes(full_dict)

	
	
	