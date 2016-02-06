import re
import sys

def scanner():

	lines = sys.stdin.readlines()
	newline = []
	for i in range(len(lines)):
		words = lines[i].split()
		for word in words:
			newline.append(word)
		#lines[i] = lines[i].lstrip(' ')
		#lines[i] = lines[i].replace('\n','')
	return newline

def main():
	lines = scanner()
	
	print lines
if __name__ == '__main__':
    main()