"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


def file_to_print(in_filename):
    with open(in_filename) as incoming_file:
        for line in incoming_file:
            print line.strip(), "=", calculate_from_line(line)


def file_to_file(in_filename, out_filename):
    incoming_file = open(in_filename)
    outgoing_file = open(out_filename, "w")
    for line in incoming_file:
        equation = line.strip() + " = " + str(calculate_from_line(line)) + "\n"
        outgoing_file.write(equation)

    incoming_file.close()
    outgoing_file.close()


def calculate_from_line(line):
    tokens = line.split()
    if tokens[0] == 'q':
        return 'quit'
    try:
        numbers = map(int, tokens[1:])
    except:
        print "I need integers here"

    if tokens[0] == '+':
        return reduce(add, numbers)
    elif tokens[0] == '-':
        return reduce(subtract, numbers)
    elif tokens[0] == '*':
        return reduce(multiply, numbers)
    elif tokens[0] == '/':
        return reduce(divide, numbers)
    elif tokens[0] == 'square':
        return square(numbers[0])
    elif tokens[0] == 'cube':
        return cube(numbers[0])
    elif tokens[0] == 'pow' or tokens[0] == '**' or tokens[0] == 'exp':
        return reduce(power, numbers)
    elif tokens[0] == 'mod' or tokens[0] == '%':
        return reduce(mod, numbers)
    else:
        return "I don't understand this input"


# Your code goes here
# def main():
#     while True:
#         user_input = raw_input("> ")
#         if calculate_from_line(user_input) == 'quit':
#             break
#         print calculate_from_line(user_input)

if __name__ == '__main__':
    while True:
        user_input = raw_input("> ")
        if calculate_from_line(user_input) == 'quit':
            break
        print calculate_from_line(user_input)