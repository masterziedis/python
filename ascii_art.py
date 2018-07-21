from pyfiglet import figlet_format
from termcolor import colored



msg = input("ka printint?")

ascii_art = figlet_format(msg)

print(ascii_art)
