"""CLI application for a prefix-notation calculator."""

from arithmetic import add, subtract, multiply, divide, square, cube, power, mod

def validate_three_args(tokens):
    if len(tokens) < 3:
        print("Please input 3 arguments: an operator and two numbers.")
        return False
    num1 = tokens[1]
    num2 = tokens[2]
    try: 
        num1 = int(num1)
    except:
        print("second argument is not a number!")
        return False
    try: 
        num2 = int(num2)
    except:
        print("third argument is not a number!")
        return False
    return True

def validate_two_args(tokens):
    if len(tokens) < 2:
        print("Please input 2 arguments: an operator and a number.")
        return False
    num1 = tokens[1]
    try:
        num1 = int(num1)
    except:
        print("first argument is not a number!")
        return False
    return True

while True:
    input_string = input("Please enter your equation > ")
    tokens = input_string.split(' ') 
    
    if tokens[0] == 'q':
        print("Goodbye!")
        break
    elif tokens[0] == '+':
        if validate_three_args(tokens) == False:
            continue 
        print(add(int(tokens[1]), int(tokens[2])))

    elif tokens[0] == '-':
        if validate_three_args(tokens) == False:
            continue 
        print(subtract(int(tokens[1]), int(tokens[2])))

    elif tokens[0] == '*':    
        if validate_three_args(tokens) == False:
            continue 
        print(multiply(int(tokens[1]), int(tokens[2])))

    elif tokens[0] == '/':    
        if validate_three_args(tokens) == False:
            continue 
        if int(tokens[2]) == 0:
            print("can not divide by zero!")
            continue
        print(round(divide(int(tokens[1]), int(tokens[2])), 2))

    elif tokens[0] == 'square':
        if validate_two_args(tokens) == False:
            continue
        print(square(int(tokens[1])))
    
    elif tokens[0] == 'cube':
        if validate_two_args(tokens) == False:
            continue
        print(cube(int(tokens[1])))
        
    elif tokens[0] == 'pow':
        if validate_three_args(tokens) == False:
            continue
        print(power(int(tokens[1]), int(tokens[2])))

    elif tokens[0] == 'mod':    
        if validate_three_args(tokens) == False:
            continue 
        if int(tokens[2]) == 0:
            print("can not divide by zero!")
            continue
        print(mod(int(tokens[1]), int(tokens[2])))

    else:
        print("wrong operation!")