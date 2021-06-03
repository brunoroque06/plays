let R = require('ramda');

function newVertex(vertices, e) {
  return (
    (vertices.has(e.vertices[0]) && !vertices.has(e.vertices[1])) ||
    (vertices.has(e.vertices[1]) && !vertices.has(e.vertices[0]))
  );
}

function dijkstra(graph) {
  let vertices = new Map([[graph.vertices[0].id, { cost: 0, path: [] }]]);

  while (vertices.size < graph.vertices.length) {
    let start;
    let edge;
    let end;

    let cost = Number.MAX_VALUE;

    graph.edges.forEach((e) => {
      if (newVertex(vertices, e)) {
        if (
          vertices.has(e.vertices[0]) &&
          vertices.get(e.vertices[0]).cost + e.weight < cost
        ) {
          [start, end] = e.vertices;
          edge = e;
          cost = vertices.get(e.vertices[0]).cost + e.weight;
        } else if (
          vertices.has(e.vertices[1]) &&
          vertices.get(e.vertices[1]).cost + e.weight < cost
        ) {
          [end, start] = e.vertices;
          edge = e;
          cost = vertices.get(e.vertices[1]).cost + e.weight;
        }
      }
    });

    vertices.set(end, { cost, path: [...vertices.get(start).path, edge] });
  }

  return {
    cost: Array.from(vertices.values())
      .map((p) => p.cost)
      .reduce(R.add),
    vertices,
  };
}

function prim(graph) {
  let edges = R.range(0, graph.edges.length).map(R.F);
  let vertices = new Set([graph.vertices[0].id]);
  let totalCost = 0;

  while (vertices.size < graph.vertices.length) {
    let index;
    let cost = Number.MAX_VALUE;

    graph.edges.forEach((e, idx) => {
      if (newVertex(vertices, e) && e.weight < cost) {
        index = idx;
        cost = e.weight;
      }
    });

    edges[index] = true;
    totalCost += cost;

    let visit = vertices.has(graph.edges[index].vertices[0])
      ? graph.edges[index].vertices[1]
      : graph.edges[index].vertices[0];

    vertices.add(visit);
  }

  return {
    cost: totalCost,
    edges: graph.edges.filter((_, idx) => edges[idx]),
  };
}

module.exports = {
  dijkstra,
  prim,
};
