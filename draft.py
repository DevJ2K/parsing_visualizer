from Colors import *
import os
import subprocess


def highlighted_str_i(str: str, index: int, color: str):
	if index > len(str):
		return
	string = ""
	for i in range(len(str)):
		if i == index:
			string += color + str[i] + RESET
		else:
			string += str[i]
	print(string)

def display_quotes_informations(is_open: bool, quote_type: str):
	print(f"Quote is open ? : {GREENHB + 'YES' if is_open else REDHB + 'NO'}{RESET}")
	if is_open:
		print(f"{BHWHITE}Quote type : {BHYELLOW}{quote_type}{RESET}")
	else:
		print(f"{BHWHITE}Quote type : {BLACKB} {RESET}")
		pass

def display_str(string: str, index: int, return_str: str):
	print(f"{BHGREEN}RETURN  : {WHITEB}{return_str}{RESET}")
	print(f"{BHBLUE}CURRENT :{BHWHITE} ", end="")
	highlighted_str_i(string, index, REDB)
	print(RESET)
	# input("(enter)...")


def exist_in_env(string: str) -> bool:
	return os.getenv(string) is not None

# Si j'ai ça '$USER.' la fonction à 'USER.'
def look_for_expand(string: str) -> str:
	i = 0
	if is_valid_expand(string[i]) == False:
		return "$"
	i = get_str_to_expand_size(string)

	str_to_find = string[:i]

	env_variable = os.getenv(str_to_find)
	# env_variable = os.getenv(str_to_find)

	# print(f"{string[:i]}: {env_variable}")
	if exist_in_env(str_to_find):
		return env_variable
	return None



def is_valid_expand(char: str) -> bool:
	return char.isalnum() or char == '_'

def get_str_to_expand_size(string: str) -> int:
	i = 0
	if is_valid_expand(string[i]) == False:
		# while i < len(string) and string[i + 1] == " ":
		# 	i += 1
		return 0

	while i < len(string) and is_valid_expand(string[i]):
		i += 1

	# if exist_in_env(string[:i]) == False:

	# while i < len(string) and string[i + 1] == " ":
	# 	i += 1
	return i

def allow_to_expand(is_quote_open: bool, quote_type: bool) -> bool:
	return (is_quote_open == True and quote_type == '\'') == False
	if is_quote_open:
		if quote_type == '"':
			return True
		return False
	return True

def skip_whitespace(string: str, is_quote_open: bool) -> int:
	i = 0
	if is_quote_open == True:
		return 1
	if i < len(string) and string[i] in [" ", "	"]:
		while i < len(string) and string[i] in [" ", "	"]:
			i += 1
		return i
	else:
		return 1

	# string[i] == " " and string[i + 1] == " " and string[i + 2] == " ":
	# 		while i + 1 < len(string) and string[i + 1] == " " and string[i + 2] == " ":
	# 			i += 1

def ft_strtrim_whitespace(string: str) -> str:
	return string.strip(" 	")


def main(initial_str: str):
	# print(initial_str)

	return_str = ""

	# display_quotes_informations(True, '"')
	# display_quotes_informations(True, '\'')
	# display_quotes_informations(False, '"')
	# display_str(string, 3, return_str)

	# display_str(string, 0, return_str)
	# input("(enter)...")

	is_quote_open = False
	quote_type = ""

	i = 0
	string = ft_strtrim_whitespace(initial_str)
	while i < len(string):
		# display_str(string, i, return_str)
		# input("(enter)...")
		# print(f"--{i}")
		if string[i] == '"' or string[i] == '\'':
			if is_quote_open == True and quote_type == string[i]:
				is_quote_open = False
			elif is_quote_open == False:
				is_quote_open = True
				quote_type = string[i]
			else:
				return_str += string[i]


		# elif string[i] == '\'':
		# 	if is_quote_open == True and quote_type == string[i]:
		# 		is_quote_open = False
		# 	elif is_quote_open == False:
		# 		is_quote_open = True
		# 		quote_type = string[i]
		# 	else:
		# 		return_str += string[i]

		elif string[i] == "$" and allow_to_expand(is_quote_open, quote_type):
			expand_var = look_for_expand(string[i + 1:])
			i += get_str_to_expand_size(string[i + 1:])
			# display_str(string, i, return_str)
			# input("(enter)...")
			if expand_var is None:
				return_str += ""
				# print("NEED TO SKIP SPACE")
				while i + 1 < len(string) and string[i + 1] in [" ", "	"] and is_quote_open == False:
					i += 1
				# return_str = ft_strtrim_whitespace(return_str)
				if i + 1 == len(string):
					return_str = return_str.rstrip()
			else:
				return_str += expand_var

		else:
			return_str += string[i]
		i += skip_whitespace(string[i:], is_quote_open)

		# display_quotes_informations(is_quote_open, quote_type)
	return_value = subprocess.run(f"echo -n {initial_str}" ,shell=True, capture_output=True, executable="/bin/bash") #

	bash_str = return_value.stdout.decode('utf-8')

	# print(f"{BHWHITE}INITIAL STR : {string}{RESET}")
	# print(f"{BHWHITE}FINAL STR   : {GREENB}{return_str}{RESET}")
	# print(f"{BHWHITE}REAL BASH   : {CYANB}{bash_str}{RESET}")

	return return_str

	# os.system('clear')
	# highlighted_str_i("salut", 2, BHRED)
	# input("(enter)...")


# print(ft_strtrim_whitespace("   	SALUT  	"))
# print(ft_strtrim_whitespace("   	T  	"))
# print(ft_strtrim_whitespace("   	  	"))

if __name__ == "__main__":
	initial_str = "HELLO'$USER'_\"'az'\"_\"'$USER'\"_'$AC'_\"$UNEXIST_.\" $   $ $A   $USER$USER $.E $B        '$    .E' \"$   .B\""

	# initial_str = "   	$USER  	$USER    	 "
	# initial_str = " $USER  	$A  	$B $C   $D salut    	 "
	# initial_str = '"     "$USER   "    $USER" "           "'
	# initial_str = input("Enter string to visualize -> ")
	main(initial_str=initial_str)
