"""  Your name here
     Program #2: The rigonometric functions calculator
     COSC 1306
     Spring 2021
"""


from math import pi

# Define the factorial function here

def factorial(integer):
    factorialSum = 1
    for i in range(1, integer + 1):
        factorialSum *= i
    return factorialSum

#degree to radians
def degTorad(degrees):
     radians = (degrees * pi) / 180
     return radians

# Define the sin function
def sinFunc(radians, terms):
    sinSum = (-1 ** terms) * (radians ** (2 * terms + 1) /factorial(integer = 2 * terms + 1))
    return sinSum

# Define the cos function
def cosFunc(radians, terms):
    cosineSum = (-1 ** terms) * (radians ** (2 * terms)/factorial(integer = 2 * terms))
    return cosineSum

# menu function
def printMenu():
    print("THE TRIGONOMETRIC CALCULATOR") 
    print("1 - Calculate the sine of a value")
    print("2 - Calculate the cosine of a value")
    print("3 - Calculate the tangent of a value")
    print("4 - Exit")

# menu loop
for i in range(100): #need to fix
    printMenu()
    option = int(input("Enter your option: "))
    if (option == 1 or option == 2 or option == 3): #option 1, 2, 3 opens math functions
        degrees = int(input("Enter the value (in degrees): "))
        terms = int(input("Enter the number of terms: "))
        if(option == 1): #choose sin function
            radian = degTorad(degrees)
            result = sinFunc(radian, terms)
            print("The sine of",degrees,"is %.4f" %result) 
        elif(option == 2): #choose cosine function
            radian = degTorad(degrees)
            result = cosFunc(radian, terms)
            print("The cosine of",degrees,"is %.4f" %result)   
        elif(option == 3): #choose tan function
            if degrees == 90 or degrees == 270: #tan undefined
                print("The tangent of",degrees,"is undefined")
            elif(option == 3):
                radian = degTorad(degrees)
                sin = sinFunc(radian, terms)
                cos = cosFunc(radian, terms)
                result = sin/cos
                print("The tangent of",degrees,"is %.4f" %result)
    elif(option == 4):
            break
    else:
        print("Invalid Option. Please try again")


