from Colors import *
import os
import subprocess

ENVIRONNEMENT = {
	"USER": "theo"
}

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
	print(f"{BHGREEN}RETURN  : {BHWHITE}{return_str}")
	print(f"{BHBLUE}CURRENT :{BHWHITE} ", end="")
	highlighted_str_i(string, index, BHRED)
	print(RESET)
	# input("(enter)...")

def look_for_expand(string: str) -> str:
	# NEED TO KNOW WHERE TO STOP EXPAND
	env_variable = ENVIRONNEMENT.get(string)
	return "EXPAND"
	# return env_variable if env_variable is not None else ""

# def get_expand_size(string: str) -> int:
# 	env_variable = ENVIRONNEMENT.get(string)
# 	if len(env_variable )

def allow_to_expand(is_quote_open: bool, quote_type: bool) -> bool:
	if is_quote_open:
		if quote_type == '"':
			return True
		return False
	return True

def main(string: str):
	print(string)

	return_str = ""

	display_quotes_informations(True, '"')
	display_quotes_informations(True, '\'')
	display_quotes_informations(False, '"')
	display_str(string, 3, return_str)

	is_quote_open = False
	quote_type = ""

	i = 0
	while i < len(string):
		# print(f"--{i}")
		if string[i] == '"':
			if is_quote_open == True and quote_type == string[i]:
				is_quote_open = False
			elif is_quote_open == False:
				is_quote_open = True
				quote_type = string[i]
			else:
				return_str += string[i]



		elif string[i] == '\'':
			if is_quote_open == True and quote_type == string[i]:
				is_quote_open = False
			elif is_quote_open == False:
				is_quote_open = True
				quote_type = string[i]
			else:
				return_str += string[i]
		elif string[i] == "$" and allow_to_expand(is_quote_open, quote_type):
			return_str += look_for_expand(string[i:])
			# print(i)
			# print(len(look_for_expand(string[i:])))
			i += len(look_for_expand(string[i:])) - 1
			print(i)
		else:
			return_str += string[i]
		i += 1

		# display_quotes_informations(is_quote_open, quote_type)
		# display_str(string, i, return_str)
		# input("(enter)...")
	return_value = subprocess.run(f"echo {initial_str}" ,shell=True, capture_output=True) #

	bash_str = return_value.stdout.decode('utf-8').strip()

	print(f"{BHWHITE}INITIAL STR : {initial_str}{RESET}")
	print(f"{BHWHITE}FINAL STR   : {BHGREEN}{return_str}{RESET}")
	print(f"{BHWHITE}REAL BASH   : {BHCYAN}{bash_str}{RESET}")


	# os.system('clear')
	# highlighted_str_i("salut", 2, BHRED)
	# input("(enter)...")

if __name__ == "__main__":
	initial_str = "HELLO'$USER'_\"'az'\"_\"'$USER'\"_'$AC'_\"$UNEXIST_\""

	initial_str = input("Enter string to visualize -> ")
	main(string=initial_str)
