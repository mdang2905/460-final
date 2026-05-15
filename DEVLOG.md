# Development Log – The Torchbearer

**Student Name:** Meghan Dang
**Student ID:** 132429671

> Instructions: Write at least four dated entries. Required entry types are marked below.
> Two to five sentences per entry is sufficient. Write entries as you go, not all in one
> sitting. Graders check that entries reflect genuine work across multiple sessions.
> Delete all blockquotes before submitting.

---

## Entry 1 – [May 12, 2026]: Initial Plan

> Required. Write this before writing any code. Describe your plan: what you will
> implement first, what parts you expect to be difficult, and how you plan to test.

_First, I will write out the problem on paper and examine the example graphs given. 
Following the steps described in the README, I will analyze the problem, noting the choices I make and why.
I expect the actual implementation will be the most difficult.
To test, I will debug the test cases, keeping track of every decision the code makes._

---

## Entry 2 – [May 12, 2026]: Wrong assumption

> Required. At least one entry must describe a bug, wrong assumption, or design change
> you encountered. Describe what went wrong and how you resolved it.

_At first, for Part 2b: Distance Storage, I did not realize a separate data structure was being used to store the data.
I filled in the table describing a graph until I got to the time complexity analysis and realized why we are using a adjacency matrix._

---

## Entry 3 – [May 14, 2026]: Another Wrong Assumption

_After Part 2b and Entry 2, I thought the distance storage was meant to be an adjacency matrix._ 
_However, while trying to find a counter example, I realized that an adjacency table only stores direct edges, while the distance storage stores distances from a source node to every other node, sometimes going through other nodes._
_I will adjust my answer to Part 2._
---

## Entry 4 – [Date]: Post-Implementation Reflection

> Required. Written after your implementation is complete. Describe what you would
> change or improve given more time.

_Your entry here._

---

## Final Entry – [Date]: Time Estimate

> Required. Estimate minutes spent per part. Honesty is expected; accuracy is not graded.

| Part | Estimated Hours |
|---|-----------------|
| Part 1: Problem Analysis | 1 hr            |
| Part 2: Precomputation Design | 2 hr            |
| Part 3: Algorithm Correctness | 1 hr            |
| Part 4: Search Design | 1 hr            |
| Part 5: State and Search Space |                 |
| Part 6: Pruning |                 |
| Part 7: Implementation |                 |
| README and DEVLOG writing |                 |
| **Total** |                 |
