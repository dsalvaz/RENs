from collections import defaultdict
from itertools import combinations
import networkx as nx


# Computes the frequency of each node appearing in cliques
def mono_freqs(cliques):
    node_frequency = defaultdict(int)
    for clique in cliques:
        for node in clique:
            node_frequency[node] += 1
    sorted_node_frequency = dict(sorted(node_frequency.items(), key=lambda x: x[1], reverse=True))
    return sorted_node_frequency

# Computes frequency of high-order node combinations in cliques
def high_freqs(cliques, hn):
    high_frequency = defaultdict(int)
    for clique in cliques:
        for high in combinations(clique, hn):
            sorted_high = tuple(sorted(high))
            high_frequency[sorted_high] += 1
    sorted_high_frequency = dict(sorted(high_frequency.items(), key=lambda x: x[1], reverse=True))
    return sorted_high_frequency

# Extracts MREN hyperedges containing at least one node from U in a specific time slice
def get_mren_for_time_slice(node_cliques, U, time_index):
    mren_hyperedges = []
    for node in U:
        if node in node_cliques and time_index in node_cliques[node]:
            cliques_at_time = node_cliques[node][time_index]
            for clique in cliques_at_time:
                if len(set(clique) & U) > 0:
                    mren_hyperedges.append(clique)
    return mren_hyperedges

# Extracts fractured MREN: cliques must contain at least an alpha fraction of nodes in U
def get_fractured_mren_for_time_slice(node_cliques, U, time_index, alpha):
    mren_hyperedges = []
    for node in U:
        if node in node_cliques and time_index in node_cliques[node]:
            cliques_at_time = node_cliques[node][time_index]
            for clique in cliques_at_time:
                if len(set(clique) & U) >= alpha * len(U):
                    mren_hyperedges.append(clique)
    return mren_hyperedges

# Extracts core MREN: cliques must have at least a beta fraction of their nodes in U
def get_core_mren_for_time_slice(node_cliques, U, time_index, beta):
    mren_hyperedges = []
    for node in U:
        if node in node_cliques and time_index in node_cliques[node]:
            cliques_at_time = node_cliques[node][time_index]
            for clique in cliques_at_time:
                if len(set(clique) & U) >= beta * len(clique):
                    mren_hyperedges.append(clique)
    return mren_hyperedges

# Computes Jaccard similarity between two sets of cliques
def jaccard_similarity(E_U, E_V):
    if len(E_U) == 0 or len(E_V) == 0:
        return 0.0
    intersection = set(tuple(sorted(clique)) for clique in E_U) & set(tuple(sorted(clique)) for clique in E_V)
    union = set(tuple(sorted(clique)) for clique in E_U) | set(tuple(sorted(clique)) for clique in E_V)
    return len(intersection) / len(union)

# Computes minimum overlap similarity between two sets of cliques
def minimum_overlapping_similarity(E_U, E_V):
    if len(E_U) == 0 or len(E_V) == 0:
        return 0.0
    intersection = set(tuple(sorted(clique)) for clique in E_U) & set(tuple(sorted(clique)) for clique in E_V)
    return len(intersection) / min(len(E_U), len(E_V))

# Computes Jaccard index between two generic sets
def jaccard_index(set1, set2):
    intersection = len(set1 & set2)
    union = len(set1 | set2)
    return intersection / union if union != 0 else 0.0

# Computes delta similarity based on maximum Jaccard index between clique pairs
def delta_similarity(E_U, E_V):
    if not E_U and not E_V:
        return 1.0
    if not E_U or not E_V:
        return 0.0
    E_U_sets = [set(clique) for clique in E_U]
    E_V_sets = [set(clique) for clique in E_V]
    sum_max_U = sum(max(jaccard_index(e_u, e_v) for e_v in E_V_sets) for e_u in E_U_sets)
    sum_max_V = sum(max(jaccard_index(e_v, e_u) for e_u in E_U_sets) for e_v in E_V_sets)
    return (sum_max_U + sum_max_V) / (len(E_U) + len(E_V))
