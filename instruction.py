import sys

stack = []
store_addr = []
store_value = []

def compile(lines):
	global stack
	global store_addr
	global store_value
	
	i = 0
	# Read an word from input and execute if it's one of the given commands.
	# If there is any error, print the error message and terminate the program.
	while i < len(lines):
		if lines[i] == 'ildc':
			stack.append(int(lines[i + 1]))
			i = i + 1
		elif lines[i] == 'iadd':
			try:
				stack.append(int(stack.pop()) + int(stack.pop()))
			except:
				sys.exit("Empty Stack Error: Pop from empty stack")
		elif lines[i] == 'isub':
			try:
				num = int(stack.pop())
				stack.append(int(stack.pop()) - num)
			except:
				sys.exit("Empty Stack Error: Pop from empty stack")
		elif lines[i] == 'imul':
			try:
				stack.append(int(stack.pop()) * int(stack.pop()))
			except:
				sys.exit("Empty Stack Error: Pop from empty stack")
		elif lines[i] == 'idiv':
			try:
				num = int(stack.pop())
				stack.append(int(stack.pop()) / num)
			except:
				sys.exit("Empty Stack Error: Pop from empty stack")
		elif lines[i] == 'imod':
			try:
				num = int(stack.pop())
				stack.append(int(stack.pop()) % num)
			except:
				sys.exit("Empty Stack Error: Pop from empty stack")
		elif lines[i] == 'pop':
			try:
				stack.pop()
			except:
				sys.exit("Empty Stack Error: Pop from empty stack")
		elif lines[i] == 'dup':
			try:
				stack.append(stack[len(stack) - 1])
			except:
				sys.exit("Empty Stack Error: No element in the stack")
		elif lines[i] == 'swap':
			try:
				stack.append(stack.pop(len(stack) - 2))
			except:
				sys.exit("Empty Stack Error: No element in the stack")
		elif lines[i] == 'jz':
			try:
				if (int(stack.pop()) == 0):
					i = lines.index(lines[i + 1] + ':')
			except:
				sys.exit("Empty Stack Error: No element in the stack")
		elif lines[i] == 'jnz':
			try:
				if (int(stack.pop()) != 0):
					i = lines.index(lines[i + 1] + ':')
			except:
				sys.exit("No element in the stack")
		elif lines[i] == 'jmp':
			try:
				i = lines.index(lines[i + 1] + ':')
			except:
				sys.exit("Empty Stack Error: No element in the stack")
		elif lines[i] == 'store':
			if len(stack) > 1 and (stack[len(stack)-1] is not None) and (stack[len(stack)-2] is not None):
				v1 = stack.pop()
				v2 = stack.pop()
				if v2 in store_addr:
					store_value[store_addr.index(v2)] = v1
				else:
					store_addr.append(v2)
					store_value.append(v1)
			else:
				sys.exit("Invaild stack: there is not enough data on the stack")
		elif lines[i] == 'load':
			if len(stack) > 0 and len(store_addr) > 0 and len(store_value) > 0:
				v1 = stack.pop()
				if v1 in store_addr:
					addr = store_addr.index(v1)
					store_addr[addr]
					val = store_value[addr]
					stack.append(val)
				else:
					sys.exit("Invaild address: The given address does not exist on the store")
			else:
				sys.exit("Invaild store: there is not enough data on the store")
		i += 1
	#print 'Stack'
	#print stack
	#print 'Store_addr'
	#print store_addr
	#print 'Store_value'
	#print store_value
	return stack.pop()