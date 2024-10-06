from Colors import *
import os
import sys
from mylib import *
from utils import *
import subprocess

def allow_to_expand(is_quote_open: bool, quote_type: bool) -> bool:
	# return (is_quote_open == True and quote_type == '\'') == False
	if is_quote_open:
		if quote_type == '"':
			return True
		return False
	return True

# Une variable d'environnement ne peut contenir que [a-z], [A-Z], [0-9], _
def is_valid_expand(char: str) -> bool:
	return char.isalnum() or char == '_'


def get_str_to_expand_size(string: str) -> int:
	i = 0
	if is_valid_expand(string[i]) == False:
		return 0

	while i < len(string) and is_valid_expand(string[i]):
		i += 1
	return i

def get_expand_value(string: str) -> str:
	i: int = 0

	# Si l'élément juste après le $ n'est pas valide, dans ce cas il faut conserver le $
	if is_valid_expand(string[i]) == False:
		return "$"

	# Ça permet d'obtenir la taille précisement du mot à expand
	# Ex. 'USER.SALUT' renvoie 4 car y'a que USER à expand
	i = get_str_to_expand_size(string)

	# On conserve que la partie de la string à expand
	str_to_expand = string[:i]

	# La valeur dans l'env si elle existe sinon None
	return os.getenv(str_to_expand)


def skip_whitespace(string: str, is_quote_open: bool) -> int:
	i = 0
	# Si les cotes sont fermés et qu'on est sur un espace, on doit skip tous les autres
	if i < len(string) and string[i] in [" ", "	"] and is_quote_open == False:
		while i < len(string) and string[i] in [" ", "	"]:
			i += 1
		return i
	# Sinon on avance juste de 1
	else:
		return 1

def handle_input_parsing(initial_str: str, step: bool = False) -> str:
	"""Cette fonction a pour but de traiter l'input principal :
	- Retirer les guillemets
	- Expand les variables d'environnements
	- Traitement parfait des espaces

	Args:
		initial_str (str): L'input par défaut

	Returns:
		str: L'input après son traitement.
	"""

	return_str: str = ""

	# Le bash retire les whitespaces
	string: str = my_trim(initial_str, None)
	is_quote_open: bool = False
	quote_type: str = None
	i: int = 0

	while i < len(string):
		display_step(string, i, return_str, is_quote_open, quote_type, REDB, step)

		if string[i] == '"' or string[i] == '\'':
			# Si la guillemet ouvert est celle actuel, on la ferme
			if is_quote_open == True and quote_type == string[i]:
				is_quote_open = False
			# Sinon si aucune guillemet est ouverte, on l'ouvre et on indique la guillemet ouverte
			elif is_quote_open == False:
				is_quote_open = True
				quote_type = string[i]
			# Sinon, donc ça veut dire qu'une guillemet est ouverte mais c'est pas la bonne, donc il fait l'ajouter
			else:
				return_str += string[i]


		elif string[i] == "$" and allow_to_expand(is_quote_open, quote_type):
			# Ex. "$USER_.SALUT" envoie ça à la fonction "USER_.SALUT"
			expand_var: str | None = get_expand_value(string[i + 1:])
			# On incremente i jusqu'à la fin de la variable
			i += get_str_to_expand_size(string[i + 1:])
			if expand_var is None:
				display_step(string, i, return_str, is_quote_open, quote_type, REDB, step)

				# Si la variable n'existe pas, il faut retirer tous les espaces jusqu'à la prochaine valeur
				while i + 1 < len(string) and my_isspace(string[i + 1]) and is_quote_open == False:
					i += 1
					display_step(string, i, return_str, is_quote_open, quote_type, REDB, step)

				# Si jamais la prochaine valeur c'est la fin du mot, il faut retirer tous les espaces à droite
				# car c'est possible qu'il y en avait avant.
				if i + 1 == len(string):
					return_str = return_str.rstrip()
			else:
				return_str += expand_var
		else:
			return_str += string[i]
		i += skip_whitespace(string[i:], is_quote_open)

	display_step(string, i, return_str, is_quote_open, quote_type, REDB, step)
	return return_str

if __name__ == "__main__":

	if len(sys.argv) == 2 and sys.argv[1] in ['-p', '--prompt']:
		# HELLO'$USER'_"'az'"_"'$USER'"_'$AC'_"$UNEXIST_." $   $ $A   $USER$USER $.E $B        '$    .E' "$   .B"
		# "SALUT$USER$USER'$USER'$B$E"
		initial_str = input("Enter string to visualize -> ")
	else:
		initial_str = "HELLO'$USER'_\"'az'\"_\"'$USER'\"_'$AC'_\"$UNEXIST_.\" $   $ $A   $USER$USER $.E $B        '$    .E' \"$   .B\""


	return_str = handle_input_parsing(initial_str=initial_str, step=True)
	return_bash = subprocess.run(f"echo -n {initial_str}" ,shell=True, capture_output=True, executable="/bin/bash") #

	bash_str = return_bash.stdout.decode('utf-8')

	print(f"{BHWHITE}INITIAL STR : {BHWHITE}{initial_str}{RESET}")
	print(f"{BHWHITE}FINAL STR   : {GREENB}{return_str}{RESET}")
	print(f"{BHWHITE}REAL BASH   : {CYANB}{bash_str}{RESET}")


