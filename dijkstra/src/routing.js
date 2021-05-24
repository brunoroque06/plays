let R = require('ramda');

function dijkstra(graph) {
  let selected = R.range(0, graph.edges.length).map(R.F);
  let visited = new Set([graph.vertices[0].id]);
  let totalCost = 0;

  while (visited.size < graph.vertices.length) {
    let index;
    let cost = Number.MAX_VALUE;

    graph.edges.forEach((e, idx) => {
      if (
        ((visited.has(e.vertices[0]) && !visited.has(e.vertices[1])) ||
          (visited.has(e.vertices[1]) && !visited.has(e.vertices[0]))) &&
        e.weight < cost
      ) {
        index = idx;
        cost = e.weight;
      }
    });

    selected[index] = true;
    totalCost += cost;

    let visit = visited.has(graph.edges[index].vertices[0])
      ? graph.edges[index].vertices[1]
      : graph.edges[index].vertices[0];

    visited.add(visit);
  }

  return {
    cost: totalCost,
    edges: graph.edges.filter((_, idx) => selected[idx]),
  };
}

function prim(graph) {
  let selected = R.range(0, graph.edges.length).map(R.F);
  let visited = new Set([graph.vertices[0].id]);
  let totalCost = 0;

  while (visited.size < graph.vertices.length) {
    let index;
    let cost = Number.MAX_VALUE;

    graph.edges.forEach((e, idx) => {
      if (
        ((visited.has(e.vertices[0]) && !visited.has(e.vertices[1])) ||
          (visited.has(e.vertices[1]) && !visited.has(e.vertices[0]))) &&
        e.weight < cost
      ) {
        index = idx;
        cost = e.weight;
      }
    });

    selected[index] = true;
    totalCost += cost;

    let visit = visited.has(graph.edges[index].vertices[0])
      ? graph.edges[index].vertices[1]
      : graph.edges[index].vertices[0];

    visited.add(visit);
  }

  return {
    cost: totalCost,
    edges: graph.edges.filter((_, idx) => selected[idx]),
  };
}

module.exports = {
  dijkstra,
  prim,
};
