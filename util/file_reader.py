from graphs.graph import Graph\

def read_graph_from_file(filename):
    """
    Read in data from the specified filename, and create and return a graph
    object corresponding to that data.

    Arguments:
    filename (string): The relative path of the file to be processed

    Returns:
    Graph: A directed or undirected Graph object containing the specified
    vertices and edges
    """

    # TODO: Use 'open' to open the file
    # TODO: Use the first line (G or D) to determine whether graph is directed 
    # and create a graph object
    # TODO: Use the second line to add the vertices to the graph
    # TODO: Use the 3rd+ line to add the edges to the graph
<<<<<<< HEAD
    
    with open(filename) as f:
        first_line = next(f).strip(' \n')

        if first_line == 'G':
            g = Graph(is_directed=False)
        elif first_line == 'D':
            g = Graph(is_directed=True)
        else:
            raise ValueError("Invalid file format.")

        for each in next(f).strip(' \n').split(','):
            g.add_vertex(each)
        
        for line in f:
            g.add_edge(line[1], line[3])

    return g

if __name__ == '__main__':

    graph = read_graph_from_file('test.txt')

    print(graph)
=======

    pass
>>>>>>> 28b0c0fb235f7f0787ebe54d3b1cc50a8577598d
