import ast
import sys
import logging

# reg: All Registers
# regAvailable: Available Registers
# regUsed: Used Registers (Not available)
reg = []
regAvailable = []
regUsed = []
static_data_size = 0
static_data = []
classtable = {}
lastlabel = 0

def print_code(out, ct, ss):
    global lastlabel, reg, regAvailable, regUsed
    global static_data_size, static_data, classtable
    static_data_size = ss

    # File Output Source
    outfile = open(out, 'w')
    classtable = ct

    outfile.write(".static_data %d\n" % static_data_size)
    outfile.write("top:\n")

    # Print all things in the classtable
    for keys,values in classtable.items():
        # Print out the label
        if values.builtin:
            print "Builitin class: %s" % keys
        else:
            outfile.write("\nt%d:\n" % lastlabel)
            lastlabel += 1
            outfile.write("\tret\n")
        # Print the values

    outfile.write("\n__main__:\n")
    outfile.write("\tcall top\n")
    outfile.write("\tret")
