# The Torchbearer

**Student Name:** Meghan Dang
**Student ID:** 132429671
**Course:** CS 460 – Algorithms | Spring 2026

> This README is your project documentation. Write it the way a developer would document
> their design decisions , bullet points, brief justifications, and concrete examples where
> required. You are not writing an essay. You are explaining what you built and why you built
> it that way. Delete all blockquotes like this one before submitting.

---

## Part 1: Problem Analysis

> Document why this problem is not just a shortest-path problem. Three bullet points, one
> per question. Each bullet should be 1-2 sentences max.

- **Why a single shortest-path run from S is not enough:**
  _Each relic needs to be visited. A single shortest-path run may not visit each relic._

- **What decision remains after all inter-location costs are known:**
  _After all inter-location costs are known, we must determine which visiting order is the most cost-efficient._

- **Why this requires a search over orders (one sentence):**
  _To make the most cost-efficient run, we want to prioritize the corridors with the least amount of torch cost._

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

> List the source node types as a bullet list. For each, one-line reason.

| Source Node Type  | Why it is a source                          |
|-------------------|---------------------------------------------|
| _Entrance Node S_ | _Can travel to other nodes starting at S._  |
| _Relics_          | _Can travel to other Relics and the exit T_ |

### Part 2b: Distance Storage

> Fill in the table. No prose required.

| Property | Your answer                                                |
|---|------------------------------------------------------------|
| Data structure name | Nested Dictionary                                          |
| What the keys represent | start location 'u' and end location 'v'                    |
| What the values represent | Torch cost to reach that location from the source location |
| Lookup time complexity | O(1)                                                       |
| Why O(1) lookup is possible | Direct look up cost for (u, v)                             |

### Part 2c: Precomputation Complexity

> State the total complexity and show the arithmetic. Two to three lines max.

- **Number of Dijkstra runs:** _Number of relics m + Start 1 = m + 1_
- **Cost per run:** _O(nlogn)_
- **Total complexity:** _O((m + 1)(nlogn))_
- **Justification (one line):** _We need to run Dijkstra from every source node (entrance and relics)_

---

## Part 3: Algorithm Correctness

> Document your understanding of why Dijkstra produces correct distances.
> Bullet points and short sentences throughout. No paragraphs.


### Part 3a: What the Invariant Means

> Two bullets: one for finalized nodes, one for non-finalized nodes.
> Do not copy the invariant text from the spec.

- **For nodes already finalized (in S):**
  _dist[v] is the shortest path to get from x to v_

- **For nodes not yet finalized (not in S):**
  _dist[u] is the shortest path known to get from x to v using finalized nodes in S_

### Part 3b: Why Each Phase Holds

> One to two bullets per phase. Maintenance must mention nonnegative edge weights.

- **Initialization : why the invariant holds before iteration 1:**
  _Before iteration 1, only the source distance is known: 0. That is the shortest path from source to itself._
  _All remaining nodes u have not been discovered yet and S only stores the source._

- **Maintenance : why finalizing the min-dist node is always correct:**
  _Dijkstras uses a priority queue, which means that as long as the edges are non-negative._ 
  _The shortest distance will always be processed first and therefore, the shortest distance to every node will be produced._
  
- **Termination : what the invariant guarantees when the algorithm ends:**
  _The invariant guarantees that when the algorithm ends, only the shortest distances from source x to other locations will be stored in S._

### Part 3c: Why This Matters for the Route Planner

> One sentence connecting correct distances to correct routing decisions.

_Correct distance that the torchbearer will not waste torch fuel when making routing decisions._

---

## Part 4: Search Design

### Why Greedy Fails

> State the failure mode. Then give a concrete counter-example using specific node names
> or costs (you may use the illustration example from the spec). Three to five bullets.

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

### What the Algorithm Must Explore

> One bullet. Must use the word "order."

- _The algorithm must explore all possible combinations of paths and different orders of node exploration._

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | | | |
| Relics already collected | | | |
| Fuel cost so far | | | |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen | |
| Operation: check if relic already collected | Time complexity: |
| Operation: mark a relic as collected | Time complexity: |
| Operation: unmark a relic (backtrack) | Time complexity: |
| Why this structure fits | |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** _Your answer (in terms of k)._
- **Why:** _One-line justification._

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** _Your answer here._
- **When it is used:** _Your answer here._
- **What it allows the algorithm to skip:** _Your answer here._

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** _Your answer here._
- **What the lower bound accounts for:** _Your answer here._
- **Why it never overestimates:** _Your answer here._

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- _Your answer here._

---

## References

> Bullet list. If none beyond lecture notes, write that.

- _Your references here._
