"""CLI application for a prefix-notation calculator."""

from arithmetic import add



# Replace this with your code
while True:
    input_string = input("Please enter your equation > ")
    tokens = input_string.split(' ') 
    # tokens = ["+", "3", "6"] + 3 6
    if tokens[0] == 'q':
        print("Goodbye!")
        break
    elif tokens[0] == '+':
        if len(tokens) < 3:
            print("Please input 3 arguments: an operator and two numbers.")
            continue
        num1 = tokens[1]
        num2 = tokens[2]

        try: 
            num1 = int(num1)
        except:
            print("second argument is not a number!")
            continue
        try: 
            num2 = int(num2)
        except:
            print("third argument is not a number!")
            continue
        print(add(num1, num2))

        