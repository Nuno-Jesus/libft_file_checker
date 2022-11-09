from colorama import Style
from colorama import Fore
import random

menu_options = {
	'1' : 'Check for forbidden files',
	'2' : 'Check filenames for Mandatory Part',
	'3' : 'Check filenames for Bonus Part',
	'4' : 'Run the norminette in every file',
	'5' : 'Check incorrect function prototypes in .c files',
	'6' : 'Check incorrect function prototypes in libft.h',
	'7' : 'Full run (1 - 6)',
}

wrong_color = Fore.LIGHTRED_EX
correct_color = Fore.LIGHTGREEN_EX
main_menu_color = Fore.LIGHTCYAN_EX
colors = [main_menu_color, Fore.LIGHTWHITE_EX]

def print_menu():
	menu_string = \
	'\t\t        :::      ::::::::   ::::::::::: ::::::::::: ::::::::::: :::        \n' + \
	'\t\t      :+:      :+:    :+:       :+:     :+:     :+: :+:     :+: :+:        \n' + \
	'\t\t    +:+ +:+         +:+         :+:     :+:     :+: :+:     :+: :+:        \n' + \
	'\t\t  +#+  +:+       +#+            +#+     +#+     +#+ +#+     +#+ +#+        \n' + \
	'\t\t+#+#+#+#+#+   +#+               +#+     +#+     +#+ +#+     +#+ +#+        \n' + \
	'\t\t     #+#    #+#                 #+#     #+#     #+# #+#     #+# #+#        \n' + \
	'\t\t    ###   ########              ###     ########### ########### ###########\n'

	print()
	for char in menu_string:
		print(f'{colors[random.randint(0, len(colors) - 1)]}{char}{Style.RESET_ALL}', end = '')
	print()

def print_options():
	for option in menu_options.items():
		print(f'\t[{main_menu_color}{option[0]}{Style.RESET_ALL}] - {option[1]}')
	print()

def print_separator(title, c1, c2, color):
	print('\n\t' + 25*c1 + color + f' {title} ' + Style.RESET_ALL + 25*c2 + '\n')

def print_title(title):
	print(f'{Fore.LIGHTYELLOW_EX}{title}{Style.RESET_ALL}')