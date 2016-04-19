Interpreter for Register Abstract Machine

ami.py:   Interpreter code

To run, do
   python ami.py <filename>
   where <filename> is name of file with machine instructions
   machine instruction file should have a .ami extension
   when specifying the filename, the trailing .ami may be omitted

   This loads the machine program, and if there are no errors,
   starts execution at "__main__" label (if any).

   Run with -i option to get back to python prompt after
   loading/running to inspect machine state:
   -  peek("r") to see register r's value
   -  eval("instruction") to parse and evaluate another instruction
   -  see contents of 
      	  controlstack: saved return addresses
	  datastack: saved register valus
	  heap: heap (!!)
   	  program: sequence of instructions
 	  labelmap: a map from labels to instruction addresses.
   -  see current values of 
      	  heap pointer (hp)
      	  static address pointer (sap)
	  program counter (pc)

   Add your own code if you want to singlestep through the program,
   poke registers (change their values), skip over calls etc.
   
Note: Register abstract machine is not intended as your final target.  This interpreter is provided so that you can test your intermediate code generation.
