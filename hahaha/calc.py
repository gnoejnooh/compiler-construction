import calclexer
import calcparser
while True:
    try:
        s = raw_input('calc > ') 
    except EOFError:
        break
    parser.parse(s)