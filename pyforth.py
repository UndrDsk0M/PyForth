from random import shuffle

source = ["\ Calculate ( (5 3 + 2 * 10 mod) dup swap 1000 + . )",
"5 3 + 2 * 10 mod dup swap 1000 + .",
"\ Now test stack manipulation",
"10 20 30 dup swap over + . drop",
"\ Nested arithmetic and stack ops",
"100 5 mod 3 * 2 + dup . swap 50 - .",
"\ Edge case: underflow",
"drop drop drop drop",]

def __load_file__(filename):
    global source
    with open(filename, 'r') as f:
        source = f.readlines()
    return source

def __is_int__(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

stack = []

def tokenize(source):
    source += ' '
    token = source.split()
    return token

def interpret(tokens):
    global stack
    isword = False
    is_comment = False
    matched = True 
    for t in tokens:
        try :
            if not is_comment : 
                match t.lower():

                    case ':':
                        isword = True

                    # handling int
                    case t if __is_int__(t):
                        stack.append(int(t))

                    # comments
                    case t if t.startswith("\\"):
                        is_comment = True

                    # intiger words
                    case '.':
                        print(stack.pop())
                        
                    case '+':
                        b = stack.pop()
                        a = stack.pop()
                        stack.append(a + b)
                    case '-':
                        b = stack.pop()
                        a = stack.pop()
                        stack.append(a - b)
                    case '*':
                        b = stack.pop()
                        a = stack.pop()
                        stack.append(a * b)
                    case 'mod':
                        b = stack.pop()
                        a = stack.pop()
                        stack.append(a // b)
                    case 'dup':
                        a = stack.pop()
                        stack.append(a)
                        stack.append(a)
                    case 'swap':
                        a = stack.pop()
                        b = stack.pop()
                        stack.append(a)
                        stack.append(b)
                    case 'rot':
                        a = stack.pop()
                        b = stack.pop()
                        c = stack.pop()
                        stack.append(b)
                        stack.append(a)
                        stack.append(c)
                    case 'drop':
                        stack.pop()    
                    case 'nip':
                        a = stack.pop()
                        b = stack.pop()
                        stack.append(a) 
                    case 'over':
                        a = stack.pop()
                        b = stack.pop()
                        stack.append(b)
                        stack.append(a)
                        stack.append(b)
                    case 'tuck':
                        a = stack.pop()
                        b = stack.pop()
                        stack.append(a)
                        stack.append(b)
                        stack.append(a)
                    case 'negate':
                        a = stack.pop()
                        stack.append(-a)
                    case 'abs':
                        a = stack.pop()
                        stack.append(abs(a))
                    case 'min':
                        b = stack.pop()
                        a = stack.pop()
                        stack.append(min(a, b))
                    case 'max':
                        b = stack.pop()
                        a = stack.pop()
                        stack.append(max(a, b))
                    case 'shuffle':
                        shuffle(stack)
                    case 'reverse':
                        stack.reverse()
                    case 'count':
                        stack.append(len(stack))
                    case 'sum':
                        stack.append(sum(stack))
                    case 'mean':
                        stack.append(sum(stack) // len(stack))
                    case 'minmax':
                        stack.append(min(stack))
                        stack.append(max(stack))
                    case 'sort':
                        stack = sorted(stack)
                    
                    # coditions 
                    case '=':
                        b = stack.pop()
                        a = stack.pop()
                        stack.append(int(a == b))
                    case '<':
                        b = stack.pop()
                        a = stack.pop()
                        stack.append(int(a < b))
                    case '>':
                        b = stack.pop()
                        a = stack.pop()
                        stack.append(int(a > b))
                    case '<=':
                        b = stack.pop()
                        a = stack.pop()
                        stack.append(int(a <= b))
                    case '>=':
                        b = stack.pop()
                        a = stack.pop()
                        stack.append(int(a >= b))
                    
                    
                        
                        

 
                    case t if t in ('clearstack', 'clear'):
                        stack = []
                    case 'stack':
                        print(stack)
                    case 'bye':
                        exit(0)
                    case t if t in ('help', 'h', '?', 'words', 'commands'):
                        print("Available commands: + - * mod dup swap drop over clear stack bye help negate abs min max shuffle reverse count sum mean minmax sort")
                    case 'page':
                        print("\033c", end="")
                        matched = False

                    case 'newwordl':
                        print("New added words: shuffle, reverse, count, sum, mean, minmax, sort, help, ")
                    case _ :
                        matched = False
                        if t != "\n" and not is_comment:
                            raise ValueError(f"Unknown token: {t}")
                        elif t == "\n":
                            is_comment = False
                if matched:
                    print(f"Stack<{[x for x in stack]}>", "ok" )
                    matched = False


        except IndexError:
            raise IndexError("Error: Stack underflow")
            
        

def __run__(line):
    tokens = tokenize(line)
    try :
        interpret(tokens)
    except Exception as e:
        print(">>> ", stack)
        print(e)


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        if sys.argv[1] == '--help' or sys.argv[1] == '-h':
            print("Usage: python pyforth.py [source_file]")
            print("If no source_file is provided, a default commend line forth will be run.")
            exit(0)

        __load_file__(sys.argv[1])
        for line in source:
            __run__(line)
        exit(0)

    print("Welcome to PyForth 0.0.8! Type 'help' for a list of commands and 'newwordl' to see new added words.\nPyForth is available in GitHub and PyPi and you can get the lastest verstion in this (link)[https://github.com/UndrDsk0M/PyForth] \nType 'bye' to exit.")
    while True:
        input_code = input()
        __run__(input_code)