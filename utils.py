import random
import os
import copy
import subprocess

from colorama import Style
from colorama import Fore

# Path to search for the files on (YES, YOU MAY CHANGE THIS)
path = '../42-cursus/libft/'

# Used colors across the files
reset = Style.RESET_ALL
danger_color = Fore.LIGHTRED_EX
warning_color = Fore.LIGHTYELLOW_EX
correct_color = Fore.LIGHTGREEN_EX
main_menu_color = Fore.LIGHTCYAN_EX
colors = [main_menu_color, Fore.LIGHTWHITE_EX]

# This is used to easily print the right string on the given option
menu_options = {
	'1' : 'Check for forbidden files',
	'2' : 'Check filenames for Mandatory Part',
	'3' : 'Check filenames for Bonus Part',
	'4' : 'Run the norminette',
	'5' : 'Look for incorrect function prototypes in \'.c\' files',
	'6' : 'Look for incorrect function prototypes in \'libft.h\'',
	'7' : 'Full run (1 - 7)',
}

def print_menu():
	menu_string = \
	'\t\t        :::      ::::::::   ::::::::::: ::::::::::: ::::::::::: :::        \n' + \
	'\t\t      :+:      :+:    :+:       :+:     :+:     :+: :+:     :+: :+:        \n' + \
	'\t\t    +:+ +:+         +:+         :+:     :+:     :+: :+:     :+: :+:        \n' + \
	'\t\t  +#+  +:+       +#+            +#+     +#+     +#+ +#+     +#+ +#+        \n' + \
	'\t\t+#+#+#+#+#+   +#+               +#+     +#+     +#+ +#+     +#+ +#+        \n' + \
	'\t\t     #+#    #+#                 #+#     #+#     #+# #+#     #+# #+#        \n' + \
	'\t\t    ###   ########              ###     ########### ########### ###########\n'

	os.system('clear')
	print()
	for char in menu_string:
		print(f'{colors[random.randint(0, len(colors) - 1)]}{char}{reset}', end = '')
	print()

	for option in menu_options.items():
		print(f'\t[{main_menu_color}{option[0]}{reset}] - {option[1]}')
	print()

def print_separator(title, c1, c2, color):
	print('\n\t' + 25*c1 + color + f' {title} ' + reset + 25*c2 + '\n')

def print_title(title):
	print(f'{Fore.LIGHTYELLOW_EX}{title}{reset}')