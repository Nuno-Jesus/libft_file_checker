from project_file import ProjectFile

part1_files = {
	'ft_memset.c' 	: ProjectFile('ft_memset', 'void\t*ft_memset(void *s, int c, size_t n)', []),
	'ft_bzero.c' 	: ProjectFile('ft_bzero' , 'void\tft_bzero(void *s, size_t n)', []),
	'ft_memcpy.c' 	: ProjectFile('ft_memcpy', 'void\t*ft_memcpy(void *dest, const void *src, size_t n)', []),
	'ft_memmove.c' 	: ProjectFile('ft_memmove', 'void\t*ft_memmove(void *dest, const void *src, size_t n)', []),
	'ft_memchr.c' 	: ProjectFile('ft_memchr', 'void\t*ft_memchr(const void *s, int c, size_t n)', []),
	'ft_memcmp.c' 	: ProjectFile('ft_memcmp', 'int\tft_memcmp(const void *s1, const void *s2, size_t n)', []),
	'ft_strlen.c' 	: ProjectFile('ft_strlen', 'size_t\tft_strlen(const char *s)', []),
	'ft_strlcpy.c' 	: ProjectFile('ft_strlcpy', 'size_t\tft_strlcpy(char *dst, const char *src, size_t size)', []),
	'ft_strlcat.c' 	: ProjectFile('ft_strlcat', 'size_t\tft_strlcat(char *dst, const char *src, size_t size)', []),
	'ft_strchr.c' 	: ProjectFile('ft_strchr', 'char\t*ft_strchr(const char *s, int c)', []),
	'ft_strrchr.c' 	: ProjectFile('ft_strrchr', 'char\t*ft_strrchr(const char *s, int c)', []),
	'ft_strnstr.c' 	: ProjectFile('ft_strnstr', 'char\t*ft_strnstr(const char *big, const char *little, size_t len)', []),
	'ft_strncmp.c' 	: ProjectFile('ft_strncmp', 'int\tft_strncmp(const char *s1, const char *s2, size_t n)', []),
	'ft_atoi.c' 	: ProjectFile('ft_atoi' ,  'int\tft_atoi(const char *nptr)', []),
	'ft_isalpha.c' 	: ProjectFile('ft_isalpha', 'int\tft_isalpha(int c)', []),
	'ft_isdigit.c' 	: ProjectFile('ft_isdigit', 'int\tft_isdigit(int c)', []),
	'ft_isalnum.c' 	: ProjectFile('ft_isalnum', 'int\tft_isalnum(int c)', []),
	'ft_isascii.c' 	: ProjectFile('ft_isascii', 'int\tft_isascii(int c)', []),
	'ft_isprint.c' 	: ProjectFile('ft_isprint', 'int\tft_isprint(int c)', []),
	'ft_toupper.c' 	: ProjectFile('ft_toupper', 'int\tft_toupper(int c)', []),
	'ft_tolower.c' 	: ProjectFile('ft_tolower', 'int\tft_tolower(int c)', []),
	'ft_calloc.c' 	: ProjectFile('ft_calloc', 'void\t*ft_calloc(size_t nmemb, size_t size)', []),
	'ft_strdup.c' 	: ProjectFile('ft_strdup', 'char\t*ft_strdup(const char *s)', []),
	'Makefile' 		: ProjectFile('Makefile', None, None),
	'libft.h' 		: ProjectFile('libft.h', None, None),
	'.git'			: ProjectFile('.git', None, None)
}

part2_files = {
	'ft_substr.c'		: ProjectFile('ft_substr', 'char\t*ft_substr(char const *s, unsigned int start, size_t len)', ['malloc']),
	'ft_strjoin.c'		: ProjectFile('ft_strjoin', 'char\t*ft_strjoin(char const *s1, char const *s2)', ['malloc']),
	'ft_strtrim.c'		: ProjectFile('ft_strtrim', 'char\t*ft_strtrim(char const *s1, char const *set)', ['malloc']),
	'ft_split.c'		: ProjectFile('ft_split', 'char\t**ft_split(char const *s, char c)', ['malloc', 'free']),
	'ft_itoa.c'			: ProjectFile('ft_itoa', 'char\t*ft_itoa(int n)', ['malloc']),
	'ft_strmapi.c'		: ProjectFile('ft_strmapi', 'char\t*ft_strmapi(char const *s, char (*f)(unsigned int, char))', ['malloc']),
	'ft_striteri.c'		: ProjectFile('ft_striteri', 'void\tft_striteri(char *s, void (*f)(unsigned int, char *))', None),
	'ft_putchar_fd.c'	: ProjectFile('ft_putchar_fd', 'void\tft_putchar_fd(char c, int fd)', ['write']),
	'ft_putstr_fd.c'	: ProjectFile('ft_putstr_fd', 'void\tft_putstr_fd(char *s, int fd)', ['write']),
	'ft_putendl_fd.c'	: ProjectFile('ft_putendl_fd', 'void\tft_putendl_fd(char *s, int fd)', ['write']),
	'ft_putnbr_fd.c'	: ProjectFile('ft_putnbr_fd', 'void\tft_putnbr_fd(int n, int fd)', ['write'])
}

bonus_files = {
	'ft_lstnew.c' 		: ProjectFile('ft_lstnew', 't_list\t*ft_lstnew(void *content)', ['malloc']),
	'ft_lstadd_front.c' : ProjectFile('ft_lstadd_front', 'void\tft_lstadd_front(t_list **lst, t_list *new)', None),
	'ft_lstsize.c' 		: ProjectFile('ft_lstsize', 'int\tft_lstsize(t_list *lst)', None),
	'ft_lstlast.c' 		: ProjectFile('ft_lstlast', 't_list\t*ft_lstlast(t_list *lst)', None),
	'ft_lstadd_back.c' 	: ProjectFile('ft_lstadd_back', 'void\tft_lstadd_back(t_list **lst, t_list *new)', None),
	'ft_lstdelone.c' 	: ProjectFile('ft_lstdelone', 'void\tft_lstdelone(t_list *lst, void (*del)(void*))', ['free']),
	'ft_lstclear.c' 	: ProjectFile('ft_lstclear', 'void\tft_lstclear(t_list **lst, void (*del)(void*))', ['free']),
	'ft_lstiter.c' 		: ProjectFile('ft_lstiter', 'void\tft_lstiter(t_list *lst, void (*f)(void*))', None),
	'ft_lstmap.c' 		: ProjectFile('ft_lstmap', 't_list\t*ft_lstmap(t_list *lst, void *(*f)(void*), void (*del)(void*))', ['malloc', 'free'])
}
""" 
strs = list(map(lambda x : x[1].header, bonus_files.items()))

for str in strs:
	print(str)

	str = str.replace("\t", " ")
	str = str.replace(" **", "** ")
	str = str.replace(" *", "* ")
	str = str.replace("(", " ")
	str = str.replace(")", " ")
	str = str.replace(" ,", ",")

	res = str.split(' ')
	res = list(filter(lambda x : x != '', res))

	if res == ['t_list*', 'ft_lstmap', 't_list*', 'lst,', 'void*', '*f', 'void*,', 'void', '*del', 'void*']:
		print(res)

 """
str = "t_list	*ft_lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *))"
str = str.replace("\t", " ")
print(str)
str = str.replace(" **", "** ")
print(str)
str = str.replace(" *", "* ")
print(str)
str = str.replace("(", " ")
print(str)
str = str.replace("( ", "(")
print(str)
str = str.replace(" )", ")")
print(str)
str = str.replace(")", " ")
print(str)
str = str.replace(" ,", ",")
print(str)

res = str.split(' ')
res = list(filter(lambda x : x != '', res))

print(res)
