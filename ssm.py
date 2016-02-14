import re
import sys
import instruction

# Read from standard input
def scanner():
	lines = sys.stdin.readlines()
	if len(lines) == 0:
		sys.exit("Invaild input: There is no input.")
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
		if lines[i - 1] == 'ildc':
			if lines[i].lstrip('-').isdigit():
				continue
			else:
				sys.exit("Input: " + lines[i] + "\nInvalid input: Wrong input (Not a digit)")
		elif (lines[i - 1] == 'jz' or lines[i - 1] == 'jnz' or lines[i - 1] == 'jmp'):
			if lines[i] + ':' in lines:
				tmpLine = lines[i]
				for j in range(len(tmpLine)):
					if(tmpLine[j].isalpha()):
						continue
					elif j == 0 and tmpLine[j] == '_':
						sys.exit("Input: " + lines[i] + "\nInvaild label: Label starts with underscore('_')")
					elif tmpLine[j] == '_':
						continue
					else:
						sys.exit("Input: " + lines[i] + "\nInvaild label: Label name has invaild character")
				continue
			sys.exit("Input: " + lines[i] + "\nInvalid input: label does not exist")
		else:
			if (isValid(lines[i]) is not True):
				sys.exit("Input: " + lines[i] + "\nInvalid command: Please check the command")

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
		'imod': True,
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
	output = instruction.compile(lines)
	print output
		
if __name__ == '__main__':
    main()