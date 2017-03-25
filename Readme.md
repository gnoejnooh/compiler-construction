# Decaf Compiler
A series of complete compilers for a sequence of increasingly complex high-level language, Decaf.

### Getting Started
The following is the sequence of compiler construction.
```
Syntax Checker -> AST Builder -> Type Checker -> Code Generation
```

Decaf compiler should be organized into the following files

| Operation | File | Description |
|-----------|------|-------------|
| Lexer | decaflexer.py | PLY/lex scanner specification file. |
| Parser | decafparser.py | PLY/yacc parser specification file. |
| AST | ast.py | table and class definitions for Decaf's AST. |
| Type Checker | typecheck.py | definitions for evaluating the type constraints and for name resolution. |
| Code Generator | codegen.py | definitions for generating code. |
| Abstract Machine | absmc.py | definitions for the abstract machine, and for manipulating abstract programs (e.g. SSA construction, printing). |
| Main Top-Level | decafc.py | containing the main python function that ties the modules together, takes command line argument of input file name, and processes the Decaf program in that file. |

### Running

decafc takes a single command line argument, with the name of the Decaf program to be translated. For example, if the Decaf program is in fum.decaf, then the invocation will be as
```
python decafc.py fum  

python decafc.py fum.decaf  
```
The output file is generated at the same folder as decaf file with same name except the extension.
