import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import random

def electric_system(L, s=0, t=1, E=5):
    def make_nx_graph(L):
        graph = nx.Graph()
        for u, v, w in L:
            graph.add_edge(u, v, capacity=w)
        return graph
    
    def make_nx_answer_graph(L):
        graph = nx.DiGraph()
        for u, v, r, i in L:
            graph.add_edge(u, v, resistance=r, intensity=i)
        return graph

    def first_Kirchoffs_law(A, L, ver):
        for v in range(ver-1):
            for i, (e1, e2, _) in enumerate(L):
                if e1 == v:
                    A[v][i] = -1
                elif e2 == v:
                    A[v][i] = 1

    def second_Kirchoffs_law(A, L, cycles, ver, edg):
        for cycle_ind in range(edg-ver+1):
            cycle = cycles[cycle_ind]
            for i in range(len(cycle)):
                a, b = cycle[(i-1)%len(cycle)], cycle[i]
                for k, (first, second, w) in enumerate(L):
                    if a == first and b == second:
                        A[cycle_ind + ver - 1][k] = w
                        break
                    elif a == second and b == first:
                        A[cycle_ind + ver - 1][k] = -w
                        break
                if a == s and b == t:
                    B[cycle_ind + ver -1] = E
                elif a == t and b == s:
                    B[cycle_ind + ver -1] = -E

  
    for i in range(len(L)):
        first, second, _ = L[i]
        if (s == first and t == second) or (s == second and t == first):
            del L[i]
            break
        
    L.append((s, t, 0))
             
    print(L)
    graph = make_nx_graph(L)
    edg = graph.number_of_edges()
    ver = graph.number_of_nodes()
    cycles = sorted(nx.cycle_basis(graph))

    A = np.zeros(shape=(edg, edg))
    B = np.zeros(shape=edg)

    first_Kirchoffs_law(A, L, ver)
    second_Kirchoffs_law(A, L, cycles, ver, edg)
    intensities = np.linalg.solve(A, B)
    result = [(v1, v2, r, i) if i >= 0 else (v2, v1, r, -i) for (v1, v2, r), i in zip(L, intensities)]
    return make_nx_answer_graph(result)

#graph = electric_system([(0, 1, 6), (0, 2, 8), (1, 3, 1), (2, 4, 7), (2, 3, 2), (3, 4, 10)], 1, 2, 10)
#print(zip(), [random.randint(1, 10) for _ in range(10)])

def erdos_renyi(n, p = 0.5):
    L = nx.erdos_renyi_graph(n, 0.5).edges
    e = len(L)
    first = [u for (u, _) in L]
    second = [v for (_, v) in L]
    
    return list(zip(first, second, [random.randint(1, 10) for _ in range(e)]))

def cubical(n):
    L = nx.random_regular_graph(3, n, 12112363).edges
    e = len(L)
    first = [u for (u, _) in L]
    second = [v for (_, v) in L]
    return list(zip(first, second, [random.randint(1, 10) for _ in range(e)]))

def bridge(n):
    v1 = random.randint(int(n/3), int((2*n)/3))
    v2 = n-v1
    L1 = erdos_renyi(v1)
    L2 = [(first + v1, second + v1, wage) for (first, second, wage) in erdos_renyi(v2)]
    node1 = random.choice(L1)
    node2 = random.choice(L2)
    return L1 + L2 + [(node1[0], node2[1], random.randint(1, 10))] + [(node1[1], node2[0], random.randint(1, 10))]

def draw_graph(graph, s, t, E):
    plt.figure(figsize=(12,10))
    pos = nx.kamada_kawai_layout(graph)
    node_options = {"node_color": "black", "node_size": 0}
    node_label_options = {"font_size": 10,
                        "font_color": "black",
                        "verticalalignment": "center",
                        "horizontalalignment": "right"}

    edge_options = {"width": 0.5, "alpha": 0.5, "edge_color": "black"}
    edge_label_options = {"label_pos": 0.3,
                        "font_size": 7,
                        "font_color": "black",
                        "rotate": False}

    edge_labels = {}
    for u, v, data in graph.edges(data=True):
        intensity = data.get('intensity', '')
        resistance = data.get('resistance', '')  # Assuming you have two weights in the edge data
        if u == s and v == t:
            edge_labels[(u, v)] = f"I = {float(intensity):.3f} A \n U = {E} V"

        else:
            edge_labels[(u, v)] = f"I = {float(intensity):.3f} A \n R = {resistance} \u03A9"
            
        

    nx.draw_networkx_nodes(graph, pos, **node_options)
    nx.draw_networkx_edges(graph, pos, **edge_options)
    nx.draw_networkx_labels(graph, pos, **node_label_options)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, **edge_label_options)
    plt.show()


graph = electric_system(bridge(12), 0, 1, 123)
draw_graph(graph, 0, 1, 123)