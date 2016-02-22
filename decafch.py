from ply import *
import decaflexer
import decafparser

def main():
	#filename = raw_input('Decaf Syntax Checker\nEnter file name: ')
	filename = "test.txt"
	yacc.parse(open(filename).read())
	print "Yes"
		
if __name__ == '__main__':
    main()