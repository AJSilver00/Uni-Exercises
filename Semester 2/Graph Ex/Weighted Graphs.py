def EmptyWtGraph () :
    # An empty graph is represented as a pair of empty sets.
    # graph[0] = set of vertices
    # graph[1] = set of edges
    # graph[2] = 'wt' weight
    graph = (set(),set(),dict())
    return graph

    
def AddVertex (graph,vertex) :      # e.g. to add vertex 1, call: AddVertex (G,'1')
    # How to add a vertex to a graph:
    # Put 'graph' and 'vertex' as parameters.
    # Now simply do graph[0].add(vertex)
    # NOTE: graph[0] = set of vertices
    graph[0].add(vertex)


def AddEdge (graph,v1,v2,wt) :  # This is AddEdge (set(),set(),dict())
                                # e.g. to add weight to edge, call: AddEdge (G,'1','3',12)
    # How to add an edge to a graph:
    # If 1st vertex and 2nd vertex is both in graph[0],
    # then convert {v1,v2} into a frozenset and give it the variable name 'edge'.
    # then add 'edge' to graph[1].
    # graph[2] is the edge between v1 and v2. This edge is
    # being associated with 'wt' weight, (aka it's assigned to a dict)
    if v1 in graph[0] and v2 in graph[0] :  
        edge = frozenset ({v1,v2})
        graph[1].add(edge)
        graph[2][edge] = wt 


def RemoveEdge (graph,v1,v2) :  # To remove edge, you must remove the 2 vertices the edge is
                                # connected to.
                                # e.g. call: RemoveEdge (G,'1','3')
    # How to remove an edge from a graph:
    # Put 'graph,v1,v2' as the parameters.
    # Now convert {v1,v2} into frozenset and give it variable name 'edge'.
    # Using 'discard' is better than using 'remove' bcus 'remove' will give
    # a run-time error if you try to remove an element that is not in a set.
    edge = frozenset ({v1,v2})
    graph[1].discard(edge)  # removes the edge
    graph[2].pop(edge)      # removes the value associated with key ('edge') from dict.



def RemoveVertex (graph,vertex) :
    for edge in graph [1] :
        if vertex in edge :     # Does the following if vertex 'in' (associated with) edge:
            graph[1].discard(edge)  # removes the edge
            graph[2].pop(edge)  # removes the value associated with key ('edge') from dict.
    graph[0].discard(vertex)    # removes the vertex


def CopyOf (graph) :
    # this gives copy of graph = (set(),set(),dict())
    newgraph = ( graph[0].copy(), graph[1].copy(), graph[2].copy() )
    return newgraph




G = EmptyWtGraph()

AddVertex (G,'1')
AddVertex (G,'2')
AddVertex (G,'3')
AddVertex (G,'4')
AddVertex (G,'5')
AddVertex (G,'6')
AddVertex (G,'7')
AddVertex (G,'8')
AddVertex (G,'9')


AddEdge (G,'1','3',12)
AddEdge (G,'1','4',99)
AddEdge (G,'2','3',9)
AddEdge (G,'1','7',6)
AddEdge (G,'7','6',53)
AddEdge (G,'6','3',12)
AddEdge (G,'4','9',10)
AddEdge (G,'5','9',4)
AddEdge (G,'6','1',5)
