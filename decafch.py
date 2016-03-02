import sys
import os
from ply import *
import decaflexer
import decafparser

def main():
	filename = raw_input('------------------------------------------------------------\n Decaf Syntax Checker\n------------------------------------------------------------\nEnter file name: ')
	try:
		if os.stat(filename).st_size <= 0:
			print "File error: File is empty (filename: %s)." % filename
			sys.exit()
		
	except OSError:
		print "File error: Cannot open the file (filename: %s)." % filename
		sys.exit()

	yacc.parse(open(filename).read())
	print "There is no syntax errors in given decaf file."
	
if __name__ == '__main__':
    main()