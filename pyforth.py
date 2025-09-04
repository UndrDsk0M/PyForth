

source = ["\ Calculate ( (5 3 + 2 * 10 mod) dup swap 1000 + . )",
"5 3 + 2 * 10 mod dup swap 1000 + .",
"\ Now test stack manipulation",
"10 20 30 dup swap over + . drop",
"\ Nested arithmetic and stack ops",
"100 5 mod 3 * 2 + dup . swap 50 - .",
"\ Edge case: underflow",
"drop drop drop drop",]

def load_file(filename):
    global source
    with open(filename, 'r') as f:
        source = f.readlines()
        print("Loaded file:", source)
    return source


stack = []

def tokenize(source):
    source += ' '
    token = source.split()
    return token

def interpret(tokens):
    global stack
    global is_comment
    is_comment = False
    for t in tokens:
        try :
            if not is_comment : 
                match t.lower():
                    
                    case t if t.strip().isdigit():
                        stack.append(int(t))

                    case t if t.startswith("\\"):
                        is_comment = True

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
                    case 'drop':
                        stack.pop()     
                    case 'over':
                        a = stack.pop()
                        b = stack.pop()
                        stack.append(b)
                        stack.append(a)
                        stack.append(b)
                    case 'clear':
                        stack = []
                    case 'stack':
                        print(stack)
                    case 'bye':
                        exit(0)
                    case 'help':
                        print("Available commands: + - * mod dup swap drop over clear stack bye help")
                    
                    case _ :
                        if t != "\n" and not is_comment:
                            raise ValueError(f"Unknown token: {t}")
                        elif t == "\n":
                            is_comment = False

        except IndexError:
            raise IndexError("Error: Stack underflow")
            
        

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        load_file(sys.argv[1])
    for line in source:
        is_comment = False
        tokens = tokenize(line)
        try :
            interpret(tokens)
        except Exception as e:
            print(stack)
            print(e)