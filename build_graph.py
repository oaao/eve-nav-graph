import json
import networkx as nx


# This function is unnecessary to use in this specific case given that the available data provides "edges".
def from_nodes(data, k):
    nodes = [x[k] for x in data]
    return nodes


def from_edges(data, k1, k2):
    edges = [(x[k1], x[k2]) for x in data]
    return edges


def run(data, field_from, field_to):

    jump_data = json.load(open(data))
    jumps     = from_edges(jump_data, field_from, field_to)

    G = nx.Graph()
    G.add_edges_from(jumps)
    print(nx.info(G))
    print(nx.density(G))
    print(type(G))

    return G


if __name__ == "__main__":

    run('res/jumps.json', 'fromSolarSystemID', 'toSolarSystemID')
