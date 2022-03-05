# Exercise set 4

# Functions that make use of if statements and for loops

# 1.
def voter ():
    age = input("Please enter your age in whole years")
    age = int(age)
    if age >= 18:
        print("You are old enough to vote")
    else:
        print("You are not old enough to vote")

# 2.
def checkNum():
    num = input("Please enter a number between 1 and 20 inclusive")
    num = int(num)
    if num < 1:
        print("Too low")
    elif num > 20:
        print("Too high")
    else:
        print ("In range")

# 3.
def footballMatch():
    teamA = input("Please enter the name of a football team playing in a league match")
    teamA = str(teamA)
    scoreA = input ("Please enter the score of this team")
    scoreA = int(scoreA)
    teamB = input("Please enter the name of another football team playing in the league match")
    teamB = str(teamB)
    scoreB = input("Please enter the score of this team")
    scoreB = int(scoreB)
    if scoreA == 0:
        print("lose")
    elif scoreB == 0:
        print("lose")
    elif scoreA == 1:
        print("draw")
    elif scoreA == 1:
        print("draw")
    else:
        print("win")

# 3.
def magnitude(x):
    x < 0
    if x < 0:
        print("The magnitude of this number is", -x)
    else:
        print("The magnitude of this number is", x)

# 4.
def isEven (n):
    d = n%2
    if d == 0:
        return False
    else:
        return True







        
