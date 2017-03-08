import json
import networkx as nx


# This function is unnecessary to use in this specific case given that the available data provides "edges".
def nodes_from_data(data, k):
    nodes = [x[k] for x in data]
    return nodes


def edges_from_data(data, k1, k2):
    edges = [(x[k1], x[k2]) for x in data]
    return edges

if __name__ == "__main__":
    jump_data = json.load(open('jumps.json'))
    jumps     = edges_from_data(jump_data, 'fromSolarSystemID', 'toSolarSystemID')

    G = nx.Graph()
    G.add_edges_from(jumps)
    print(nx.info(G))
