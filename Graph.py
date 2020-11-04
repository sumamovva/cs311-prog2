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

    """def traceback_parents(self, path, node):
        curr = node
        adjacent_nodes = []
        print(curr)

        while(curr > 0):
            adjacent_nodes.append(curr)
            curr = path[curr]"""
    def print_odd_cycle(self, parent, src, dest):
        """curr = src
        odd_cycle = []
        adjacent = False

        while(curr != None):
            print(curr)
            #odd_cycle.append(curr+1)
            if(dest == curr):
                adjacent = True
                break
            curr = parents[curr]

        if(adjacent): return

        curr = dest
        while(parents[curr] != None):
            print(curr)
            #odd_cycle.append(curr+1)
            curr = parents[curr]

        # print(odd_cycle)
        return odd_cycle"""

        """while(curr != None):
            odd_cycle.append(curr+1)
            curr = parents[curr]
            for neighbor in self.graph_repr[curr]:
                if (neighbor+1) in odd_cycle:
                    return odd_cycle"""
            
        # print(odd_cycle)
        odd_cycle = []
        odd_cycle.append(src+1)
        curr = dest
        while(curr!=src and parent[curr]!=None):
            odd_cycle.append(curr+1)
            curr = parent[curr]
        # odd_cycle.append(src+1)
        return odd_cycle

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

        for src in range(self.n_nodes):
            if coloring[src] != -1: # skip node if node is already colored
                continue

            stack = [src]
            coloring[src] = 0 # init to BLACK

            while stack:
                src = stack.pop()

                for dest in self.graph_repr[src]:
                    if coloring[dest] != -1:
                        if coloring[dest] == coloring[src]:
                            odd_cycle = self.print_odd_cycle(parent, src, dest)
                            # print("[]")
                            print(False, odd_cycle)
                            return [False, odd_cycle]
                    else: 
                        parent[dest] = src
                        stack.append(dest)
                        if coloring[src] == 0:
                            coloring[dest] = 1
                        else:
                            coloring[dest] = 0

        # print([True, coloring])
        return [True, coloring]

        """
        for i in range(self.n_nodes):
                if coloring[i] == -1: # if start is uncolored
                    coloring[i] = 0 # init to BLACK
                    queue = []
                    queue.append(i)
                    while queue:
                        start = queue.pop()
                        for connected in self.graph_repr[start]:
                                if coloring[connected] != -1:
                                    if coloring[connected] == coloring[start]:
                                        print("[]")
                                        return [False, []]
                                else:
                                    if coloring[start] == 0:
                                        coloring[connected] = 1
                                    else:
                                        coloring[connected] = 0
        
        print([True, coloring])
        return [True, coloring]"""      

def main():
    #Main function, you can edit as needed
    #Extra import may also be made locally in this function

   graph = Graph('../data/testgraph')
   # output small graph: [True, [0, 1, 0, 0, 1, 0, 1, 1, 0, 1]]
   # graph.print_graph()
   colors = graph.check_2colorable()



if __name__ == '__main__':
    main()
