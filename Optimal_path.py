from queue import Queue
import heapq

class Graph:
    def __init__(self, V=(), E=()):
        """
        A class for representing a graph, where V is a set of vertices (nodes) and E is a set of edges (connections 
        between vertices).

        Parameters:
        V (set): A set of vertices.
        E (set): A set of edges.

        Attributes:
        V (set): A set of vertices.
        E (set): A set of edges.
        neighbors (dict): A dictionary containing the neighbors of each vertex in the graph.

        Returns:
        None.
        """
        self.V = set()
        self.E = set()

        self.neighbors = {}
        
        # Add vertices and edges to the graph
        for v in V: 
            self.add_vertex(v)
        for e in E: 
            self.add_edge(e)

    def add_vertex(self, v):
        """
        Adds a vertex to the graph.

        Parameters:
        v (object): The vertex to be added.

        Returns:
        None.
        """
        self.V.add(v)

    def remove_vertex(self, v):
        """
        Removes a vertex from the graph.

        Parameters:
        v (object): The vertex to be removed.

        Returns:
        If the vertex is not in the graph, returns a string indicating that the city is not found on the graph.
        """
        if v in self.V:
            self.V.remove(v)
        else:
            return "City is not found on Graph"

    def add_edge(self, u, v, wt):
        """
        Adds an edge to the graph.

        Parameters:
        u (object): The first vertex of the edge.
        v (object): The second vertex of the edge.
        wt (float): The weight of the edge.

        Returns:
            None
        """
        if u not in self.neighbors:
            self.neighbors[u] = {v: wt}
        else:
            self.neighbors[u][v] = wt

        if v not in self.neighbors:
            self.neighbors[v] = {u: wt}
        else:
            self.neighbors[v][u] = wt

    def remove_edge(self, u, v, wt):
        """
        Removes an edge from the graph.

        Parameters:
        u (object): The first vertex of the edge.
        v (object): The second vertex of the edge.
        wt (float): The weight of the edge.

        Returns:
        If there is no path between the two cities, returns a string indicating that no path is found between them.
        """
        if u in self.neighbors[v] and v in self.neighbors:
            del self.neighbors[v][u]   
        if v in self.neighbors[u] and u in self.neighbors:
            del self.neighbors[u][v]     
        else:
            return 'No path is found between the two cities!'

    def __iter__(self):
        """
        A special method that allows the graph to be iterated over.

        Returns:
        An iterator over the vertices in the graph.
        """
        return iter(self.V)
    
    def nbrs(self, v):
        """
        Returns the neighbors of a vertex in the graph.

        Parameters:
        v (object): The vertex whose neighbors are being requested.

        Returns:
        An iterator over the neighbors of the vertex.
        """
        return iter(self.neighbors[v])

class GraphTraversal(Graph):
    def __init__(self):
        self.gt = Graph()
    
    def fewest_flights(self,city): 
        """
        Finds how to get from city to any other city in the graph with the fewest number of flights.
        This is for busy users who need to get from city to city quickly, and cannot waste time in extraneous layovers.
        BFS  is for fewest flights!!!
        """
        # Create a dictionary to store the traversal order and the distance from the source vertex
        traversal_order = {}
        distances = {}
        
        # Initialize the distances of all vertices to infinity except the source vertex, which is 0
        for v in self.gt._V:
            distances[v] = float('inf')
        distances[city] = 0
        
        # Initialize a queue for BFS and enqueue the source vertex
        queue = Queue()
        queue.put(city)
        
        # Perform BFS
        while not queue.empty():
            # Dequeue a vertex from the queue
            curr = queue.get()
            
            # Visit the vertex if it hasn't been visited yet
            if curr not in traversal_order:
                # Add the vertex to the traversal order
                traversal_order[curr] = len(traversal_order)
                
                # Update the distances of the neighbors of the current vertex
                for nbr in self.gt.nbrs(curr):
                    if distances[nbr] == float('inf'):
                        distances[nbr] = distances[curr] + 1
                        
                    # Enqueue the neighbor if it hasn't been visited yet
                    queue.put(nbr)
        
        return traversal_order, distances

    def shortest_path(self, city):
        """
        Finds how to get from city to any other city in the graph with the fewest number of miles travelled.
        This is for environmentally conscious users who want to use the least amount of fuel to get between two cities.
        Dijkstra's algorithm is used for finding the shortest path.
        """
        # Create a dictionary to store the traversal order and the distance from the source vertex
        traversal_order = {}
        distances = {}
        
        # Initialize the distances of all vertices to infinity except the source vertex, which is 0
        for v in self.gt._V:
            distances[v] = float('inf')
        distances[city] = 0
        
        # Initialize a priority queue for Dijkstra's algorithm and enqueue the source vertex
        queue = [(0, city)]
        
        # Perform Dijkstra's algorithm
        while queue:
            # Dequeue a vertex from the queue with the smallest distance
            curr_dist, curr = heapq.heappop(queue)
            
            # Visit the vertex if it hasn't been visited yet
            if curr not in traversal_order:
                # Add the vertex to the traversal order
                traversal_order[curr] = len(traversal_order)
                
                # Update the distances of the neighbors of the current vertex
                for nbr, wt in self.gt.nbrs(curr).items():
                    if distances[nbr] > curr_dist + wt:
                        distances[nbr] = curr_dist + wt
                        
                        # Enqueue the neighbor with its updated distance
                        heapq.heappush(queue, (distances[nbr], nbr))
        
        return traversal_order, distances
    def minimum_salt(self, city):
        """
        Connects city to every other city in the graph with the fewest total number of miles.
        This tree would allow us to keep all cities connected in the winter with the least amount of salt used on roads.
        prmins algorithsm!!!
        """
        # Create a dictionary to store the traversal order and the distance from the source vertex
        traversal_order = {}
        distances = {}
        
        # Initialize the distances of all vertices to infinity except the source vertex, which is 0
        for v in self.gt._V:
            distances[v] = float('inf')
        distances[city] = 0
        
        # Initialize a priority queue for Prim's algorithm and enqueue the source vertex
        queue = [(0, city)]
        
        # Create a set to keep track of visited vertices
        visited = set()
        
        # Create a dictionary to store the minimum spanning tree
        mst = {}
        
        # Perform Prim's algorithm
        while queue:
            # Dequeue a vertex from the queue with the smallest distance
            curr_dist, curr = heapq.heappop(queue)
            
            # Visit the vertex if it hasn't been visited yet
            if curr not in visited:
                # Add the vertex to the visited set
                visited.add(curr)
                
                # Add the vertex and its distance to the traversal order
                traversal_order[curr] = len(traversal_order)
                if curr != city:
                    mst[(curr, distances[curr])] = traversal_order[curr]
                
                # Update the distances of the neighbors of the current vertex
                for nbr, wt in self.gt.nbrs(curr).items():
                    if nbr not in visited and distances[nbr] > wt:
                        distances[nbr] = wt
                        
                        # Enqueue the neighbor with its updated distance
                        heapq.heappush(queue, (distances[nbr], nbr))
        
        # Return the traversal order and the minimum spanning tree
        return traversal_order, mst


    
