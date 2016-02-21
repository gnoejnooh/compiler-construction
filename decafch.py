def main():
	filename = raw_input('Decaf Syntax Checker\nEnter file name: ')
	file = open(filename, 'r+')
	yacc.parse(file)
	print "Yes"
		
if __name__ == '__main__':
    main()