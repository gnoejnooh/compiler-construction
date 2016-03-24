class AST:
    pass

class PGM(AST):
    def __init__(self, class_decl):
        self.child = class_decl
    def __str__(self):
        return "%s" % self.child

class CLASS_DECL_LIST(AST):
    def __init__(self, class_decl, class_decl_list):
        self.lchild = class_decl
        self.rchild = class_decl_list
    def __str__(self):
        if(self.rchild == None):
            self.rchild = ""
        return "%s%s" % (self.lchild, self.rchild)

class CLASS_DECL(AST):
    Name = ""
    def __init__(self, className, superName, body):
        Name = className
        self.lchild = className
        self.mchild = superName
        self.rchild = body
        itr = self.rchild.lchild
        try:
            while itr:
                itr.lchild.rchild.child.class_name = className
                itr = itr.lchild
        except AttributeError:
                itr = itr
    def __str__(self):
        if(self.mchild == None):
            self.mchild = "Superclass:"
        if(self.rchild == None):
            self.rchild = ""
        #else:
        return "Class Name: %s\n%s\n%s\n" % (self.lchild, self.mchild, self.rchild)

class EXTENDS_ID(AST):
    def __init__(self, extendID):
        self.child = extendID
    def __str__(self):
        return "Superclass Name: %s" % (self.child)

class CLASS_BODY_DECL_LIST(AST):
    def __init__(self, class_body_decl_list, class_body_decl):
        self.lchild = class_body_decl_list
        self.rchild = class_body_decl
    def __str__(self):
        if(self.lchild == None):
            self.lchild = ""
        if(self.rchild == None):
            self.rchild = ""
        return "%s%s" % (self.lchild, self.rchild)

class CLASS_BODY_DECL_FIELD(AST):
    def __init__(self, field_decl):
        self.child = field_decl
    def __str__(self):
        if(self.child == None):
            return ""
        return "Fields:\n%s" % self.child

class CLASS_BODY_DECL_METHOD(AST):
    def __init__(self, method_decl):
        self.child = method_decl
    def __str__(self):
        if(self.child == None):
            return ""
        return "Method:\n%s" % self.child

class CLASS_BODY_DECL_CONSTRUCTOR(AST):
    def __init__(self, constructor_decl):
        self.child = constructor_decl
    def __str__(self):
        if(self.child == None):
            return ""
        return "Constructor:\n%s" % self.child

class FIELD_DECL(AST):
    def __init__(self, count, mod, var_decl):
        self.count = count
        self.class_name = None
        self.lchild = mod
        self.rchild = var_decl
    def __str__(self):
        return "FIELD %d, %s, %s, %s%s\n" % (self.count, self.class_name, self.rchild.rchild, self.lchild, self.rchild.lchild)

class METHOD_DECL(AST):
    def __init__(self, count, mod, type, ID, param, block):
        self.count = count
        self.llchild = mod
        self.lchild = type
        self.mchild = ID
        self.rchild = param
        self.rrchild = block
    def __str__(self):
        return """METHOD: %d, %s, %s%s
Method Parameters: %s
Variable Table:
Method Body: %s\n""" % (self.count, self.mchild, self.llchild, self.lchild, self.rchild, self.rrchild)

class CONSTRUCTOR_DECL(AST):
    def __init__(self, num, mod, param, block):
        self.number = num
        self.lchild = mod.lchild
        self.mchild = param
        self.rchild = block
    def __str__(self):
        if(self.mchild == None):
            self.mchild = ""
        if(self.rchild == None):
            self.rchild = ""
        str = """CONSTRUCTOR: %d, %s
Constructor Parameters: %s
Constructor Body: %s\n""" % (self.number, self.lchild, self.mchild, self.rchild)
        return str

class MOD(AST):
    def __init__(self, visibility_mod, storage_mod):
        self.lchild = visibility_mod
        self.rchild = storage_mod
    def __str__(self):
        return "%s, %s, " % (self.lchild, self.rchild)

class VISIBILITY_MOD(AST):
    def __init__(self, mod):
        self.child = mod
    def __str__(self):
        if(self.child == None):
            self.child = "private"
        return "%s" % self.child

class STORAGE_MOD(AST):
    def __init__(self, mod):
        self.child = mod
    def __str__(self):
        if(self.child == None):
            self.child = "instance"
        return "%s" % self.child

class VAR_DECL(AST):
    def __init__(self, type, var_list):
        self.lchild = type
        self.rchild = var_list
    def __str__(self):
        if(self.rchild == None):
            return "%s" % self.lchild
        return "%s, %s" % (self.lchild, self.rchild)

class TYPE(AST):
    def __init__(self, type):
        self.child = type
    def __str__(self):
        if(self.child != "int" and self.child != "boolean" and self.child != "float"):
            self.child = "user(" + self.child + ")"
        return "%s" % self.child

class VAR_LIST(AST):
    def __init__(self, var_list, var):
        self.lchild = var_list
        self.rchild = var
    def __str__(self):
        if(self.lchild == None):
            self.lchild = ""
        return "%s%s" % (self.lchild, self.rchild)

class VAR(AST):
    def __init__(self, var):
        self.child = var
    def __str__(self):
        return "%s" % self.child

class PARAM_LIST_OPT(AST):
    def __init__(self, param_list):
        self.child = param_list
    def __str__(self):
        return "%s" % self.child

class PARAM_LIST(AST):
    def __init__(self, param_list, param):
        self.lchild = param_list
        self.rchild = param
    def __str__(self):
        if self.lchild == None:
            self.lchild = ""
        if self.rchild == None:
            self.rchild = ""
        return "%s%s" % (self.lchild, self.rchild)

class PARAM(AST):
    def __init__(self, type, ID):
        self.lchild = type
        self.rchild = ID
    def __str__(self):
        return "%s %s" % (self.lchild, self.rchild)

class BLOCK(AST):
    def __init__(self, stmt_list):
        self.child = stmt_list
    def __str__(self):
        return "\nBlock([\n%s\n])" % self.child

class STMT_LIST(AST):
    def __init__(self, stmt_list, stmt):
        self.lchild = stmt_list
        self.rchild = stmt
    def __str__(self):
        if self.lchild == None:
            self.lchild = ""
        if self.rchild == None:
            self.rchild = ""
        return "%s%s" % (self.lchild, self.rchild)

class STMT_IF(AST):
    def __init__(self, IF, expr, ifStmt, ELSE, elseStmt):
        self.llchild = IF
        self.lchild = expr
        self.mchild = ifStmt
        self.rchild = ELSE
        self.rrchild = elseStmt
    def __str__(self):
        if self.rchild == None:
            self.rchild = self.rrchild = ""
        else:
            self.rchild = ", " + self.rchild
            self.rrchild = ", " + self.rrchild
        return "%s(%s), %s%s%s)" % (self.llchild, self.lchild, self.mchild, self.rchild, self.rrchild)

class STMT_WHILE(AST):
    def __init__(self, WHILE, expr, stmt):
        self.lchild = WHILE
        self.mchild = expr
        self.rchild = stmt
    def __str__(self):
        return "%s(%s), %s" % (self.lchild, self.mchild, self.rchild)

class STMT_FOR(AST):
    def __init__(self, FOR, stmt_expr_opt, expr_opt, opt, stmt):
        self.llchild = FOR
        self.lchild = stmt_expr_opt
        self.mchild = expr_opt
        self.rchild = opt
        self.rrchild = stmt
    def __str__(self):
        return "%s(%s, %s, %s), %s" % (self.llchild, self,lchild, self.mchild, self.rchild, self.rrchild)

class STMT_RETURN(AST):
    def __init__(self, RETURN, expr_opt):
        self.lchild = RETURN
        self.rchild = expr_opt
    def __str__(self):
        return "%s(%s)" % (self.lchild, self.rchild)

class STMT_STMT_EXPR(AST):
    def __init__(self, expr):
        self.child = expr
    def __str__(self):
        return "%s" % self.child

class STMT_BREAK(AST):
    def __init__(self, BREAK):
        self.child = BREAK
    def __str__(self):
        return "%s" % self.child

class STMT_CONTINUE(AST):
    def __init__(self, CONTINUE):
        self.child = CONTINUE
    def __str__(self):
        return "%s" % self.child

class STMT_BLOCK(AST):
    def __init__(self, block):
        self.child = block
    def __str__(self):
        return "%s" % self.child

class STMT_VAR_DECL(AST):
    def __init__(self, var_decl):
        self.child = var_decl
    def __str__(self):
        return "%s" % self.child

class LITERAL_INT_CONST(AST):
    def __init__(self, int_const):
        self.child = int_const
    def __str__(self):
        return "Constant(Integer-constant(%s))" % self.child

class LITERAL_FLOAT_CONST(AST):
    def __init__(self, float_const):
        self.child = float_const
    def __str__(self):
        return "Constant(Float-constant(%s))" % self.child

class LITERAL_STRING_CONST(AST):
    def __init__(self, string_const):
        self.child = string_const
    def __str__(self):
        return "Constant(String-constant(%s))" % self.child

class LITERAL_NULL(AST):
    def __init__(self, NULL):
        self.child = NULL
    def __str__(self):
        return "%s" % self.child

class LITERAL_TRUE(AST):
    def __init__(self, TRUE):
        self.child = TRUE
    def __str__(self):
        return "%s" % self.child

class LITERAL_FALSE(AST):
    def __init__(self, FALSE):
        self.child = FALSE
    def __str__(self):
        return "%s" % self.child        

class PRIMARY_LITERAL(AST):
    def __init__(self, primary):
        self.child = primary
    def __str__(self):
        return "%s" % self.child

class PRIMARY_THIS(AST):
    def __init__(self, primary):
        self.child = primary
    def __str__(self):
        return "%s" % self.child

class PRIMARY_SUPER(AST):
    def __init__(self, primary):
        self.child = primary
    def __str__(self):
        return "%s" % self.child

class PRIMARY_NEWOBJ(AST):
    def __init__(self, ID, args_opt):
        self.lchild = ID
        self.rchild = args_opt
    def __str__(self):
        if self.rchild == None:
            self.rchild = ""
        return "New-object(%s, [%s])" % (self.lchild, self.rchild)

class PRIMARY_LHS(AST):
    def __init__(self, lhs):
        self.child = lhs
    def __str__(self):
        return "%s" % self.child

class PRIMARY_METHOD_INVOCATION(AST):
    def __init__(self, method):
        self.child = method
    def __str__(self):
        return "%s" % self.child

class ARGS_OPT(AST):
    def __init__(self, args_opt):
        self.child = args_opt
    def __str__(self):
        return "%s" % self.child

class ARGS_PLUS(AST):
    def __init__(self, arg_plus, expr):
        self.lchild = arg_plus
        self.rchild = expr
    def __str__(self):
        if self.lchild == None:
            self.lchild = ""
        return "%s%s" % (self.lchild, self.rchild)

class LHS(AST):
    def __init__(self, lhs):
        self.child = lhs
    def __str__(self):
        return "%s" % self.child

class FIELD_ACCESS(AST):
    def __init__(self, primary, ID):
        self.lchild = primary
        self.rchild = ID
    def __str__(self):
        if self.lchild == None:
            self.lchild = "this"
        return "Field-access(%s, %s)" % (self.lchild, self.rchild)

class ARRAY_ACCESS(AST):
    def __init__(self, primary, expr):
        self.lchild = primary
        self.rchild = expr
    def __str__(self):
        return "Array-access(%s, %s)" % (self.lchild, self.rchild)

class METHOD_INVOCATION(AST):
    def __init__(self, field_access, args_opt):
        self.lchild = field_access.lchild
        self.mchild = field_access.rchild
        self.rchild = args_opt
    def __str__(self):
        return "Method-call(%s, %s, %s)" % (self.lchild, self.mchild, self.rchild)

class EXPR_BASIC(AST):
    def __init__(self, basic):
        self.child = basic
    def __str__(self):
        return "Expr( %s )" % self.child

class EXPR_BINOP(AST):
    def __init__(self, expr_prev, op, expr_next):
        self.lchild = expr_prev
        self.mchild = op
        self.rchild = expr_next
    def __str__(self):
        # binary conversion
        if self.mchild == "+":
            self.mchild = "add"
        elif self.mchild == "-":
            self.mchild = "sub"
        elif self.mchild == "*":
            self.mchild = "mul"
        elif self.mchild == "/":
            self.mchild = "div"
        elif self.mchild == "&&":
            self.mchild = "and"
        elif self.mchild == "\|\|":
            self.mchild = "or"
        elif self.mchild == "==":
            self.mchild = "eq"
        elif self.mchild == "!=":
            self.mchild = "neq"
        elif self.mchild == "<":
            self.mchild = "le"
        elif self.mchild == "<=":
            self.mchild = "leq"
        elif self.mchild == ">":
            self.mchild = "gt"
        elif self.mchild == ">=":
            self.mchild = "geq"
        else:
            self.mchild = None
        return "Binary(%s, %s, %s)" % (self.mchild, self.lchild, self.rchild)

class EXPR_UNOP(AST):
    def __init__(self, op, expr):
        self.lchild = op
        self.rchild = expr
    def __str__(self):
        if self.lchild == '+':
            self.lchild = ""
        if self.lchild == '!':
            pass
        return "%s%s" % (self.lchild, self.rchild)

class ASSIGN_EQUALS(AST):
    def __init__(self, lhs, expr):
        self.lchild = lhs
        self.rchild = expr
    def __str__(self):
        return "Assign(%s, %s)" % (self.lchild, self.rchild)

class ASSIGN_POST_INC(AST):
    def __init__(self, lhs):
        self.child = lhs
    def __str__(self):
        return "Auto(%s, inc, post)" % self.child

class ASSIGN_PRE_INC(AST):
    def __init__(self, lhs):
        self.child = lhs
    def __str__(self):
        return "Auto(%s, inc, pre)" % self.child

class ASSIGN_POST_DEC(AST):
    def __init__(self, lhs):
        self.child = lhs
    def __str__(self):
        return "Auto(%s, dec, post)" % self.child

class ASSIGN_PRE_DEC(AST):
    def __init__(self, lhs):
        self.child = lhs
    def __str__(self):
        return "Auto(%s, dec, pre)" % self.child

class STMT_EXPR(AST):
    def __init__(self, expr):
        self.child = expr
    def __str__(self):
        if self.child == None:
            self.child = ""
        return "%s" % (self.child)

class STMT_EXPR_OPT(AST):
    def __init__(self, stmt_expr):
        self.child = stmt_expr
    def __str__(self):
        if self.child == None:
            self.child = ""
        return "%s" % (self.child)

class EXPR_OPT(AST):
    def __init__(self, expr):
        self.child = expr
    def __str__(self):
        if self.child == None:
            self.child = ""
        return "%s" % (self.child)