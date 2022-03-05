
# EXERCISE SET 3 - Q8

# Sets = Cannot have duplicates. Unordered
# Lists = can have duplicates. Ordered

class digraphs () : # digraph = directed graph

    def emptyDigraph ():
        # An empty graph is represented as a pair of empty sets.
        # graph[0] = set of vertices
        # graph[1] = set of edges
        graph = (set(),set())
        return graph

    def __init__(graph,vertex) :        # e.g. to add vertex 1, call: AddVertex (G,'1')
        # How to add a vertex to a graph:
        # Put 'graph' and 'vertex' as parameters.
        # Now simply do graph[0].add(vertex)
        # NOTE: graph[0] = set of vertices
        graph[0].add(vertex)

    def add_vertex (graph,vertex) :       # (self,v) = adding a vertex v to self
        graph[0].add(vertex)



    # Define directed edge

    def add_directed_edge (graph,v1,v2,di_edge):
        if v1 in graph[0] and v2 in graph[0] :
            edge = []
            edge.append(v1)
            edge.append(v2)
            graph[1].add(edge)
            graph[2][edge] = di_edge





G = digraphs.emptyDigraph()

digraphs.add_vertex (G,'1')
digraphs.add_vertex (G,'2')
digraphs.add_vertex (G,'3')
digraphs.add_vertex (G,'4')
digraphs.add_vertex (G,'5')
digraphs.add_vertex (G,'6')
digraphs.add_vertex (G,'7')
digraphs.add_vertex (G,'8')
digraphs.add_vertex (G,'9')


add_directed_edge (G,'1','3')
add_directed_edge (G,'1','4')
add_directed_edge (G,'2','3')
add_directed_edge (G,'1','7')
add_directed_edge (G,'7','6')
add_directed_edge (G,'6','3')
add_directed_edge (G,'4','9')
add_directed_edge (G,'5','9')
add_directed_edge (G,'6','1')
