"""
See small problem page for description.

P:
Execute a given string of instructions based on the rules of our mini stack-and-register based programming language.

Rules:
    - There is a stack and register
    - A digit represents the new value of the register
    - PUSH represents adding the current register to the stack
    - ADD represents removing the last value added to the stack and adding it to the register, storing the result in the register
    - SUB represents removing the last value added to the stack and subtracting it from the register, storing the result in the register
    - MULT represents removing the last value added to the stack and multiplying it by the register, storing the result in the register
    - DIV represents removing the last value added to the stack and dividing the register value by the popped value, storing 
      the integer result in the register
    - REMAINDER represents removing the last value added to the stack and dividing the register by the popped value, storing 
      the integer remainder in the register
    - POP represents removing the last value added to the stack and placing it in the register
    - PRINT represents printing the value of the register
    - The register is initialized to 0 while the stack is initialized to an empty list

D:
    - Input: String
    - Output: Integer, prints to console only when we see PRINT
    - Intermediary
        - List: Store the commands from the input string, as well as for the stack itself

High level strategies:
    - For each command in the input string, we'll alter the stack and register. Print to console when we're directed to.        

A:
    - Create an empty list called 'stack'
    - Assign a variable 'register' to 0
    - Create a list 'commands' by splitting apart the input string
    - For each 'command' in 'commands'
        - Execute the required steps, as per the command given

Helper: Execute the required steps per command
Input: String, stack, register
Output: Stack, register, potential print to console
Algorithm:
    - [Based on extensive rules above]


"""

def execute_command(command, stack, register):
    match command:
        case "PUSH":
            stack.append(register)
        case "ADD":
            register += stack.pop()
        case "SUB":
            register -= stack.pop()
        case "MULT":
            register *= stack.pop()
        case "DIV":
            register = register // stack.pop()
        case "REMAINDER":
            register = register % stack.pop()
        case "POP":
            register = stack.pop()
        case "PRINT":
            print(register)
        case _:
            register = int(command)
    
    return stack, register

def minilang(instructions):
    stack = []
    register = 0
    commands = instructions.split()
    for command in commands:
        stack, register = execute_command(command, stack, register)


# Test cases
minilang('PRINT')
# 0

minilang('5 PUSH 3 MULT PRINT')
# 15

minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
# 5
# 3
# 8

minilang('5 PUSH POP PRINT')
# 5

minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
# 5
# 10
# 4
# 7

minilang('3 PUSH PUSH 7 DIV MULT PRINT')
# 6

minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
# 12

minilang('-3 PUSH 5 SUB PRINT')
# 8

minilang('6 PUSH')
# (nothing is printed)

