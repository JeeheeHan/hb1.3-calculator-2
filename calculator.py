"""CLI application for a prefix-notation calculator."""

from arithmetic import *

#while loop that is forever - true bool
    #get an input 
    #tokenize input
    # if statements on quiting the while loop
        #break
    #else: continue with the math equations 
        #continue

    #if statements matching math functions

while True: 
    user_input = input("What is your equation?(type 'q' to exit) > ")
    token = user_input.rstrip().split(' ')
    

    if token[0] is "q":
        break
    elif len(token) < 2:
        print ("Not enough arguments")
        continue

    math_symbol = token[0]
    num1 = float(token[1])

    if len(token)  == 2:
        if math_symbol == "*":
            print(square(num1))
        elif math_symbol == "**":
            print(cube(num1))
       
    elif len(token) == 3:
        num2 = float(token[2])
        if math_symbol == "+":
            print (add(num1, num2))
        elif math_symbol == "-":
            print(subtract(num1,num2))
        elif math_symbol == "*":
            print(multiply(num1,num2))
        elif math_symbol == "/":
            print(divide(num1,num2))
        elif math_symbol == "**":
            print(power(num1,num2))
        elif math_symbol == "%":
            print(mod(num1,num2))
        elif math_symbol == "+**3":
            print(add_cubes(num1, num2))

    elif len(token) == 4:
        num3 = float(token[2])
        if math_symbol == "+*":
            print(add_multi(num1, num2, num3))
    else:
        print("Too many arguments")
        continue




