# IPDS Exercise set 5

# Manipulating strings

# find every A
def findEveryA():
    s_str = input('Please type in a character string')
    s_str = str(s_str)
    substr = 'A'
    count = s_str.count(substr)
    print(count)

# Find first instance of A
def findFirstA():
    s_str = input('Please type in a character string')
    s_str = str(s_str)
    substr = 'A'
    if substr in s_str:
        result = s_str.find(substr)
        print(result)
    else:
        print('The letter A is not in the string you entered')

# NOTES:

# s.find(t)     #returns: -1, or index where t starts in s
# s.index(t)    #returns: Same as find, but raises ValueError if t is not in s    

# d.rfind(t)   
# s.rindex(t)   #functions starting with r indicate that the search happens
                #from right to left.

# you might want to search for the string with spaces on either end:
# 'this is a'.find(' is ')


# Find all
def findAll():
    s_str = input('Please type in a character string')
    length = len(s_str)
    substr = input('Now please type in the letter you would like to search for')
    
    i = 0
    print("The letter '" + substr + "' appears in the following positions:")
    while i < length:
        if s_str[i] == substr:
            print (i)
        i = i + 1

def findAll2() :
    s = input ("Please type in a character string: ")
    length = len (s)
    c = input ("Please type in a character to look for: ")
    i = 0
    print ("The character '" + c + "' appears in the following positions:")
    while i < length :
        if s[i] == c :
            print (i)
        i = i + 1







