# Do not change the name of this file or the class name.
class Graph:

    def __init__(self, file_path):
        self.graph_repr = self.store_graph(file_path)
        self.n_nodes = len(self.graph_repr)

    def store_graph(self, file_path):
        """Store graph as an adjacency matrix or adjacency list.

        Arguments:
            file_path (str): path of file storing graph in the following format:
            The first line contains the number of vertices (|V |). The vertices
            are numbered 1 through |V |. Each subsequent line contains a pair of
            vertices such that each such pair defines an edge.

        Returns:
            graph_repr (list of list of int): an adjacency matrix or adjacency
            list storing graph
        """
        with open(file_path, 'r') as f:
            total_vertices = int(f.readline())
            graph = [[] for _ in range(total_vertices)]
            
            for line in f:
                vertices = line.split()
                first_vertex = int(vertices[0])
                second_vertex = int(vertices[-1])
                # print(second_vertex)
                
                graph[first_vertex - 1].append(second_vertex - 1)

                graph[second_vertex - 1].append(first_vertex - 1)

        return graph
    
    def print_graph(self):
        for i in range(self.n_nodes):
                print(i, self.graph_repr[i])

    def print_odd_cycle(self, parent, initial, final):
        odd_cycle = []
        curr = initial
        
        while(curr != final and parent[curr] != None):
            odd_cycle.append(curr+1)
            curr = parent[curr]

        odd_cycle.append(final+1)
        
        #print(odd_cycle)
        return odd_cycle

    def dfs_util(self, node, coloring, parent):
        visited = [10]*(self.n_nodes) # track if a node has been undiscovered, discovered, completed
                                         # undiscovered = WHITE = 10
                                         # discovered = GREY = 11
                                         # completed = BLACK = 12
        stack = [node]
        coloring[node] = 0 
        visited[node] = 10 # init to WHITE

        while stack:
            src = stack.pop()

            for dest in reversed(self.graph_repr[src]):
                #print("src is " + str(coloring[src]) + " and dest is" + str(coloring[dest])) 
                # print(dest)
                if visited[dest] == 10 or visited[dest] == 11:
                    stack.append(dest)
                    
                    if coloring[src] == 0:
                        coloring[dest] = 1
                    else:
                        coloring[dest] = 0

                    parent[dest] = src
                    visited[dest] = 11
                

                elif coloring[src] == coloring[dest]:
                    #print("src is" + str(src))
                        return False, self.print_odd_cycle(parent, dest, src)

            visited[src] = 12

        return True, None


    def check_2colorable(self):
        """Determine whether or not the graph is 2-colorable and return colors.

        Returns:
            colors (list of int): a list containing colors of the nodes if
            graph is 2-colorable. The color of each node needs to be one of the
            values 0 or 1. We are not asking for all different possible
            colorings of the graph and the coloring is fine as long as
            nodes of the same color don't share an edge. If graph is not
            2-colorable, return [].
        """
        # node 1's children in node 0
        # do +1 in odd cycle list
        # initializes coloring adjacent list with all -1s (uncolored)
        coloring = [-1]*(self.n_nodes)
        parent = [None]*(self.n_nodes)
        bipartite = None
        for i in range(self.n_nodes):
            if coloring[i] == -1:
                # print(i)
                bipartite, output_list = self.dfs_util(i, coloring, parent)
            if bipartite == False:
                print("false")
                print(output_list)
                return False, output_list

        print([True, coloring])
        return True, coloring

def main():
    #Main function, you can edit as needed
    #Extra import may also be made locally in this function

   graph = Graph('../data/testgraph')
   # output small graph: [True, [0, 1, 0, 0, 1, 0, 1, 1, 0, 1]]
   # graph.print_graph()
   colors = graph.check_2colorable()



if __name__ == '__main__':
    main()
