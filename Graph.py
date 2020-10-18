# Do not change the name of this file or the class name.

# adjacency list representation 
class AdjNode:
    
    def __init__(self, value):
        self.vertex = value
        self.next = None

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
                
                edges = [second_vertex]
                graph[first_vertex].append(second_vertex)

                egdes = [first_vertex]
                graph[second_vertex].append(first_vertex)

                """node = AdjNode(second_vertex)
                node.next = graph[first_vertex]
                graph[first_vertex] = node

                node = AdjNode(first_vertex)
                node.next = graph[second_vertex]
                graph[second_vertex] = node"""

        return graph
    
    def print_graph(self):
        """for i in range(self.n_nodes):
            print("v " + str(i) + ": ", end="")
            temp = self.graph_repr[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")"""
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
        pass

def main():
    #Main function, you can edit as needed
    #Extra import may also be made locally in this function

   graph = Graph('data/largegraph1')
   graph.print_graph()
   colors = graph.check_2colorable()



if __name__ == '__main__':
    main()
