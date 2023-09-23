import networkx as nx

# Python Klassen erstmal besser verstehen
# => diesen Algorithmus besser verstehen.

graph = nx.DiGraph()
graph.add_edges_from([("root", "a"), ("a", "b"), ("a", "e"), ("b", "c"), ("b", "d"), ("d", "e")])
print(graph.in_edges("e"))