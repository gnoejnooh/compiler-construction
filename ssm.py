import re
import sys

stack = []

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
		if (lines[i - 1] == 'ildc'):
			if lines[i].isdigit():
				continue
			else:
				sys.exit("Invalid instruction")
		elif (lines[i - 1] == 'jz' or lines[i - 1] == 'jnz' or lines[i - 1] == 'jmp'):
			if lines[i] + ':' in lines:
				continue
			sys.exit("Invalid instruction")
		else:
			if (isValid(lines[i]) is not True):
				sys.exit("Invalid instruction")

# Validate each element in the list
def isValid(str):
	# Checking for label
	if ':' in str:
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
	semanticanalysis(lines)
	global stack

	print lines
if __name__ == '__main__':
    main()