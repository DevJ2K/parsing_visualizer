from Colors import *

def highlight_str_i(string: str, index: int, color: str):
	if index > len(str):
		return
	c_string = ""
	for i in range(len(string)):
			if i == index:
				c_string += color + string[i] + RESET
			else:
				c_string += string[i]
	print(c_string)

def display_quotes_informations(is_open: bool, quote_type: str):
	print(f"Quote is open ? : {GREENHB + 'YES' if is_open else REDHB + 'NO'}{RESET}")
	if is_open:
		print(f"{BHWHITE}Quote type : {BHYELLOW}{quote_type}{RESET}")
	else:
		print(f"{BHWHITE}Quote type : {BLACKB} {RESET}")

def display_str(string: str, index: int, return_str: str):
	print(f"{BHGREEN}RETURN  : {WHITEB}{return_str}{RESET}")
	print(f"{BHBLUE}CURRENT :{BHWHITE} ", end="")
	highlight_str_i(string, index, REDB)
	print(RESET)
