from colorama import just_fix_windows_console
just_fix_windows_console()

from colorama import init
init()

from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')

print('\033[31m' + 'some red text')
print('\033[39m') # and reset to default color

from colorama import just_fix_windows_console
from termcolor import colored

print(colored('Hello, World!', 'green', 'on_red')

Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL

from colorama import init
init(autoreset=True)
print(Fore.RED + 'some red text')
print('automatically back to default color again')

import sys
from colorama import init, AnsiToWin32
init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream

# Python 2
print >>stream, Fore.BLUE + 'blue text on stderr'

# Python 3
print(Fore.BLUE + 'blue text on stderr', file=stream)

