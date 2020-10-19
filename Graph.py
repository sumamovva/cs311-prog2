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
            graph = [[] for _ in range(total_vertices+1)]
            
            for line in f:
                vertices = line.split()
                first_vertex = int(vertices[0])
                second_vertex = int(vertices[-1])
                # print(second_vertex)
                
                #if first_vertex != []:
                graph[first_vertex].append(second_vertex)

                # if second_vertex != []:
                graph[second_vertex].append(first_vertex)

        return graph
    
    def print_graph(self):
        for i in range(self.n_nodes):
                print(i, self.graph_repr[i])

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
        # initializes coloring adjacent list with all -1s (uncolored)
        coloring = [-1]*self.n_nodes

        """coloring[0] = 0 # init src to color 0

        queue = []
        queue.append(1)
        
        while queue:
            start = queue.pop()

            for dest in self.graph_repr[start]:
                if start == dest: # self loop
                    print("[]")
                    return []

            for dest in self.graph_repr[start]:
                # edge exists from start to dest and dest is -1 (uncolored)
                if coloring[dest] == -1:
                    if coloring[start] == 0: # set dest to opposite color as start
                        coloring[dest] = 1 
                    else:
                        coloring[dest] = 0
                    queue.append(dest)

                # edge exists from start to dest and dest is colored with same color as start
                elif coloring[dest] == coloring[start]:
                    return []

        print(coloring)
        return coloring
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
                                        return []
                                else:
                                    if coloring[start] == 0:
                                        coloring[connected] = 1
                                    else:
                                        coloring[connected] = 0
        
        coloring.pop(0) # ignores node 0 
        print(coloring)
        return coloring        

def main():
    #Main function, you can edit as needed
    #Extra import may also be made locally in this function

   graph = Graph('../data/smallgraph')
   # graph.print_graph()
   colors = graph.check_2colorable()



if __name__ == '__main__':
    main()
