import ast
import sys
import logging

tmpreg = []
argreg = []
controlstack = []
datastack = []
static_data_size = 0
static_data = []
classtable = {}
lastlabel = 0

def print_code(out, ct):
    global lastlabel
    global tmpreg, argreg, controlstack, datastack
    global static_data_size, static_data, classtable

    # File Output Source
    outfile = open(out, 'w')
    classtable = ct

    # Calculate static data size
    static_data_size = ast.lastfields
    
    outfile.write(".static_data %d\n" % static_data_size)
    outfile.write("top:\n")

    # Print all things in the classtable
    for keys,values in classtable.items():
        # Print out the label
        if values.builtin:
            print "Builitin class: %s" % keys
        else:
            if values.constructors:
                for constructor in values.constructors:
                    if constructor.body.lines == None:
                        print "Skip this constructor: %s" % constructor.name
                    else:
                        outfile.write("\nt%d:\n" % lastlabel)
                        lastlabel += 1
                        for stmt in constructor.body.stmtlist:
                            if stmt.type == "Skip":
                                print "Skip: %s" % stmt
                            elif stmt.type == "Block":
                                print "Block: %s" % stmt
                            elif stmt.type == "Expr":
                                l = "\t%s" % stmt.expr
                                outfile.write("%s\n"%l)
                                print l
                            elif stmt.type == "For":
                                print "For: %s" % stmt
                            elif stmt.type == "While":
                                print "While: %s" % stmt
                            elif stmt.type == "If":
                                print "If: %s" % stmt
                            elif stmt.type == "Continue":
                                print "Continue: %s" % stmt
                            elif stmt.type == "Break":
                                print "Break: %s" % stmt
                            elif stmt.type == "Return":
                                print "Return: %s" % stmt
                            else:
                                print "Else: %s" % stmt
                        outfile.write("\tret\n")

    outfile.write("\n__main__:\n")
    outfile.write("\tcall top\n")
    outfile.write("\tret")
