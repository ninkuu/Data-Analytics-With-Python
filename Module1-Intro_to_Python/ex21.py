def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"Subtracting {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"Multiplying {a} * {b}")
    return a * b

def divide(a, b):
    print(f"Dividing {a} / {b}")
    return a / b

print("Let's do some math with just functions!")

age = add (int(input(">")), float(input(">>")))
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

#a puzzle for extra credit, type it in anyway
print("Here is a puzzle:\n what = add(age, subtract(height, multiply(weight, divide(iq, 2))))\n Show your work.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print("That becomes: ", what, "can you do it by hand")

#experimenting
print("Writing a formulate for 24 + 34 / 100 - 1023. \n It looks like add(subtract(divide(34, 100), 2013), 24). \nShow your work")
experiment = add(subtract(divide(34, 100),2013), 24)
print(experiment)