
# IPDS Ecercise 2
# Functions with parameters


# 7. Example with one parameter
def hello (name):
    print ("Hello", name)

# 8. Goodbye
def goodbye (name):
    print ("Goodbye", name)

# 9. Delicious
def delicious (food):
    print (food, "is delicious")

# 10,11. Example: a function that uses functions with parameters
def greet ():
    forename = input("Please enter your forename")
    hello (forename)  #call the func hello and pass it the variable
                      #forename as its argument
    fave = input("Please enter the name of your favourite food")
    delicious (fave)
    goodbye (forename)  #call the func goodbye and pass it the variable
                        #forename as its argument


# 12. Example: a function with one parameter and a return value
def circArea (radius): #func circArea takes single parameter called radius
                       #and implements following program:
    pi = 3.14159
    a = pi * radius * radius
    return a

# 13. Circumference
def circumference (radius):
    pi = 3.14159
    c = 2 * pi * radius
    return c #Returns c to the calling program

# 14. Example: a function that uses functions with return values
def circle ():
    r = input ("Please enter the radius of the circle")
    r = float(r)
    area = circArea (r)
    circ = circumference (r) #call the func circumference, pass it contents
                            # of r as a parameter, and store the result in a
                            # variable called circ.
    print ("A circle of radius",r,"has area",area,"and circumference",circ)

# 15. Do the same for squares and rectangles
def sqArea (side):
    area = side * side
    return area
def sqPerimeter (side):
    perimeter = side * 4
    return perimeter
def square ():
    s = input("Please enter the side length of the square")
    s = float(s)
    area = sqArea(s)
    peri = sqPerimeter(s)
    print("A square of side length",s,"has area",area,"and perimeter",peri)

# Now write similar functions for rectangles.

def recArea (sideA, sideB):
    area = sideA * sideB
    return area
def recPerimeter (sideA, sideB):
    perimeter = ((sideA*2) + (sideB*2))
    return perimeter
def rectangle ():
    sA = input("Please enter a side length of the rectangle")
    sA = float(sA)
    sB = input("Please now enter a different side lenth of the rectangle")
    sB = float(sB)
    area = recArea(sA, sB)
    peri = recPerimeter(sA, sB)
    print("A rectangle of side length",sA,"and adjacent side length",sB,\
          "has area",area,"and perimeter",peri)


    








