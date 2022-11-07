from colorama import Style
from colorama import Fore

def print_menu():
	print('\n')
	print(15*' ' + f'{Fore.LIGHTCYAN_EX}	       :::      ::::::::   ::::::::::: ::::::::::: ::::::::::: :::        {Style.RESET_ALL}')
	print(15*' ' + f'{Fore.LIGHTCYAN_EX}      :+:      :+:    :+:       :+:     :+:     :+: :+:     :+: :+:        {Style.RESET_ALL}')
	print(15*' ' + f'{Fore.LIGHTCYAN_EX}    +:+ +:+         +:+         :+:     :+:     :+: :+:     :+: :+:        {Style.RESET_ALL}')
	print(15*' ' + f'{Fore.LIGHTCYAN_EX}  +#+  +:+       +#+            +#+     +#+     +#+ +#+     +#+ +#+        {Style.RESET_ALL}')
	print(15*' ' + f'{Fore.LIGHTCYAN_EX}+#+#+#+#+#+   +#+               +#+     +#+     +#+ +#+     +#+ +#+        {Style.RESET_ALL}')
	print(15*' ' + f'{Fore.LIGHTCYAN_EX}     #+#    #+#                 #+#     #+#     #+# #+#     #+# #+#        {Style.RESET_ALL}')
	print(15*' ' + f'{Fore.LIGHTCYAN_EX}    ###   ########              ###     ########### ########### ###########{Style.RESET_ALL}')


def print_separator(title, c1, c2, color):
	print('\n\t' + 25*c1 + color + f' {title} ' + Style.RESET_ALL + 25*c2 + '\n')

def print_title(title):
	print(f'{Fore.LIGHTYELLOW_EX}{title}{Style.RESET_ALL}')