Decaf AST Construction
Team Member: Chaeyoung Lee, Jeonghoon Kim

File Structure
README.txt		: README file for our documentation
decafch.py		: This file is originally from Professor's solution repo.
				  Get file and pass it to decafparser. File must have the ".decaf" file type.
				  After all things are done successfully, print ast.
				  If there are any errors during execution, we do not print ast.
decaflexer.py	: This file is originally from Professor's solution repo.
				  Tokenize given input file based on PLY/yacc specification.
decafparser.py	: This file is originally from Professor's solution repo.
				  Check with grammar rules on Decaf manual.
				  Pass the checked data to ast.py to build an ast.
ast.py			: This file has a structure of AST.
					We use this file to store all data with proper structure which follows Decaf manual.
					