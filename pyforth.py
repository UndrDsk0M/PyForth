

source = "2 3 + 2 - ."

def load_file(filename):
    global source
    with open(filename, 'r') as f:
        source = f.read()
        print("Loaded file:", source)
    return source


stack = []

def tokenize(source):
    source += ' '
    token = source.split()
    return token

def interpret(tokens):
    global stack
    is_comment = False
    for t in tokens:
        try :
            if t.strip().isdigit():
                stack.append(int(t))

            elif t.startswith('\\'):
                is_comment = True
                continue

            match t.lower():

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
                    else :
                        is_comment = False

        except IndexError:
            raise IndexError("Error: Stack underflow")
            
        

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        load_file(sys.argv[1])
    tokens = tokenize(source)
    print("Tokens:", repr(tokens))
    try :
        interpret(tokens)
    except Exception as e:
        print(e)