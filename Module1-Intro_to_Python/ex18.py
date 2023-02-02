#This one is like your scripts with argv
def print_two(*arguments):
    arg1, arg2, arg3 = arguments
    print(f"arg1: {arg1}, arg2: {arg2}, arg3: {arg3}")
    
#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")
    
#this just takes one argument:
def print_one(arg1):
    print(f"arg1: {arg1}")
    
#this takes no arguments
def print_none():
    print("i got nothin'.")
    
print_two("Ninh", "Khuu", "L")
print_two_again("nin", "kuu")
print_one("ninh")
print_none()

'''Function Rules
1. Did you start your function defition with 'def'?
2. Does your function name have only characters and _ (underscore) characters?
3. Did you put an open parenthesis ( right after the function name?
4. Did you put your arguments after the parenthesis ( separated by commas?
5. Did you make each argument unique (meaning no duplicated names?)
6. Did you put a close parenthesis and a colon ) : after the arguments?
7. Did you indent all lines of code you want in the function four spaces? No more, no less. 
8. Did you "end" your function by going back to writing with no indent (dedenting we call it)?
'''