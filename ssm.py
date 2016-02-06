import re
import sys

# Read from standard input
def scanner():
	lines = sys.stdin.readlines()
	newline = []
	for i in range(len(lines)):
		# Consideration for the comment line
		if lines[i].startswith('#'):
			continue
		# If comments are after the instruction, this should catch it
		if '#' in lines[i]:
			lines[i] = lines[i].split('#', 1)[0]
		words = lines[i].split()
		# Append splited instruction into new list
		for word in words:
			newline.append(word)
	return newline

# Analyze the sequence (ordering, parameter, infinite loop)
def semanticanalysis(lines):
	for i in range(len(lines)):
		if (isValid(lines[i])):
			sys.exit("Invalid instruction")

# Validate each element in the list
### NOTE: currently giving error since there is no case for label without ':'
def isValid(str):
	# Checking for label
	if ':' in str:
		return True
	# Checking for digit
	if str.isdigit():
		return True
	# Checking for instruction
	return {
		'ildc': True,
		'iadd': True,
		'isub': True,
		'imul': True,
		'idiv': True,
		'pop': True,
		'dup': True,
		'swap': True,
		'jz': True,
		'jnz': True,
		'jmp': True,
		'load': True,
		'store': True,
	}.get(str, False)

def main():
	lines = scanner()
	print lines
	semanticanalysis(lines)

	print lines
if __name__ == '__main__':
    main()