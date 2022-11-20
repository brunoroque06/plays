# Dijkstra

The following is performed:

- a random graph is created;
- the minimum spanning tree is calculated using Prim's algorithm;
- the shortest path to each vertex is calculated using Dijkstra's algorithm.

## Functional Programming and Cyclic Structures

In a functional programming language (with immutable variables), how can a cyclic structure be created? E.g.: how can structure `a` point to `b` and `b` to `a`? Haskell uses a concept called [Tying the Knot](https://wiki.haskell.org/Tying_the_Knot) to solve this problem.
