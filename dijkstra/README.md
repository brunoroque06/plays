# Dijkstra

Dijsktra
Minimum Spanning Tree
Ramda?

## Graph Properties

For an undirected connected weighted graph, the following is true:

- minimum number of edges: `n - 1`;
- maximum number of edges: `n * (n - 1) / 2`;
- number of edges for a given density: `n - 1 + d * (n * (n - 1) / 2 - n + 1)`;

where:

- `n`, number of vertices;
- `d`, graph density.

## Functional Programming and Cyclic Structures

When trying to represent a graph in a functional programming language, one might run into the following problem: creating vertices `A` and `B`, where `A` points to `B` and `B` points to `A`. How to create one without the other? Haskel uses a concept called [Tying the Knot](https://wiki.haskell.org/Tying_the_Knot) to solve this problem.
