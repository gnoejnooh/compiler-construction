import decaflexer
import decafparser

from ply import *

def main():
	filename = raw_input('Decaf Syntax Checker\nEnter file name: ')
	yacc.parse(open(filename).read())
	print "Yes"
		
if __name__ == '__main__':
    main()