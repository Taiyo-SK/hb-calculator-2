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


# Replace this with your code
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

    
        