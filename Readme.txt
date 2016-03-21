CSE304 Homework 2 - Decaf Syntax Checker
Team Members: Chaeyoung Lee, Jeonghoon Kim

1) decafch.py
- This is the main file of decaf syntax checker. 
- It opens the file and check if the file is empty. If the file is not empty, try parsing.

2) decaflexer.py
- It breaks inputs to a collection of tokens.
- We specified rules for tokens using regular expressions (Specific rules are in the file with proper comments).

3) decafparser.py
- It applies the rules using tokens from decaflexer.py
- We specified rules for parsing (Specific rules are in the file with proper comments).
- If there is any error while parsing, the program will print out error message and terminates after that. 