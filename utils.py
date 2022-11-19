import os
import re
import copy
import random
import subprocess

from colorama import Style
from colorama import Fore

# INSERT YOUR PATH HERE, INSIDE QUOTES
path = '../libft/'

# Used colors across the files
RESET = Style.RESET_ALL
DANGER = Fore.LIGHTRED_EX
WARNING = Fore.LIGHTYELLOW_EX
FATAL = Fore.LIGHTBLUE_EX
CORRECT = Fore.LIGHTGREEN_EX
MAIN_MENU_COLOR = WARNING
COLORS = [MAIN_MENU_COLOR, Fore.LIGHTGREEN_EX]

# This is used to easily print the right string on the given option
menu_options = {
	'1' : 'Check for forbidden files',
	'2' : 'Check filenames for Mandatory Part',
	'3' : 'Check filenames for Bonus Part',
	'4' : 'Run the norminette',
	'5' : 'Look for incorrect function prototypes in \'.c\' files',
	'6' : 'Look for incorrect function prototypes in \'libft.h\'',
	'7' : 'Full run (1 - 6)',
}

char_map = {
	'#' : MAIN_MENU_COLOR,
	'+' : Fore.LIGHTCYAN_EX,
	':' : Fore.LIGHTWHITE_EX,
	' ' : Fore.WHITE,
	'\t' : Fore.WHITE,
	'\n' : Fore.WHITE
}

def tokenize(str):
	str = re.sub('\t+', ' ', str)
	str = str.replace(' **', '** ')
	str = str.replace(' *', '* ')
	str = str.replace('( ', '(')
	str = str.replace(' )', ')')
	str = str.replace('(', ' ')
	str = str.replace(')', ' ')
	str = str.replace(' ,', ',')
	
	res = str.split(' ')
	res = list(filter(lambda x : x != '', res))

	return res

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
		print(f'{char_map[char]}{char}{RESET}', end = '')
	print()

	for option in menu_options.items():
		print(f'\t[{MAIN_MENU_COLOR}{option[0]}{RESET}] - {option[1]}')
	print()

def print_separator(title, c1, c2, color):
	print('\n\t' + 25*c1 + color + f' {title} ' + RESET + 25*c2 + '\n')

def print_title(title):
	print(f'{Fore.LIGHTYELLOW_EX}{title}{RESET}')
