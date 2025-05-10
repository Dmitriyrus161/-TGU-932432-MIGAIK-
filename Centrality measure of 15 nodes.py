import networkx as nx
n = 15
G = nx.Graph()
node_list = [
    (0, 1), (1, 2), (2, 3), (3, 4),
    (4, 5), (5, 6), (6, 7), (7, 8),
    (8, 9), (9, 10), (10, 11), (11, 12),
    (12, 13), (13, 14)]
for nodes in node_list:
    G.add_edge(nodes[0], nodes[1])
    # G.add_edge(*nodes)
centrality = nx.eigenvector_centrality(G)
for n in sorted(centrality.keys()):
    print(f'c({n}) = {centrality[n]:.4f}')
