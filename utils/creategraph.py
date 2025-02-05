import networkx as nx
import matplotlib.pyplot as plt
import random
import itertools
import sys

def generate_and_draw_graph(n, a, b):
    # Error handling for input parameters
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    if a > b:
        raise ValueError("a must be less than or equal to b.")
    if a < 0 or b < 0:
        raise ValueError("a and b must be non-negative integers.")
    
    max_edges = n * (n - 1) // 2
    if a > max_edges or b > max_edges:
        raise ValueError(f"The range [a, b] must be within [0, {max_edges}] for n={n} vertices.")
    
    # Generate random number of edges m within [a, b]
    m = random.randint(a, b)
    
    # Generate all possible edges (without self-loops or duplicate edges)
    possible_edges = list(itertools.combinations(range(n), 2))
    
    # Randomly select m edges
    edges = random.sample(possible_edges, m)
    
    # Create the graph
    G = nx.Graph()
    G.add_nodes_from(range(n))
    G.add_edges_from(edges)
    
    # Draw the graph
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500)
    plt.title(f"Graph with {n} vertices and {m} edges")
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <n> <a> <b>")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
        a = int(sys.argv[2])
        b = int(sys.argv[3])
        generate_and_draw_graph(n, a, b)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)