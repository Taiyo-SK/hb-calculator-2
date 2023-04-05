"""CLI application for a prefix-notation calculator."""

from arithmetic import add, subtract, multiply, divide, square, cube, power, mod

def validate_three_args(tokens):
    if len(tokens) < 3:
        print("Please input 3 arguments: an operator and two numbers.")
        return False
    num1 = tokens[1]
    num2 = tokens[2]
    try: 
        num1 = float(num1)
    except:
        print("second argument is not a number!")
        return False
    try: 
        num2 = float(num2)
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
        num1 = float(num1)
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
        print(round(add(float(tokens[1]), float(tokens[2])), 2))

    elif tokens[0] == '-':
        if validate_three_args(tokens) == False:
            continue 
        print(round(subtract(float(tokens[1]), float(tokens[2])), 2))

    elif tokens[0] == '*':    
        if validate_three_args(tokens) == False:
            continue 
        print(round(multiply(float(tokens[1]), float(tokens[2])), 2))

    elif tokens[0] == '/':    
        if validate_three_args(tokens) == False:
            continue 
        if int(tokens[2]) == 0:
            print("can not divide by zero!")
            continue
        print(round(divide(float(tokens[1]), float(tokens[2])), 2))

    elif tokens[0] == 'square':
        if validate_two_args(tokens) == False:
            continue
        print(round(square(float(tokens[1])), 2))
    
    elif tokens[0] == 'cube':
        if validate_two_args(tokens) == False:
            continue
        print(round(cube(float(tokens[1])), 2))
        
    elif tokens[0] == 'pow':
        if validate_three_args(tokens) == False:
            continue
        print(round(power(float(tokens[1]), float(tokens[2])), 2))

    elif tokens[0] == 'mod':    
        if validate_three_args(tokens) == False:
            continue 
        if int(tokens[2]) == 0:
            print("can not divide by zero!")
            continue
        print(round(mod(float(tokens[1]), float(tokens[2])), 2))

    else:
        print("wrong operation!")