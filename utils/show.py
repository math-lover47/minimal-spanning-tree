import random
import networkx as nx
import matplotlib.pyplot as plt

def generate_graph(num_vertices, edge_range):
    edges = []
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if random.random() < 0.5:  # Randomly decide if an edge exists
                weight = int(random.uniform(*edge_range))  # Convert weight to integer
                edges.append((i, j, weight))
    return edges

def prim_mst(edges):
    G = nx.Graph()
    G.add_weighted_edges_from(edges)
    return nx.minimum_spanning_tree(G, algorithm='prim')

def kruskal_mst(edges):
    G = nx.Graph()
    G.add_weighted_edges_from(edges)
    return nx.minimum_spanning_tree(G, algorithm='kruskal')

def draw_graph(graph, pos, title):
    plt.figure(figsize=(8, 6))
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=700, font_size=10)
    edge_labels = {k: int(v) for k, v in nx.get_edge_attributes(graph, 'weight').items()}  # Convert labels to integers
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=8, bbox=dict(facecolor='none', edgecolor='none'))
    plt.title(title)
    plt.show()

def main():
    num_vertices = int(input("Enter number of vertices: "))
    edge_min = float(input("Enter minimum edge weight: "))
    edge_max = float(input("Enter maximum edge weight: "))
    edge_range = (edge_min, edge_max)
    
    edges = generate_graph(num_vertices, edge_range)
    
    G = nx.Graph()
    G.add_weighted_edges_from(edges)
    pos = nx.spring_layout(G, seed=42)  # Compute positions once and reuse
    
    draw_graph(G, pos, "Original Graph")
    
    mst_prim = prim_mst(edges)
    draw_graph(mst_prim, pos, "Minimum Spanning Tree - Prim's Algorithm")
    
    mst_kruskal = kruskal_mst(edges)
    draw_graph(mst_kruskal, pos, "Minimum Spanning Tree - Kruskal's Algorithm")

if __name__ == "__main__":
    main()
