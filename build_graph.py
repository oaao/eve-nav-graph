import json
import networkx as nx


def load_json(data):
    return json.load(open(data))


# This function is unnecessary to use in this specific case given that the available data provides "edges".
def nodes_from_data(data, k):
    nodes = [x[k] for x in data]
    return nodes


def edges_from_data(data, k1, k2):
    edges = [(x[k1], x[k2]) for x in data]
    return edges

jumps_data = load_json('jumps.json')
jumps      = edges_from_data(jumps_data, 'fromSolarSystemID', 'toSolarSystemID')

G = nx.Graph()
G.add_edges_from(jumps)
print(nx.info(G))