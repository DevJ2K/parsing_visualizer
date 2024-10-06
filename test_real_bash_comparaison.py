# import pytest
import subprocess
from draft import main
from main import handle_input_parsing

# $USER$USER
# $USER    $USER
# "     "$USER   "    $USER"
# "SALUT"

with open("input.txt", 'r') as f:
	all_input = f.read().splitlines()

	# print(all_input)

	# re_value = subprocess.run(f"echo {all_input[0]}" ,shell=True, capture_output=True)
	# print(re_value.stdout.decode().strip())
	# print(all_input)

def test_all_inputs():
	# print(all_input)
	for input_to_test in all_input:
		r_value = subprocess.run(f"echo -n {input_to_test}" ,shell=True, capture_output=True, executable="/bin/bash")
		bash_value = r_value.stdout.decode('utf-8')
		print(f"Current input test : {input_to_test}")
		print(f"EXCEPT : {bash_value}")
		print("=" * 25)
		assert handle_input_parsing(initial_str=input_to_test) == bash_value
