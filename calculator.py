"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
def main():
    while True:
        user_input = raw_input("> ")
        tokens = user_input.split()
        try:
            if tokens[0] == 'q':
                quit()
            elif tokens[0] == '+':
                print add(int(tokens[1]), int(tokens[2]))
            elif tokens[0] == '-':
                print subtract(int(tokens[1]), int(tokens[2]))
            elif tokens[0] == '*':
                print multiply(int(tokens[1]), int(tokens[2]))
            elif tokens[0] == '/':
                print divide(int(tokens[1]), int(tokens[2]))
            elif tokens[0] == 'square':
                print square(int(tokens[1]))
            elif tokens[0] == 'cube':
                print cube(int(tokens[1]))
            elif tokens[0] == 'pow' or tokens[0] == '**' or tokens[0] == 'exp':
                print power(int(tokens[1]), int(tokens[2]))
            elif tokens[0] == 'mod' or tokens[0] == '%':
                print mod(int(tokens[1]), int(tokens[2]))
            else:
                print "I don't understand"
        except:
            print "This doesn't work"        

if __name__ == '__main__':
    main()
