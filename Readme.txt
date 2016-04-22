CSE304 Homework #5 - Intermediate Code Generator
Members: Chaeyoung Lee & Jeonghoon Kim

------------------------------------------------------
How to run the program
------------------------------------------------------
> python decafch.py [DECAF FILE PATH]
*** Output file is generated at the same folder as decaf file
*** Output file's name is same as decaf file except the extension.

------------------------------------------------------
File Structure
------------------------------------------------------
|- [Folder] ami
|- [Folder] tests
|- absmc.py
|- ast.py
|- decafch.py
|- decaflexer.py
|- decafparser.py
|- parsetab.py
|- Readme.txt

------------------------------------------------------
Details
------------------------------------------------------
[Folder] ami : AMI interpreter, written by professor (Given files from solution repo)
[Folder] tests : Test cases for decaf and ami files

[Files]
- absmc.py : This file is for printing the machine code based on type-checked AST.
- ast.py : Modified from given HW4;
						This file includes all syntax for machine code
- decafch.py : Write .ami file on the same directory of .decaf file with same name.
- decaflexer.py : No changes from HW4
- decafparser.py : No changes from HW4
- parsetab.py : No changes from HW4
