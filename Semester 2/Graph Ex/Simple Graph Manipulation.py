def EmptyGraph () :
    # An empty graph is represented as a pair of empty sets
    # graph[0] is the set of vertices and graph[1] is the set of edges
    graph = (set(),set())
    return graph

    
def AddVertex (graph,vertex) :
    # graph[0] is the set of vertices, so adding a vertex is achieved
    # by adding its label to the set of vertices (graph[0])
    graph[0].add(vertex)


def AddEdge (graph,v1,v2) :
    # graph[1] is the set of edges, and the edge between v1 and v2
    # is represented by the frozenset {v1,v2}, so adding the edge
    # is achieved by adding this frozenset to graph[1]
    # But we only add the edge if v1 and v2 are both in the set of
    # vertices (graph[0])
    if v1 in graph[0] and v2 in graph[0] :
        edge = frozenset ({v1,v2})
        graph[1].add(edge)


def RemoveEdge (graph,v1,v2) :
    # graph[1] is the set of edges, and the edge between v1 and v2
    # is represented by the frozenset {v1,v2}, so removing the edge
    # is achieved by removing this frozenset from graph[1]
    # We use discard because it does not throw an error if the
    # edge we want to remove is absent
    edge = frozenset ({v1,v2})
    graph[1].discard(edge)


def RemoveVertex (graph,vertex) :
    # Before we can remove a vertex we must remove all of the edges
    # that link it to other vertices
    # Once ths is done we can remove the vertex (by removing it
    # from the set of vertices)
    # We use discard because it does not throw an error if the
    # vertex we want to remove is absent
    for edge in graph [1] :
        if vertex in edge :
            graph[1].discard(edge)
    graph[0].discard(vertex)



def IsSubGraph (G1,G2) :
    # We can use the subset operation (<=) because a graph G1 is a
    # subgraph of graph G2 if - and only if - 1
    # the vertices of G1 are a subset of the vertices of G2 and
    # the edges of G1 are a subset of the edges of G2
    verticesIn = G1[0] <= G2[0]
    edgesIn    = G1[1] <= G2[1]
    return verticesIn and edgesIn



def CopyOf (graph) :
    newgraph = EmptyGraph ()
    for v in graph[0] :
        newgraph[0].add(v)
    for e in graph[1] :
        newgraph[1].add(e)
    return newgraph



# Ex 12   Just one of many ways to do it

def displayGraph1 (graph) :
    # First we create a sorted list of the graph's vertices, because
    # displaying them in order makes life easier for the user
    vertices = graph[0]
    vertexlist = sorted (list(vertices))

    # Next we're going to do the same for the edges
    edges = graph[1]
    edgelist = []             # Building up from an empty list of edges
    
    for edge in edges :       # Internally edge is a frozenset of 2 vertices 
        edge = list(edge)     # Create a list-based representation of each edge
        edge = sorted(edge)   # Represent each edge as a sorted list of 2 vertices  
        edgelist.append(edge) # Add each edge to the list of edges
        
    edgelist = sorted(edgelist)  # Now we have a sorted list of edges

    # Now display the contents of the two lists
    
    print ("Vertices:")
    for vertex in vertices :
        print (vertex,end=", ")
    print ()

    print ("Edges:")
    for edge in edgelist :
        print (edge[0],"<->",edge[1],end="   ")
    print ()


# A shorter function that does exactly the same thing
# Note how much harder it is to read and understand
def displayGraph2 (graph) :
    vertexlist = sorted (list(graph[0]))
    edgelist = sorted([sorted(list(e)) for e in graph[1]])
    print ("Vertices:")
    for v in vertexlist :
        print (v,end=", ")
    print ()
    print ("Edges:")
    for e in edgelist :
        print (e[0],"<->",e[1],end="   ")
    print ()


# Ex 13

def neighbourhood (graph,v) :
    # Returns the set of vertices that are neighbours of v
    # Start with an empty set and build from there
    neighbours = set()
    # Go through the set of edges, examining each n turn:
    for edge in graph[1] :
        # When you find an edge {v,w} (one that includes v),
        # add the vertex w from that edge to the set of neighbours:
        if v in edge :
            # Create a new set called neighbour containing just w
            # by subtracting the {v} from {v,w}
            neighbour = set (edge - {v})   # frozenset - set -> frozenset
            # Find the union of neighbours with neighbour
            # and assign the result the name neighbours
            neighbours = neighbours.union(neighbour)
    return neighbours


def neighbourhood2 (graph,v) :
    # Another way to do this is to create a set that is the union
    # of all the edges containing v, and then subtract the set
    # containing just v from that set(because v isn't in its own
    # neighbourhood
    neighbours = set()
    for edge in graph[1] :
        if v in edge :
            neighbours = neighbours.union(edge)
    return neighbours - {v}
    

# Ex 14

def degree (graph,v) :
    # The degree of a vertex is the number of edges that contain v
    edges = {edge for edge in graph[1] if v in edge}
    return len(edges)

def degree2 (graph,v) :
    # The degree of a vertex is the number of incident edges
    # it has. This is the same as the size of its neighbourhood
    return len(neighbourhood(graph,v))


G = EmptyGraph()

AddVertex (G,'1')
AddVertex (G,'2')
AddVertex (G,'3')
AddVertex (G,'4')
AddVertex (G,'5')
AddVertex (G,'6')
AddVertex (G,'7')
AddVertex (G,'8')
AddVertex (G,'9')


AddEdge (G,'1','3')
AddEdge (G,'1','4')
AddEdge (G,'2','3')
AddEdge (G,'1','7')
AddEdge (G,'7','6')
AddEdge (G,'6','3')
AddEdge (G,'4','9')
AddEdge (G,'5','9')
