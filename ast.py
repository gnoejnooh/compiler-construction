import typecheck

classtable = {}  # initially empty dictionary of classes.
lastmethod = 0
lastconstructor = 0

# Class table.  Only user-defined classes are placed in the class table.
def lookup(table, key):
    if key in table:
        return table[key]
    else:
        return None

def addtotable(table, key, value):
    table[key] = value


def print_ast():
    for cid in classtable:
        c = classtable[cid]
        c.printout()
    print "-----------------------------------------------------------------------------"
    

def initialize_ast():
    # define In class:
    cin = Class("In", None)
    cin.builtin = True     # this is a builtin class
    cout = Class("Out", None)
    cout.builtin = True     # this, too, is a builtin class

    scanint = Method('scan_int', cin, 'public', 'static', Type('int'))
    scanint.update_body(SkipStmt(None))    # No line number information for the empty body
    cin.add_method(scanint)
    
    scanfloat = Method('scan_float', cin, 'public', 'static', Type('float'))
    scanfloat.update_body(SkipStmt(None))    # No line number information for the empty body
    cin.add_method(scanfloat)

    printint = Method('print', cout, 'public', 'static', Type('void'))
    printint.update_body(SkipStmt(None))    # No line number information for the empty body
    printint.add_var('i', 'formal', Type('int'))   # single integer formal parameter
    cout.add_method(printint)
    
    printfloat = Method('print', cout, 'public', 'static', Type('void'))
    printfloat.update_body(SkipStmt(None))    # No line number information for the empty body
    printfloat.add_var('f', 'formal', Type('float'))   # single float formal parameter
    cout.add_method(printfloat)
    
    printboolean = Method('print', cout, 'public', 'static', Type('void'))
    printboolean.update_body(SkipStmt(None))    # No line number information for the empty body
    printboolean.add_var('b', 'formal', Type('boolean'))   # single boolean formal parameter
    cout.add_method(printboolean)
    
    printstring = Method('print', cout, 'public', 'static', Type('void'))
    printstring.update_body(SkipStmt(None))    # No line number information for the empty body
    printstring.add_var('b', 'formal', Type('string'))   # single string formal parameter
    cout.add_method(printstring)

    addtotable(classtable, "In", cin)
    addtotable(classtable, "Out", cout)


class Class:
    """A class encoding Classes in Decaf"""
    def __init__(self, classname, superclass):
        self.name = classname
        self.superclass = superclass
        self.fields = {}  # dictionary, keyed by field name
        self.constructors = []
        self.methods = []
        self.builtin = False

    def printout(self):
        if (self.builtin):
            return     # Do not print builtin methods
        
        print "-----------------------------------------------------------------------------"
        print "Class Name: {0}".format(self.name)
        sc = self.superclass
        if (sc == None):
            scname = ""
        else:
            scname = sc.name
        print "Superclass Name: {0}".format(scname)
        print "Fields:"
        for f in self.fields:
            (self.fields[f]).printout()
        print "Constructors:"
        for k in self.constructors:
            k.printout()
        print "Methods:"
        for m in self.methods:
            m.printout()
        

    def add_field(self, fname, field):
        self.fields[fname] = field
    def add_constructor(self, constr):
        self.constructors.append(constr)
    def add_method(self, method):
        self.methods.append(method)

    def lookup_field(self, fname):
        return lookup(self.fields, fname)

            
class Type:
    """A class encoding Types in Decaf"""
    def __init__(self, basetype, params=None):
        if ((params == None) or (params == 0)):
            if (basetype in ['int', 'boolean', 'float', 'string', 'void']):
                self.kind = 'basic'
                self.typename = basetype
            elif (isinstance(basetype, Type)):
                self.kind = basetype.kind
                self.typename = basetype.typename
            else:
                self.kind = 'class'
                self.typename = basetype
        else:
            bt = Type(basetype, params-1)
            self.kind = 'array'
            self.basetype = bt

    def __str__(self):
        if (self.kind == 'array'):
            return 'array(%s)'%(self.basetype.__str__())
        elif (self.kind == 'class'):
            return 'user(%s)'%(self.typename)
        else:
            return self.typename

    def __repr(self):
        return self.__str__()

class Field:
    """A class encoding fields and their attributes in Decaf"""
    lastfield = 0
    def __init__(self, fname, fclass, visibility, storage, ftype):
        Field.lastfield += 1
        self.name = fname
        self.id = Field.lastfield
        self.inclass = fclass
        self.visibility = visibility
        self.storage = storage
        self.type = ftype

    def printout(self):
        print "FIELD {0}, {1}, {2}, {3}, {4}, {5}".format(self.id, self.name, self.inclass.name, self.visibility, self.storage, self.type)

class Method:
    """A class encoding methods and their attributes in Decaf"""
    def __init__(self, mname, mclass, visibility, storage, rtype):
        global lastmethod
        self.name = mname
        lastmethod += 1
        self.id = lastmethod
        self.inclass = mclass
        self.visibility = visibility
        self.storage = storage
        self.rtype = rtype
        self.vars = VarTable()
        
    def update_body(self, body):
        self.body = body

    def add_var(self, vname, vkind, vtype):
        self.vars.add_var(vname, vkind, vtype)

    def printout(self):
        print "METHOD: {0}, {1}, {2}, {3}, {4}, {5}".format(self.id, self.name, self.inclass.name, self.visibility, self.storage, self.rtype)
        print "Method Parameters:",
        print ', '.join(["%d"%i for i in self.vars.get_params()])
        self.vars.printout()
        print "Method Body:"
        self.body.printout()
        
class Constructor:
    """A class encoding constructors and their attributes in Decaf"""
    def __init__(self, cname, visibility):
        global lastconstructor
        self.name = cname
        lastconstructor += 1
        self.id = lastconstructor
        self.visibility = visibility
        self.vars = VarTable()
        
    def update_body(self, body):
        self.body = body

    def add_var(self, vname, vkind, vtype):
        self.vars.add_var(vname, vkind, vtype)

    def printout(self):
        print "CONSTRUCTOR: {0}, {1}".format(self.id, self.visibility)
        print "Constructor Parameters:",
        print ', '.join(["%d"%i for i in self.vars.get_params()])
        self.vars.printout()
        print "Constructor Body:"
        self.body.printout()
        

class VarTable:
    """ Table of variables in each method/constructor"""
    def __init__(self):
        self.vars = {0:{}}
        self.lastvar = 0
        self.lastblock = 0
        self.levels = [0]

    def enter_block(self):
        self.lastblock += 1
        self.levels.insert(0, self.lastblock)
        self.vars[self.lastblock] = {}

    def leave_block(self):
        self.levels = self.levels[1:]
        # where should we check if we can indeed leave the block?

    def add_var(self, vname, vkind, vtype):
        self.lastvar += 1
        c = self.levels[0]   # current block number
        v = Variable(vname, self.lastvar, vkind, vtype)
        vbl = self.vars[c]  # list of variables in current block
        vbl[vname] = v
    
    def _find_in_block(self, vname, b):
        if (b in self.vars):
            # block exists
            if (vname in self.vars[b]):
                return self.vars[b][vname]
        # Otherwise, either block b does not exist, or vname is not in block b
        return None

    def find_in_current_block(self, vname):
        return self._find_in_block(vname, self.levels[0])

    def find_in_scope(self, vname):
        for b in self.levels:
            v = self._find_in_block(vname, b)
            if (v != None):
                return v
            # otherwise, locate in enclosing block until we run out
        return None

    def get_params(self):
        outermost = self.vars[0]  # 0 is the outermost block
        ids = [outermost[vname].id for vname in outermost if outermost[vname].kind=='formal']
        return ids

    def printout(self):
        print "Variable Table:"
        for b in range(self.lastblock+1):
            for vname in self.vars[b]:
                v = self.vars[b][vname]
                v.printout()
        

class Variable:
    """ Record for a single variable"""
    def __init__(self, vname, id, vkind, vtype):
        self.name = vname
        self.id = id
        self.kind = vkind
        self.type = vtype

    def printout(self):
        print "VARIABLE {0}, {1}, {2}, {3}".format(self.id, self.name, self.kind, self.type)
    

class Stmt(object): 
    """ Top-level (abstract) class representing all statements"""

class IfStmt(Stmt):
    def __init__(self, condition, thenpart, elsepart, lines):
        self.lines = lines
        self.condition = condition
        self.thenpart = thenpart
        self.elsepart = elsepart

    def printout(self):
        print "If(",
        self.condition.printout()
        print ", ",
        self.thenpart.printout()
        print ", ",
        self.elsepart.printout()
        print ")"

class WhileStmt(Stmt):
    def __init__(self, cond, body, lines):
        self.lines = lines
        self.cond = cond
        self.body = body

    def printout(self):
        print "While(",
        self.cond.printout()
        print ", ",
        self.body.printout()
        print ")"

class ForStmt(Stmt):
    def __init__(self, init, cond, update, body, lines):
        self.lines = lines
        self.init = init
        self.cond = cond
        self.update = update
        self.body = body

    def printout(self):
        print "For(",
        if (self.init != None):
            self.init.printout()
        print ", ",
        if (self.cond != None):
            self.cond.printout()
        print ", ",
        if (self.update != None):
            self.update.printout()
        print ", ",
        self.body.printout()
        print ")"

class ReturnStmt(Stmt):
    def __init__(self, expr, lines):
        self.lines = lines
        self.expr = expr

    def printout(self):
        print "Return(",
        if (self.expr != None):
            self.expr.printout()
        print ")"

class BlockStmt(Stmt):
    def __init__(self, stmtlist, lines):
        self.lines = lines
        self.stmtlist = [s for s in stmtlist if (s != None) and (not isinstance(s, SkipStmt))]

    def printout(self):
        print "Block(["
        if (len(self.stmtlist) > 0):
            self.stmtlist[0].printout()
        for s in self.stmtlist[1:]:
            print ", ",
            s.printout()
        print "])"

class BreakStmt(Stmt):
    def __init__(self, lines):
        self.lines = lines

    def printout(self):
        print "Break"
        
class ContinueStmt(Stmt):
    def __init__(self, lines):
        self.lines = lines

    def printout(self):
        print "Continue"

class ExprStmt(Stmt):
    def __init__(self, expr, lines):
        self.lines = lines
        self.expr = expr

    def printout(self):
        print "Expr(",
        self.expr.printout()
        print ")"
        
class SkipStmt(Stmt):
    def __init__(self, lines):
        self.lines = lines

    def printout(self):
        print "Skip"
        

class Expr(object):
    def __repr__(self):
        return "Unknown expression"
    def printout(self):
        print self, 


class ConstantExpr(Expr):
    def __init__(self, kind, arg=None, lines=None):
        self.lines = lines
        self.kind = kind
        # True and False have type boolean.
        if(kind == 'True' or kind == 'False'):
            self.type = 'boolean'
        # Null has type null.
        elif(kind == 'Null'):
            self.type = 'null'
        # Rest is same as kind.
        else:
            self.type = kind
        if (kind=='int'):
            self.int = arg
        elif (kind == 'float'):
            self.float = arg
        elif (kind == 'string'):
            self.string = arg

            
    def __repr__(self):
        s = "Unknown"
        if (self.kind == 'int'):
            s = "Integer-constant(%d)"%self.int
        elif (self.kind == 'float'):
            s = "Float-constant(%g)"%self.float
        elif (self.kind == 'string'):
            s = "String-constant(%s)"%self.string
        elif (self.kind == 'Null'):
            s = "Null"
        elif (self.kind == 'True'):
            s = "True"
        elif (self.kind == 'False'):
            s = "False"
        return "Constant({0})".format(s)

# Type id not declared yet.
class VarExpr(Expr):
    def __init__(self, var, lines):
        self.lines = lines
        self.var = var
        self.type = self.var.type
    def __repr__(self):
        return "Variable(%d)"%self.var.id

# Type check complete for uminus and neg except field-access variable.
class UnaryExpr(Expr):
    def __init__(self, uop, expr, lines):
        self.lines = lines
        self.uop = uop
        self.arg = expr
        if uop == 'uminus':
            self.type = typecheck.eval_number(expr, lines)
        elif uop == 'neg':
            self.type = typecheck.eval_Boolean(expr, lines)
    def __repr__(self):
        return "Unary({0}, {1})".format(self.uop, self.arg)
        
class BinaryExpr(Expr):
    def __init__(self, bop, arg1, arg2, lines):
        self.lines = lines
        self.bop = bop
        self.arg1 = arg1
        self.arg2 = arg2
        #self.type = typecheck.eval_BinaryExpr(bop, arg1, arg2, lines)

    def __repr__(self):
        return "Binary({0}, {1}, {2})".format(self.bop,self.arg1,self.arg2)

class AssignExpr(Expr):
    def __init__(self, lhs, rhs, lines):
        self.lines = lines
        self.lhs = lhs
        self.rhs = rhs
    def __repr__(self):
        return "Assign({0}, {1})".format(self.lhs, self.rhs)
        
        
class AutoExpr(Expr):
    def __init__(self, arg, oper, when, lines):
        self.lines = lines
        self.arg = arg
        self.oper = oper
        self.when = when
    def __repr__(self):
        return "Auto({0}, {1}, {2})".format(self.arg, self.oper, self.when)
        
class FieldAccessExpr(Expr):
    def __init__(self, base, fname, lines):
        self.lines = lines
        self.base = base
        self.fname = fname
        c = lookup(classtable, 'f')
        print c
    def __repr__(self):
        return "Field-access({0}, {1})".format(self.base, self.fname)
        
class MethodInvocationExpr(Expr):
    def __init__(self, field, args, lines):
        self.lines = lines
        self.base = field.base
        self.mname = field.fname
        self.args = args
    def __repr__(self):
        return "Method-call({0}, {1}, {2})".format(self.base, self.mname, self.args)
        
class NewObjectExpr(Expr):
    def __init__(self, cref, args, lines):
        self.lines = lines
        self.classref = cref
        self.args = args
    def __repr__(self):
        return "New-object({0}, {1})".format(self.classref.name, self.args)

class ThisExpr(Expr):
    def __init__(self, lines):
        self.lines = lines
    def __repr__(self):
        return "This"
        
class SuperExpr(Expr):
    def __init__(self, lines):
        self.lines = lines
    def __repr__(self):
        return "Super"
        
class ClassReferenceExpr(Expr):
    def __init__(self, cref, lines):
        self.lines = lines
        self.classref = cref
    def __repr__(self):
        return "ClassReference({0})".format(self.classref.name)
        
class ArrayAccessExpr(Expr):
    def __init__(self, base, index, lines):
        self.lines = lines
        self.base = base
        self.index = index
    def __repr__(self):
        return "Array-access({0}, {1})".format(self.base, self.index)
        
class NewArrayExpr(Expr):
    def __init__(self, basetype, args, lines):
        self.lines = lines
        self.basetype = basetype
        self.args = args
    def __repr__(self):
        return "New-array({0}, {1})".format(self.basetype, self.args)

