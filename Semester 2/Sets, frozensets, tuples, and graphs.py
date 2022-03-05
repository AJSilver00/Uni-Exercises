''' Write a function evens that takes a pair of whole numbers,
    a, and b and returns a new set containing all of the even
    numbers between a and b inclusive.
                                        '''
def evens(a, b):
    a = int(a)
    b = int(b)
    even = set()
    for x in range (a, b):
        if x%2 == 0:
            even.add(x)
    return even
print (evens (2, 10))


''' Write a function intersect that takes a list of sets, setlist,
    as its parameter and returns a new set that contains just the
    elements that are in the intersection of all the sets in setlist.
                                                                   '''
# The function intersect below does not use setlist as a proper paramter!!!
def intersect(setlist=[]):
    setlist = []

    how_many = int(input('How many sets do you want?'))
    for i in range (how_many):
        s = set()
        n = int(input('How many numbers do want this set to have?'))
        for i in range (n):
            num = int(input('Please enter a number:'))
            s.add(num)
        setlist.append(s)
    print (setlist[0].intersection(*setlist))


# the function intersect2 below uses setlist a parameter.
# To call, write: intersect2([(0,3,2,4,etc), (3,4,5,3,etc), etc)])
def intersect2(setlist):
    setlist_length = len(setlist)

    # defining setlist's index 0 as a set
    # means that python will think not only the first set in selist is a set,
    # but python will also think every other set in setlist is also a set.
    setlist_one = setlist[0]        
    inter_set = set(setlist_one)
    
    index = 1
    while index < setlist_length:
        inter_set = inter_set.intersection(setlist[index])
        index = index + 1
    return inter_set
        
''' Write a function  singletons  that takes a set, S, as its
    parameter and returns a set of frozensets, FS, as its result,
    such that each member of FS contains a single element of S and
    each element of S is represented in FS.
    For example, if S is {1,2,3,4}  FS will be  { {1}, {2}, {3}, {4} }
                                                                    '''
def singletons(S):      #S = set

    FS = set()
    
    if type(S) == tuple:   
        S_length = len(S)


        for x in range (S_length):
            miniset = set()
            miniset.add(S[x])
            frozen_miniset = frozenset(miniset)
            FS.add(frozen_miniset)
    print(FS)

''' Write a function  divisors  that takes a positive whole number
    as its argument and returns a set containing all the divisors
    of that number. (A divisor is a number that divides evenly into
    another number. For example, 4 is a divisor of 28 because 28 ÷ 4
    has a remainder of 0).  '''

def divisors(y):
    y = int(y)
    divisors = set()
    
    for x in range(y):
        if y%(x+1) == 0:        # x+1 = for loop starts at 1.
            divisors.add(x+1)   # remember to use x+1 in solution here too.
    print(divisors)


''' Write a function  letters  that takes a character string, s, as its
    single parameter and returns a set containing all of the letters
    that are found in s, but no other characters.   '''

def letters(s):
    s = str(s)

    filter_letters = ''.join(filter(str.isalpha, s))
    
    letters_found_in_s = set()

    letters_found_in_s.add(filter_letters)
            
    print (letters_found_in_s)


''' Write a function fewest that takes as its parameter a set of
    character strings called strset and returns the character string
    drawn from the set that contains the fewest unique characters. '''

# unique character means characters that only occur once.

def fewest(strset):

    duplicates = set()
    strset_length = len(strset)

    if type(strset) == tuple:
        for char in strset:
            if strset.count(char) > 1 and char not in duplicates:
                duplicates.add(char)
        print(duplicates)




''' Write a function cartesian that takes two sets, S and T as its
    parameters and returns the Cartesian product of the two sets, SxT
    This will be a set of ordered pairs (2-tuples). 
    Reminder: the Cartesian product of two sets SxT is the set of pairs
    combining each element of S with each element of T.   '''

def cartesian (S, T):

    return tuple(((x, y),(y, x)) for x in S for y in T)






























    
