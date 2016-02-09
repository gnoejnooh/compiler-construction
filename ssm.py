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
		if (lines[i - 1] == 'ildc'):4
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

def instruction(lines):
	global stack
	i = 0
	while i < len(lines):
		if lines[i] == 'ildc':
			stack.append(int(lines[i + 1]))
			i = i + 1
		if lines[i] == 'iadd':
			try:
				stack.append(int(stack.pop()) + int(stack.pop()))
			except:
				sys.exit("Pop from empty stack")
		if lines[i] == 'isub':
			try:
				num = int(stack.pop())
				stack.append(int(stack.pop()) - num)
			except:
				sys.exit("Pop from empty stack")
		if lines[i] == 'imul':
			try:
				stack.append(int(stack.pop()) * int(stack.pop()))
			except:
				sys.exit("Pop from empty stack")
		if lines[i] == 'idiv':
			try:
				num = int(stack.pop())
				stack.append(int(stack.pop()) / num)
			except:
				sys.exit("Pop from empty stack")
		if lines[i] == 'imod':
			try:
				num = int(stack.pop())
				stack.append(int(stack.pop()) % num)
			except:
				sys.exit("Pop from empty stack")
		if lines[i] == 'pop':
			try:
				stack.pop()
			except:
				sys.exit("Pop from empty stack")
		if lines[i] == 'dup':
			try:
				stack.append(stack[len(stack) - 1])
			except:
				sys.exit("No element in the stack")
		if lines[i] == 'swap':
			try:
				stack.append(stack.pop(len(stack) - 2))
			except:
				sys.exit("No element in the stack")
		if lines[i] == 'jz':
			try:
				if (int(stack.pop()) == 0):
					i = lines.index(lines[i + 1] + ':')
			except:
				sys.exit("No element in the stack")
		if lines[i] == 'jnz':
			try:
				if (int(stack.pop()) != 0):
					i = lines.index(lines[i + 1] + ':')
			except:
				sys.exit("No element in the stack")
		if lines[i] == 'jmp':
			try:
				i = lines.index(lines[i + 1] + ':')
			except:
				sys.exit("No element in the stack")
		i += 1

def main():
	lines = scanner()
	semanticanalysis(lines)
	global stack
	instruction(lines)
	print stack.pop()
		
if __name__ == '__main__':
    main()