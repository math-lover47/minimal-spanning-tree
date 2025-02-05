import networkx as nx
import matplotlib.pyplot as plt
import time
import random
import itertools

def generate_graph_with_v(v, edge_prob=0.5):
    """Generates a graph with v vertices and random edges based on edge probability."""
    G = nx.Graph()
    G.add_nodes_from(range(v))
    
    # Add edges randomly
    for u, w in itertools.combinations(range(v), 2):
        if random.random() < edge_prob:
            weight = random.uniform(0, 1)
            G.add_edge(u, w, weight=weight)
    
    return G

def generate_graph_with_e(v, e):
    """Generates a graph with v vertices and exactly e random edges."""
    G = nx.Graph()
    G.add_nodes_from(range(v))

    possible_edges = list(itertools.combinations(range(v), 2))
    selected_edges = random.sample(possible_edges, min(e, len(possible_edges)))

    for u, w in selected_edges:
        weight = random.uniform(0, 1)
        G.add_edge(u, w, weight=weight)
    
    return G

def measure_time_complexity():
    """Measures time complexity of Prim's and Kruskal's algorithms for different V and E."""
    vertices_range = list(range(10, 110, 10))  # V = 10 to 100
    edges_range = list(range(10, 1010, 100))   # E = 10 to 1000 (fixed V=100)

    prim_times_v = []
    kruskal_times_v = []
    
    prim_times_e = []
    kruskal_times_e = []

    # Measure runtime for increasing vertices (V)
    for v in vertices_range:
        G = generate_graph_with_v(v, edge_prob=0.5)  # Graph with moderate density
        
        start = time.time()
        nx.minimum_spanning_tree(G, algorithm="prim")
        prim_times_v.append(time.time() - start)

        start = time.time()
        nx.minimum_spanning_tree(G, algorithm="kruskal")
        kruskal_times_v.append(time.time() - start)

    # Measure runtime for increasing edges (E) with fixed V=100
    v_fixed = 100
    for e in edges_range:
        G = generate_graph_with_e(v_fixed, e)
        
        start = time.time()
        nx.minimum_spanning_tree(G, algorithm="prim")
        prim_times_e.append(time.time() - start)

        start = time.time()
        nx.minimum_spanning_tree(G, algorithm="kruskal")
        kruskal_times_e.append(time.time() - start)

    # Plot results
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Plot Time vs Vertices
    axes[0].plot(vertices_range, prim_times_v, label="Prim's Algorithm", marker='o', linestyle='--')
    axes[0].plot(vertices_range, kruskal_times_v, label="Kruskal's Algorithm", marker='s', linestyle='--')
    axes[0].set_xlabel("Number of Vertices (V)")
    axes[0].set_ylabel("Execution Time (seconds)")
    axes[0].set_title("Time Complexity vs Vertices (V)")
    axes[0].legend()

    # Plot Time vs Edges
    axes[1].plot(edges_range, prim_times_e, label="Prim's Algorithm", marker='o', linestyle='--')
    axes[1].plot(edges_range, kruskal_times_e, label="Kruskal's Algorithm", marker='s', linestyle='--')
    axes[1].set_xlabel("Number of Edges (E)")
    axes[1].set_ylabel("Execution Time (seconds)")
    axes[1].set_title("Time Complexity vs Edges (E)")
    axes[1].legend()

    plt.tight_layout()
    plt.show()

# Run the experiment
measure_time_complexity()
