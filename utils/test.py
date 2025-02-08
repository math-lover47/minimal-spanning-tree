import time
import random
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def generate_graph(num_vertices, edge_range):
    edges = []
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if random.random() < 0.5:  # Randomly decide if an edge exists
                weight = random.uniform(*edge_range)
                edges.append((i, j, weight))
    return edges

def prim_mst(edges, num_vertices):
    G = nx.Graph()
    G.add_weighted_edges_from(edges)
    start_time = time.perf_counter()
    mst = nx.minimum_spanning_tree(G, algorithm='prim')
    end_time = time.perf_counter()
    return mst, end_time - start_time

def kruskal_mst(edges, num_vertices):
    G = nx.Graph()
    G.add_weighted_edges_from(edges)
    start_time = time.perf_counter()
    mst = nx.minimum_spanning_tree(G, algorithm='kruskal')
    end_time = time.perf_counter()
    return mst, end_time - start_time

def save_results(num_vertices, edge_range, prim_time, kruskal_time):
    with open("mst_results.txt", "a") as f:
        f.write(f"Vertices: {num_vertices}, Edge Range: {edge_range}\n")
        f.write(f"Prim's Algorithm Time: {prim_time:.9f} seconds\n")
        f.write(f"Kruskal's Algorithm Time: {kruskal_time:.9f} seconds\n")
        f.write("-" * 40 + "\n")

def benchmark_mst(num_vertices, edge_range, runs):
    prim_times = []
    kruskal_times = []
    
    for _ in range(runs):
        edges = generate_graph(num_vertices, edge_range)
        _, prim_time = prim_mst(edges, num_vertices)
        _, kruskal_time = kruskal_mst(edges, num_vertices)
        
        prim_times.append(prim_time)
        kruskal_times.append(kruskal_time)
    
    return prim_times, kruskal_times

def main():
    num_vertices = int(input("Enter number of vertices: "))
    edge_min = float(input("Enter minimum edge weight: "))
    edge_max = float(input("Enter maximum edge weight: "))
    edge_range = (edge_min, edge_max)
    runs = int(input("Enter number of runs: "))
    
    prim_times, kruskal_times = benchmark_mst(num_vertices, edge_range, runs)
    
    avg_prim_time = np.mean(prim_times)
    avg_kruskal_time = np.mean(kruskal_times)
    
    print(f"Average Prim's Algorithm Time: {avg_prim_time:.9f} seconds")
    print(f"Average Kruskal's Algorithm Time: {avg_kruskal_time:.9f} seconds")
    
    faster_algorithm = "Prim's Algorithm" if avg_prim_time < avg_kruskal_time else "Kruskal's Algorithm"
    print(f"Faster Algorithm: {faster_algorithm}")
    
    plt.figure(figsize=(10, 6))
    plt.subplot(1, 2, 1)
    plt.plot(range(1, runs + 1), prim_times, marker='o', label="Prim's Algorithm", linestyle='-')
    plt.xlabel("Run")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Prim's Algorithm Performance")
    plt.legend()
    
    plt.subplot(1, 2, 2)
    plt.plot(range(1, runs + 1), kruskal_times, marker='s', label="Kruskal's Algorithm", linestyle='-')
    plt.xlabel("Run")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Kruskal's Algorithm Performance")
    plt.legend()
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
