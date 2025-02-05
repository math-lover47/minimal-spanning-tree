import networkx as nx
import matplotlib.pyplot as plt
import random
import itertools
import sys
import big_o

def generate_random_graph(n, a, b):
    """Generates a random weighted graph with n nodes and edges between a and b."""
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
    
    # Assign random weights in [0,1] to edges
    weighted_edges = [(u, v, random.uniform(0, 1)) for u, v in edges]
    G.add_weighted_edges_from(weighted_edges)
    
    return G

def compute_prim_mst(G):
    """Computes the Minimum Spanning Tree using Prim's Algorithm."""
    return nx.minimum_spanning_tree(G, algorithm='prim')

def compute_kruskal_mst(G):
    """Computes the Minimum Spanning Tree using Kruskal's Algorithm."""
    return nx.minimum_spanning_tree(G, algorithm='kruskal')

def draw_graphs(G, prim_mst, kruskal_mst):
    """Draws the original graph, Prim's MST, and Kruskal's MST side by side."""
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    # Define positions for consistent layout
    pos = nx.spring_layout(G)

    # Function to draw a graph
    def draw(G, ax, title, color='gray'):
        ax.set_title(title)
        nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color=color, node_size=500, ax=ax)
        edge_labels = {(u, v): f"{w:.2f}" for u, v, w in G.edges(data='weight')}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, ax=ax)

    # Draw Original Graph
    draw(G, axes[0], "Original Graph", color='gray')

    # Draw Prim's MST
    draw(prim_mst, axes[1], "Prim's MST", color='green')

    # Draw Kruskal's MST
    draw(kruskal_mst, axes[2], "Kruskal's MST", color='red')

    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <n> <a> <b>")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
        a = int(sys.argv[2])
        b = int(sys.argv[3])
        
        # Generate random graph
        G = generate_random_graph(n, a, b)

        # Compute MSTs
        prim_mst = compute_prim_mst(G)
        kruskal_mst = compute_kruskal_mst(G)

        # prim_complexity = big_o.big_o(compute_prim_mst(G), big_o.datagen.n_, max_n=1, n_repeats=1)
        # kruskal_complexity = big_o.big_o(compute_kruskal_mst(G), big_o.datagen.n_, max_n=1, n_repeats=1)

        # Draw all graphs in one window
        draw_graphs(G, prim_mst, kruskal_mst)
        
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
