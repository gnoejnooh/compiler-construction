""" AM Interpreter
An interpreter for a register abstract machine.
Usage: python ami.py <filename>
where <filename> is the name of the file containing the abstract machine program.
"""
import sys
import getopt
import math

registers = {}
pc = None
controlstack = []
datastack = []
heap = []
sap = 0    # static area pointer
hp = 0     # heap pointer
program = [] # program is simply a sequence of instructions
labelmap = {} # maps labels to instruction number in programs; initialized by program loader

def get_reg(r):
    ''' Get the value of a temporary/argument register
    Return 0 if the specified register has not been seen before'''
    global registers
    if (r in registers):
        return registers[r]
    else:
        print "No such register %s"%r
        return 0

def get_regs(rs):
    '''Return list of values corresponding to list of registers'''
    return [get_reg(r) for r in rs]

#
#  Handlers for instructions 
#
def move_immed_i((r,i)):
    global registers, pc
    registers[r] = int(i)
    pc += 1
    
def move_immed_f((r,f)):
    global registers, pc
    registers[r] = float(f)
    pc += 1

def move((r1,r2)):
    global registers, pc
    registers[r1] = registers[r2]
    pc += 1

def iadd((d,s1,s2)):
    global registers, pc
    [i1, i2] = get_regs([s1,s2])
    registers[d] = i1+i2
    pc += 1
    
def isub((d,s1,s2)):
    global registers, pc
    [i1, i2] = get_regs([s1,s2])
    registers[d] = i1-i2
    pc += 1
    
def imul((d,s1,s2)):
    global registers, pc
    [i1, i2] = get_regs([s1,s2])
    registers[d] = i1*i2
    pc += 1
    
def idiv((d,s1,s2)):
    global registers, pc
    [i1, i2] = get_regs([s1,s2])
    registers[d] = i1/i2
    pc += 1
    
def imod((d,s1,s2)):
    global registers, pc
    [i1, i2] = get_regs([s1,s2])
    registers[d] = i1%i2
    pc += 1
    
def igt((d,s1,s2)):
    global registers, pc
    [i1, i2] = get_regs([s1,s2])
    registers[d] = 1 if (i1>i2) else 0
    pc += 1
    
def igeq((d,s1,s2)):
    global registers, pc
    [i1, i2] = get_regs([s1,s2])
    registers[d] = 1 if (i1>=i2) else 0
    pc += 1
    
def ilt((d,s1,s2)):
    global registers, pc
    [i1, i2] = get_regs([s1,s2])
    registers[d] = 1 if (i1<i2) else 0
    pc += 1
    
def ileq((d,s1,s2)):
    global registers, pc
    [i1, i2] = get_regs([s1,s2])
    registers[d] = 1 if (i1<=i2) else 0
    pc += 1
    
def itof((d,s)):
    global registers, pc
    i = get_reg(s)
    registers[d] = i*1.0
    pc += 1
    
def ftoi((d,s)):
    global registers, pc
    f = get_reg(s)
    registers[d] = math.trunc(f)
    pc += 1

# Branches: Note that all labels have been checked to see if they're valid targets
def bz((r,l)):
    global registers, pc
    i = get_reg(r)
    if (i == 0):
        pc = labelmap[l]
    else:
        pc += 1

def bnz((r,l)):
    global registers, pc
    i = get_reg(r)
    if (i != 0):
        pc = labelmap[l]
    else:
        pc += 1

def jmp((l,)):
    global pc
    pc = labelmap[l]

# Heap access; if addess specified is invalid, the instruction is a nop
def hload((d,sb,so)):
    global registers, pc, heap
    if (sb == "sap"):
        b = sap
        o = get_reg(so)
    else:
        [b,o] = get_regs([sb,so])
    i = b+o
    if (i<0) or (i>=len(heap)):
        print "Heap underflow/overflow"
    else:
        registers[d] = heap[i]
    pc += 1
    
def hstore((db,do,s)):
    global registers, pc, heap
    if (db == "sap"):
        b = sap
        [o,x] = get_reg(do,s)
    else:
        [b,o,x] = get_regs([db,do,s])
    i = b+o
    if (i<0) or (i>=len(heap)):
        print "Heap underflow/overflow"
    else:
        heap[i] = x
    pc += 1

def halloc((d,sn)):
    global registers, pc, heap, hp
    n = get_reg(sn)
    register[d] = hp
    for i in range(hp, hp+n):
        heap[i] = 0
    hp += n
    pc += 1

def call((l,)):
    global  pc
    controlstack.append(pc+1)
    pc = labelmap[l]

def ret(dummy):
    global pc
    if (len(controlstack) == 0):
        # Done with all instructions
        pc = -1
    else:
        pc = controlstack.pop()

def save((r,)):
    global registers, pc
    i = get_reg(r)
    datastack.append(i)
    pc += 1
    
def restore((r,)):
    global registers, pc
    if (len(datastack) == 0):
        print "Restore from nowhere?"
    else:
        registers[r] = datastack.pop()
    pc += 1
    
def print_reg((r,)):
    global registers, pc
    print "Register %s = "%r,
    if r not in registers:
        print "None Such"
    else:
        print registers[r]

def nop(t):
    global pc
    pc += 1

def notyet(t):
    print "Instruction not yet implemented!"
    
    
typenames = {'r':'register', 'g':'general register', 'l':'label', 'i':'integer', 'f':'float'}

instructions = {  #known insrtuctions: number of arguments, handler, type of args
                  "move_immed_i":(2,move_immed_i, 'ri'),
                  "move_immed_f":(2,move_immed_f, 'rf'),
                  "move":(2,move, 'rr'),

                  "iadd":(3,iadd, 'rrr'),
                  "isub":(3,isub, 'rrr'),
                  "imul":(3,imul, 'rrr'),
                  "idiv":(3,idiv, 'rrr'),
                  "imod":(3,imod, 'rrr'),
                  "igt":(3,igt, 'rrr'),
                  "igeq":(3,igeq, 'rrr'),
                  "ilt":(3,ilt, 'rrr'),
                  "ileq":(3,ileq, 'rrr'),
                  
                  "fadd":(3,iadd, 'rrr'),  # use same functions as the integer counterparts!
                  "fsub":(3,isub, 'rrr'),
                  "fmul":(3,imul, 'rrr'),
                  "fdiv":(3,idiv, 'rrr'),
                  "fgt":(3,igt, 'rrr'),
                  "fgeq":(3,igeq, 'rrr'),
                  "flt":(3,ilt, 'rrr'),
                  "fleq":(3,ileq, 'rrr'),

                  "itof":(2,itof, 'rrr'),
                  "ftoi":(2,ftoi, 'rrr'),

                  "hload":(3,hload, 'rgr'),
                  "hstore":(3,hstore, 'grr'),
                  "halloc":(2,halloc, 'rr'),

                  "bz":(2,bz, 'rl'),
                  "bnz":(2,bnz, 'rl'),
                  "jmp":(1,jmp, 'l'),

                  "call":(1,call, 'l'),
                  "ret":(0,ret, ''),
                  "save":(1,save, 'r'),
                  "restore":(1,restore, 'r'),

                  "peek":(1,print_reg,'r'),
                  "nop":(0,nop,'')
                  }

def interp(opcode, args):
    if (opcode not in instructions):
        print "No such instruction '%s'!"%(opcode)
        return
    (n,fn,types) = instructions[opcode]
    if (len(args) != n):
        print "Instruction %s needs %d args; %d given"%(opcode, n, len(args))
        return
    t = tuple(args)
    # now invoke!
    fn(t)
    
import re
wordpattern = "[ \t\n]+|,"    
def read_instr(str):
    # first take out comments.
    if ("#" in str):
        parts = str.split("#")
        instr = parts[0]
    else:
        instr = str
    #  Not take out label if any
    if (":" in instr):
        parts = instr.split(":")
        label = parts[:-1]
        instr = (parts[-1:])[0]  # only the last element
    else:
        label = ""
    # now instr contains the opcode and arguments.  Split with space, tab, comma:
    opargs = re.split(wordpattern, instr)
    opargs = [w for w in opargs if w != '']
    if (len(opargs) < 1):
        return (label, None, None)
    else:
        return (label, opargs[0], opargs[1:])
        
def eval(instr):
    ''' Evaluate the given instruction '''
    (label, opcode, args) = read_instr(instr)
    # ignore label, since this is in the interpreter loop
    interp(opcode, args)

def peek(reg):
    ''' print the value of a given register; use the peek instruction!'''
    interp("peek", [reg])

def typecheck_arg(a, t):
    if (t=='r'):
        # register type: td+ or rd+
        if (len(a) > 1):
            f = a[0]
            i = a[1:]
            if ((f=='t' or f=='a') and i.isdigit()):
                return True
        else:
            return False
    elif (t=='g'):
        # general register, could be one of 'r' or 'sap'
        if (a=="sap") or (typecheck_arg(a,'r')):
            return True
        else:
            return False
    elif (t=="l"):
        # label, anything goes
        return True
    elif (t=='i'):
        # integer:
        try:
            i = int(a)
            return True
        except ValueError:
            return False
    elif (t=='f'):
        # float:
        try:
            i = float(a)
            return True
        except ValueError:
            return False
    else:
        # what other type is there? return false and wait for bug reports
        return False
    
def typecorrect(args, types, line):
    n = len(args)
    correct = True
    for i in range(0,n):
        a = args[i]
        t = types[i]
        if not typecheck_arg(a,t):
            print "At line %d, argument %d is expected to be a %s, found '%s'"%(line, i, typenames[t], a)
            correct = False
    return correct
def directive(l, lineno):
    global heap, hp, sap
    l.strip()
    if (len(l) == 0) or (l[0] != '.'):
        return False  # not  a directive

    parts = l.split()
    if ((len(parts) == 2) and (parts[0] == '.static_data')):
        try:
            n = int(parts[1])
        except ValueError:
            print "Integer expected in static data directive in line %d, '%s' found"%(lineno,parts[1])
            return True
        heap = [0 for i in range(n)]
        sap = 0
        hp = n
    else:
        print "Error in processing directive '%s' in line %d"%(l, lineno)
    return True

def load(filename):
    '''load given file'''
    global program, labelmap
    n = 0 # instruction number
    line = 0
    error = False
    f = open(filename, "rU")
    while (True):
        l=f.readline()
        if (l == ""):
            break  #end of file
        line += 1
        if directive(l, line):
            continue
        (labels, opcode, args) = read_instr(l)
        for label in labels:
            if (label != ""):
                if (label in labelmap):
                    print "Duplicate label '%s' at line %d"%(label, line)
                    error = True
                else:
                    labelmap[label] = n
        if (opcode != None):
            if (opcode not in instructions):
                print "Unknown instruction %s at line %d"%(opcode, line)
                error = True
            else:
                (arity, fn, types) = instructions[opcode]
                if (len(args) != arity):
                    print "Instruction %s at line %d takes %d args; %d given"%(opcode, line,arity,len(args))
                    error = True
                elif typecorrect(args, types, line):
                    program.append((opcode, args, line))
                    n += 1
    f.close()
    # Check if every label appears in the program!
    for (opcode, args, line) in program:
        if (opcode in ["bz", "bnz"]):
            dest = args[1]
        elif (opcode in ["jmp", "call"]):
            dest = args[0]
        else:
            dest = None
        if (dest != None):
            if (dest not in labelmap):
                print "Label '%s' at line %d not defined"%(dest, line)
                error = True
                
    if (error):
        program = []
        labelmap = {}

def state(k=8):
    global registers
    print "SAP =", sap
    print "HP =", hp
    print "controlstack's length = ", len(controlstack)
    print "datastack's length = ", len(datastack)
    print "Registers: ",
    print ([(r,registers[r]) for r in registers])[:k]
    
def run(label):
    global labelmap, program, pc
    if (label not in labelmap):
        print "Can't run!  No such label"
    else:
        pc = labelmap[label]
        while (pc >= 0 and pc < len(program)):
            (opcode, args, l) = program[pc]
            interp(opcode, args)
        state()

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def main(argv=None):
    if argv is None:
        argv = sys.argv
        
    # parse command line options
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "h", ["help"])
        except getopt.error, msg:
            raise Usage(msg)
        for o,a in opts:
            if o in ("-h", "--help"):
                print __doc__
                sys.exit(0)
        if (len(args) != 1):
            raise Usage("A single file name argument is required")
        fullfilename = args[0]
        if (fullfilename.endswith('.ami')):
            (filename,s,e) = fullfilename.rpartition('.')
        else:
            filename=fullfilename
        infile = filename + ".ami"
        load(infile)
        if ("__main__" in labelmap):
            run("__main__")
        
    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "For help use --help"
        sys.exit(1)

if __name__ == "__main__":
    #    sys.exit(main())
    main()
