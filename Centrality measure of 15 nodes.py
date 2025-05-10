import networkx as nx
n = 15
G = nx.Graph()
node_list = [
    (0, 1), (0, 14), (1, 2), (1, 13), (2, 3),
    (2, 12), (3, 4), (3, 11), (4, 5), (4, 10),
    (5, 6), (5, 9), (6, 7), (6, 8), (7, 8),
    (8, 9), (9, 10), (10, 11), (11, 12), (12, 13),
    (13, 14)]
for nodes in node_list:
    G.add_edge(nodes[0], nodes[1])
    # G.add_edge(*nodes)
centrality = nx.eigenvector_centrality(G)
for n in sorted(centrality.keys()):
    print(f'c({n}) = {centrality[n]:.4f}')