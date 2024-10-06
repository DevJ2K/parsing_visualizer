from Colors import *
import os
from main import allow_to_expand

def highlight_str_i(string: str, index: int, color: str):
	if index > len(string):
		return
	c_string = ""
	for i in range(len(string)):
			if i == index:
				c_string += color + string[i] + RESET
			else:
				c_string += string[i]
	print(c_string)

def display_quotes_informations(is_open: bool, quote_type: str):
	print(f"{BHWHITE}Quote is open ? : {GREENHB + 'YES' if is_open else REDHB + 'NO'}{RESET}")
	if is_open:
		print(f"{BHWHITE}Quote type : {BHYELLOW}{quote_type}{RESET}")
	else:
		print(f"{BHWHITE}Quote type : {BLACKB} {RESET}")
	print(f"{BHWHITE}Expand is allow ? : {GREENHB + 'YES' if allow_to_expand(is_open, quote_type) else REDHB + 'NO'}{RESET}")

def display_str(string: str, index: int, return_str: str):
	print(f"{BHGREEN}RETURN  : {WHITEB}{return_str}{RESET}")
	print(f"{BHBLUE}CURRENT :{BHWHITE} ", end="")
	highlight_str_i(string, index, REDB)
	print(RESET)

def display_step(string: str, index: int, return_str: str, is_quote_open: bool, quote_type: str, str_i_color: str, display: bool = True):
	if display == False:
		return
	os.system("clear")
	display_quotes_informations(is_quote_open, quote_type)
	display_str(string, index, return_str)
	input("Press enter to continue...")
