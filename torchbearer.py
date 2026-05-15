"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: Meghan Dang
Student ID:   132429671

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    """
    Returns
    -------
    str
        Your Part 1 README answers, written as a string.
        Must match what you wrote in README Part 1.

    TODO
    """

    part1 = """**Why a single shortest-path run from S is not enough:**
    _Each relic needs to be visited. A single shortest-path run may not visit each relic._

    - **What decision remains after all inter-location costs are known:**
    _After all inter-location costs are known, we must determine which visiting order is the most cost-efficient._

    - **Why this requires a search over orders (one sentence):**
    _To make the most cost-efficient run, we want to prioritize the corridors with the least amount of torch cost._"""

    return part1


# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    """
    Parameters
    ----------
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    list[node]
        No duplicates. Order does not matter.

    TODO
    """

    return [spawn, relics]


def run_dijkstra(graph, source):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
        graph[u] = [(v, cost), ...]. All costs are nonnegative integers.
    source : node

    Returns
    -------
    dict[node, float]
        Minimum cost from source to every node in graph.
        Unreachable nodes map to float('inf').

    TODO
    """
    distance = {node: float('inf') for node in graph}
    distance[source] = 0
    prio_q = [(0, source)]

    while prio_q:
        current_dist, u = heapq.heappop(prio_q)

        if current_dist > distance[u]:
            continue

        for v, cost in graph[u]:
            new_dist = current_dist + cost

            if new_dist < distance[v]:
                distance[v] = new_dist
                heapq.heappush(prio_q, (new_dist, v))

    return distance


def precompute_distances(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    dict[node, dict[node, float]]
        Nested structure supporting dist_table[u][v] lookups
        for every source u your design requires.

    TODO
    """
    sources = [spawn] + relics
    dist_matr = {}

    for u in sources:
        dist_matr[u] = run_dijkstra(graph, u)

    return dist_matr


# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    """
    Returns
    -------
    str
        Your Part 3 README answers, written as a string.
        Must match what you wrote in README Part 3.

    TODO
    """
    part3 = """
    - **For nodes already finalized (in S):**
  _dist[v] is the shortest path to get from x to v_

- **For nodes not yet finalized (not in S):**
  _dist[u] is the shortest path known to get from x to v using finalized nodes in S_
  
  - **Initialization : why the invariant holds before iteration 1:**
  _Before iteration 1, only the source distance is known: 0. That is the shortest path from source to itself._
  _All remaining nodes u have not been discovered yet and S only stores the source._

- **Maintenance : why finalizing the min-dist node is always correct:**
  _Dijkstras uses a priority queue, which means that as long as the edges are non-negative._ 
  _The shortest distance will always be processed first and therefore, the shortest distance to every node will be produced._
  
- **Termination : what the invariant guarantees when the algorithm ends:**
  _The invariant guarantees that when the algorithm ends, only the shortest distances from source x to other locations will be stored in S._

_Correct distance that the torchbearer will not waste torch fuel when making routing decisions._
    """
    return part3


# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    """
    Returns
    -------
    str
        Your Part 4 README answers, written as a string.
        Must match what you wrote in README Part 4.

    TODO
    """

    part4 = """
    - **The failure mode:** _Algorithm always chooses the cheapest available path to an unvisited node._
- **Counter-example setup:** _Using 
    graph = {
    'S': [('B', 1), ('C', 1)],
    'B': [('C', 1), ('D', 2), ('T', 3)],
    'C': [('B', 1), ('D', 4), ('T', 1)],
    'D': [('B', 1), ('C', 3)],
    'T': []
    }
- _
- **What greedy picks:** _Greedy would pick B, C, D, T with total 10
- **What optimal picks:** _Optimal is B, D, C, T with total 6_
- **Why greedy loses:** _Greedy loses because at B, it chooses the cheapest option C. The cost to go from C to D is pretty costly. Optimal chooses B to D which saves cost._

_The algorithm must explore all possible combinations of paths and different orders of node exploration._
    
    
    """
    return part4


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    spawn : node
    relics : list[node]
        Every node in this list must be visited at least once.
    exit_node : node
        The route must end here.

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """

    curr_node = spawn
    visited = []
    fuel_burned = 0
    best = [float('inf'),[]]

    to_visit = set(relics)

    _explore(dist_table, curr_node, to_visit, visited, fuel_burned, exit_node, best)

    return best[0], best[1]


def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : collection
        Your chosen data structure from README Part 5b.
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.

    TODO
    Implement: base case, pruning, recursive case, backtracking.

    REQUIRED: Add a 1-2 sentence comment near your pruning condition
    explaining why it is safe (cannot skip the optimal solution).
    This comment is graded.
    """
    if cost_so_far >= best[0]:
        return

    if len(relics_remaining) == 0:
        if dist_table[current_loc][exit_node] == float('inf'):
            return

        cost = cost_so_far + dist_table[current_loc][exit_node]

        if cost < best[0]:
            best[0] = cost
            best[1] = relics_visited_order.copy()
            return

    for relic in list(relics_remaining):
        cost = dist_table[current_loc][relic]

        if cost == float('inf'):
            continue

        current_cost = cost_so_far + cost
        relics_visited_order.append(relic)
        relics_remaining.remove(relic)

        _explore(dist_table, relic, relics_remaining, relics_visited_order, current_cost, exit_node, best)

        relics_remaining.add(relic)
        relics_visited_order.pop()




# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    distances = precompute_distances(graph, spawn, relics, exit_node)

    return find_optimal_route(distances, spawn, relics, exit_node)


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"

    select_sources('S', ['B', 'C', 'D'], 'T')

    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    _run_tests()

