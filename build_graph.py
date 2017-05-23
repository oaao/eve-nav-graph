import json
import networkx as nx


# This function is unnecessary to use in this specific case given that the available data provides "edges".
def from_nodes(data, k):
    nodes = [x[k] for x in data]
    return nodes


def from_edges(data, k1, k2):
    edges = [(x[k1], x[k2]) for x in data]
    return edges

if __name__ == "__main__":
    jump_data = json.load(open('res/jumps.json'))
    jumps     = from_edges(jump_data, 'fromSolarSystemID', 'toSolarSystemID')

    G = nx.Graph()
    G.add_edges_from(jumps)
    print(nx.info(G))
    print(nx.density(G))
    print(type(G))
