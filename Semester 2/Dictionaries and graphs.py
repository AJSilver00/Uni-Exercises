
#   DICTIONARIES AND GRAPHS

#=======================================================================================
#   Question 1
#-------------


''' Write a function  makedict  that takes two lists, a and b,
    as its parameters, and returns a dictionary in which each
    element of list a is the key to the corresponding element
    of list b. You may assume that list a contains only
    immutable values, and the two lists are of equal length 
    For example, after the statement sequence :
    x = ['fred','joe','bill'] 
    y = [21,5,93] 
    z = makedict(x,y) 
    z is the dictionary  { 'fred' : 21, 'joe' : 5, 'bill' : 93 }    '''

def makedict(a,b):      # a and b are both lists.
    # can be len(b) too. Both a and b should be same length anyway.

    D = dict()
    for i in range(len(a)):
        D[a[i]]=b[i]                   #it is i bcus we want names to be dictionary.
        print(a[i],b[i])
    return D

z = makedict(['Aimee','Dave','Brad'],[2,3,4])
print(z)



#=======================================================================================
#   Question 2
#-------------


''' Write a function  override  that takes two dictionaries,
    a and b, as its parameters and return a single new
    dictionary, d, which combines a and b so that all
    entries from b are included, along with all those entries
    from a whose keys are not in b. '''
def override(a,b):      # a and b are both dictionaries
    a = dict(a)
    b = dict(b)
    
    d = a.copy()        # d = copy of dictionary a
    d.update(b)         # add dictionary b to dictionary d.
    return d            # return dictionary d

z = override({'Aimee':10, 'Dave':5, 'Brad':53},{'Aimee':10, 'Luke':42, 'Henry':2})
print(z)


#=======================================================================================
#   Question 3
#-------------

''' Write a function  subtract  that takes two dictionaries,
    a and b, as its parameters and return a single new dictionary,
    d, which combines a and b so that the only entries included
    are those with keys in a but not in b.  '''
def subtract(a,b):
    a = dict(a)
    b = dict(b)
    d = a.copy()
    
    for key in a:       # for every key in a
        if key in b:    # if that key is also in b:
            d.pop(key)  # then pop the key out of d
    return d
    
z = subtract({'Aimee':10, 'Jason':5, 'Brad':53},{'Aimee':10, 'Luke':42, 'Henry':2})
print(z)


#=======================================================================================
#   Question 4
#-------------

''' Write a function  initialize  that takes a list of keys, ks,
    and a data value, v, as its two parameters and returns a new
    dictionary in which each of the keys from ks is associated with
    the value, v. '''
def initialize(ks,v):   # ks = list of keys   # v = data_value
    v = float(v)        # v = float
    dictionary = dict()

    for i in range(len(ks)):    # for every element i in list ks.
        dictionary[ks[i]]=v     # add index[i] to dictionary and assign it with value v.
    return dictionary           # should return value 5 with every name(key).

z = initialize(['Aimee', 'Jason', 'Jack'], 5)
print(z)


#=======================================================================================
#   Question 5
#-------------

''' Write a function  remove  that takes a dictionary, d, and a list
    of keys, ks, as its two parameters and returns a new dictionary
    containing all entries from d except those with keys in the list ks '''
def remove (d,ks):
    d = dict(d)
    new_dict = d.copy()

    for key in ks:
        if key in new_dict:
            new_dict.pop(key)
    return new_dict

z = remove({'Aimee':21, 'Jason':6, 'Jack':77},['Jack', 'Kai', 'Luke'])
print(z)


#=======================================================================================
#   Question 6
#-------------

''' Write a function  isin  that takes a dictionary, d, and a data
    value, v, as its two parameters and returns True if the data
    value is in the dictionary and False if it is not '''
def isin (d,v):
    d = dict(d)
    v = float(v)

    if v in d.values():     # if value v is found in dictionary d, return True.
        return True
    else:
        return False

z = isin({'Aimee':21, 'Jason':6, 'Jack':77}, 6)
print(z)


#=======================================================================================
#   Question 7
#-------------

''' Write a function  changekey  that takes a dictionary, d, and two
    keys, k1 and k2, as its three parameters and returns a new
    dictionary in which the entry with key k1 is replaced by an entry
    with the same data value but with the key k2.  You may assume
    that k1 is in d and k2 is not.  '''
def changekey(d,k1,k2):
    k1 = str(k1)
    k2 = str(k2)
    d = dict(d)
    d1 = d.copy()
    new_dict = dict()

    for key in d1:                      # for every key in d1
        for value in d1.values():       # for every value in d1.values()
            if k1 in d:                 # if k1 is in dictionary d:
                d.pop(key)              # then pop out that key
                new_key = {k2:value}    # assign a new_key k2 with the same value as old key
                d.update(new_key)       # update dictionary d with new_key.
                break                   # end all loops once key is replaced.
    return d                            # return dictionary d
        
z = changekey({'Aimee':21, 'Jason':6, 'Jack':77}, 'Aimee', 'Brad')
print(z)


#=======================================================================================
#   Question 8 - Working with weighted Graphs
#--------------------------------------------

''' Write a function  DisplayWtGraph  that takes a weighted
    undirected graph, g, as its parameter and displays the
    contents of g on screen in a more user-friendly format
    than the built-in  print  function.  A simple list of
    vertices and a list of edges with their weights will do
    the job nicely  '''

def DisplayWtGraph (g):
    d = dict()
    
    for pair in g[0]:
        for edge in g[1]:
            key_value = {pair:edge}
            d.update(key_value)
    return d  

g = DisplayWtGraph ([['v1,v2','v2,v1','v3,v5'],['ea,44','eb,33','ec,22']])
print (g)


''' Write a function GetWeight that takes a weighted undirected
    graph, g, and two vertices, v1 and v2, as its parameters
    and returns the weight on the edge between v1 and v2.
    If the edge {v1,v2} is not in the graph the function should
    return the special value None. '''
def GetWeight(G,v1v2):

    for pair in range (len(G)):
        if v1v2 in G:
            for x in G.values():
                return G.get(v1v2,None)

G = {'a,b':44,'b,c':22,'a,c':11}  
g = GetWeight(G,'b,c')
print(g)


''' Write a function WalkLength that takes a graph and a list
    of vertices as its parameters; if the list represents a
    walk through the graph (a series of vertices connected by
    edges) the function returns the length of the walk, and
    if it doesn't represent a walk the function returns the
    special value None. '''
def WalkLength(G,V):
    length = []
    for vertice in V:
        if vertice in G.keys() or G.values():
            for x in G.keys():
                num = G[x][1]
                length.append(num)
        else:
            return None
        return(sum(length))


G = {'a':('b',44), 'b':('c',22), 'c':('d',33)}  
g = WalkLength(G,['a','b','c','d'])
print(g)


'''SOME NOTES FROM JACK :D 
Although there's a better way to represent a graph with a dict
{"a": ("b", 44), "b": ("c": 22), "c": ("d", 33)}
# G["c"][1]
        # correction {'a':[('b',44)],'b':[('a',44),('c',22)],
        # 'c':[('b',22),('d',33)],'d':[('c',33)]}'''


    

    
