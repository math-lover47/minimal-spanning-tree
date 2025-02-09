# Requirements

## Download:

python

ide for him

## Libraries:

pip install networkx[default]

python -m pip install -U pip

python -m pip install -U matplotlib

# Minimum Spanning Tree (MST) Algorithms

This project implements and compares Prim's and Kruskal's algorithms for finding minimum spanning trees in weighted graphs. It includes visualization capabilities and performance benchmarking tools.

## Files

- `show.py`: Implements basic graph generation and visualization of MST algorithms
- `test.py`: Provides benchmarking functionality and performance comparison between algorithms

## Requirements

```
networkx
matplotlib
numpy
```

Install requirements using:
```bash
pip install networkx matplotlib numpy
```

## Usage

### Basic Visualization (show.py)

Run `show.py` to visualize a random graph and its minimum spanning trees using both algorithms:

```bash
python show.py
```

You will be prompted to enter:
- Number of vertices
- Minimum edge weight
- Maximum edge weight

The program will display:
1. The original random graph
2. MST found using Prim's algorithm
3. MST found using Kruskal's algorithm

### Performance Testing (test.py)

Run `test.py` to benchmark and compare the performance of both algorithms:

```bash
python test.py
```

You will be prompted to enter:
- Number of vertices
- Minimum edge weight
- Maximum edge weight
- Edge probability (0.0-1.0)
- Number of test runs

The program will:
1. Generate random graphs according to your specifications
2. Run both algorithms multiple times
3. Display performance metrics and graphs
4. Save results to `mst_results.txt`
5. Show visualizations of the execution times

## Features

- Random graph generation with customizable parameters
- Visual representation of graphs and MSTs
- Performance benchmarking
- Comparative analysis of algorithms
- Result logging
- Execution time visualization

## Output

### show.py
- Three graph visualizations (original, Prim's MST, Kruskal's MST)

### test.py
- Average execution times for both algorithms
- Performance comparison plots
- Generated graph visualization
- Results saved to `mst_results.txt`

## Documentation

### show.py

```python
def generate_graph(num_vertices, edge_range):
    """
    Generate a random graph with given number of vertices and edge weights within the specified range.
    
    Args:
        num_vertices (int): Number of vertices in the graph
        edge_range (tuple): Range of possible edge weights (min, max)
    
    Returns:
        list: List of tuples (source, target, weight) representing edges
    """

def prim_mst(edges):
    """
    Find minimum spanning tree using Prim's algorithm.
    
    Args:
        edges (list): List of tuples (source, target, weight) representing edges
    
    Returns:
        networkx.Graph: Minimum spanning tree
    """

def kruskal_mst(edges):
    """
    Find minimum spanning tree using Kruskal's algorithm.
    
    Args:
        edges (list): List of tuples (source, target, weight) representing edges
    
    Returns:
        networkx.Graph: Minimum spanning tree
    """

def draw_graph(graph, pos, title):
    """
    Visualize a graph with edge weights.
    
    Args:
        graph (networkx.Graph): Graph to visualize
        pos (dict): Dictionary with node positions
        title (str): Title for the plot
    """
```

### test.py

```python
def generate_graph(num_vertices, edge_range, edge_probability):
    """
    Generate a random graph with given parameters.
    
    Args:
        num_vertices (int): Number of vertices in the graph
        edge_range (tuple): Range of possible edge weights (min, max)
        edge_probability (float): Probability of edge creation between any two vertices
    
    Returns:
        list: List of tuples (source, target, weight) representing edges
    """

def benchmark_mst(num_vertices, edge_range, edge_probability, runs):
    """
    Benchmark both MST algorithms multiple times.
    
    Args:
        num_vertices (int): Number of vertices in the graph
        edge_range (tuple): Range of possible edge weights
        edge_probability (float): Probability of edge creation
        runs (int): Number of test runs to perform
    
    Returns:
        tuple: Lists of execution times for both algorithms and the last generated edges
    """

def save_results(num_vertices, edge_range, runs, edge_probability, prim_time, kruskal_time):
    """
    Save benchmark results to a file.
    
    Args:
        num_vertices (int): Number of vertices in the graph
        edge_range (tuple): Range of possible edge weights
        runs (int): Number of test runs performed
        edge_probability (float): Probability of edge creation
        prim_time (float): Average execution time for Prim's algorithm
        kruskal_time (float): Average execution time for Kruskal's algorithm
    """

def draw_graph(graph, title):
    """
    Visualize a graph with edge weights.
    
    Args:
        graph (networkx.Graph): Graph to visualize
        title (str): Title for the plot
    """
```

## Note

- Edge probability affects graph density
- Higher vertex counts will increase computation time
- Results may vary between runs due to random graph generation

For more information about minimum spanning trees and these algorithms, please refer to the documentation of the NetworkX library.
