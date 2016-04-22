import ast
import sys
import logging

tmpreg = []
argreg = []
controlstack = []
datastack = []
static_data_size = 0
staticdata = {}
classtable = {}
lastlabel = 0

def find_static_var(classname, varname):
    for keys,values in staticdata.items():
        if values.inclass.name is classname and values.name is varname:
            print "STATIC %s (%s.%s)" % (keys, values.inclass.name, values.name)
            return values
    print "Not found"
    return None

def print_code(out, ct):
    global lastlabel
    global static_data_size, staticdata, classtable

    # File Output Source
    outfile = open(out, 'w')
    classtable = ct
    static_data_size = ast.static_data_size
    staticdata = ast.staticdata

    outfile.write(".static_data %d\n" % static_data_size)
    outfile.write("top:\n")

    # Print all things in the classtable
    for keys,values in classtable.items():
        # Print out the label
        if values.builtin:
            continue
        else:
            if values.constructors:
                for constructor in values.constructors:
                    generate_code(constructor.body, outfile)
            if values.methods:
                for method in values.methods:
                    print method.name
                    generate_code(method.body, outfile)


    outfile.write("\n__main__:\n")
    outfile.write("\tcall top\n")
    outfile.write("\tret")
    return None

def generate_code(body, outfile):
    global lastlabel

    if body.lines != None:
        outfile.write("\nC%d:\n" % lastlabel)
        lastlabel += 1
        for stmt in body.stmtlist:
            if stmt.type == "Skip":
                print "Skip: %s" % stmt
            elif stmt.type == "Block":
                print "Block: %s" % stmt
            elif stmt.type == "Expr":
                l = "\t%s" % stmt.expr.codegen()
                outfile.write("%s\n"%l)
                print l
            elif stmt.type == "For":
                print "For: %s" % stmt
            elif stmt.type == "While":
                print "While: %s" % stmt
            elif stmt.type == "If":
                print "If: %s" % stmt.codegen()
            elif stmt.type == "Continue":
                print "Continue: %s" % stmt
            elif stmt.type == "Break":
                print "Break: %s" % stmt
            elif stmt.type == "Return":
                print "Return: %s" % stmt
            else:
                print "Else: %s" % stmt
        outfile.write("\tret\n")
    return None
