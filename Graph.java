import java.io.File;
import java.io.FileNotFoundException;

public class Graph {
    private int[][] graphRepr;
    private int n_nodes;

    /**
     * Init and Load graph text file
    */
    public Graph(String filePath) {
        this.graphRepr = storeGraph(filePath);
        this.n_nodes = this.graphRepr.length
    }


    /**
    * Store graph as an adjacency matrix or adjacency list.
    * Arguments:
    *       filePath (String): path of file storing graph in the following format:
    *       The first line contains the number of vertices (|V |). The vertices
    *       are numbered 1 through |V|. Each subsequent line contains a pair of
    *       vertices such that each such pair defines an edge.
    *
    * Returns:
    *       graphRepr (2D array of integer): an adjacency matrix or adjacency
    *       list storing graph
    *
    * Note:
    *   - if you are implementing an adjacency list, one way to do so is to set
    *     the lenght of the adjacency list of each node to be the number of
    *     nodes in the graph and set all initial values to -1 and change -1 to
    *     node numbers as you construct the adjacency list.
    *     e.x. [[2,3,-1,-1], [1,4,-1,-1], [1,-1,-1,-1], [2,-1,-1,-1]] for a
    *     graph with input representation of the format:
    *     4
    *     1 2
    *     1 3
    *     2 4
    */
    public int[][] storeGraph(String filePath){
        int[][] graphRepr;
        try {
                // Read the file here.
        } catch (FileNotFoundException e) {
                e.printStackTrace();
        }
        return graphRepr;
    }


    /**
     * Determine whether or not the graph is 2-colorable and return colors.
     *
     * Returns:
     *     colors (array of integer): an array containing colors of the nodes if
     *     graph is 2-colorable. The color of each node needs to be one of the
     *     values 0 or 1. We are not asking for all different possible
     *     colorings of the graph and the coloring is fine as long as
     *     nodes of the same color don't share an edge. If graph is not
     *     2-colorable, return an array of lengh equal to number of the nodes in
     *     the graph with all elements equal to -1.
    */
    public int[] check2colorable(){

        int[] colors = new int[this.n_nodes];
        // Implement your algorithm here.
        return colors;

    }

    /**
   * You can use this method for testing and debugging if you wish.
    */
    public static void main(String[] args){
        Graph myGraph = new Graph("data/smallgraph");
        myGraph.check2colorable();
    }
}
