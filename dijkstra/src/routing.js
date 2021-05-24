const R = require('ramda');

function getCheapestEdge(edges) {
  return R.reduce(
    (cheapest, edge) =>
      R.unless(
        R.pipe(R.prop('pathCost'), R.gt(R.prop('pathCost', edge))),
        R.always(edge),
      )(cheapest),
    edges[0],
    edges,
  );
}

let getEdges = R.curry((costFn, vertex) =>
  R.map((e) => ({
    x: vertex.id,
    y: e.vertex.id,
    cost: e.weight,
    pathCost: costFn(e.weight),
    vertex: e.vertex,
  }))(vertex.edges),
);

let walkGraph = R.curry((costFn, path, visited, edges) => {
  let cheapest = getCheapestEdge(edges);
  let newVisited = R.append(cheapest.y, visited);
  let newEdges = R.pipe(
    getEdges(costFn(cheapest.cost)),
    R.append(R.__, edges),
    R.flatten,
    R.filter((e) => !R.includes(e.y, newVisited)),
  )(cheapest.vertex);
  let newPath = R.append(cheapest, path);

  return R.ifElse(
    R.isEmpty,
    R.always(newPath),
    walkGraph(costFn, newPath, newVisited),
  )(newEdges);
});

function solveGraph(costFn, graph) {
  return R.pipe(
    walkGraph(
      costFn,
      R.__,
      [graph.vertices[0].id],
      getEdges(costFn(0), graph.vertices[0]),
    ),
    R.assoc('edges', R.__, {}),
    (p) => R.assoc('cost', R.pipe(R.pluck('cost'), R.sum)(p.edges), p),
  )([]);
}

function prim(graph) {
  return solveGraph(R.always(R.add(0)), graph);
}

const walkPath = R.curry((root, edges, path) => {
  let edge = R.find((e) => e.y === R.head(path.ids), edges);
  let newPath = R.pipe(
    R.assoc('ids', R.prepend(edge.x, path.ids)),
    R.assoc('cost', R.add(path.cost, edge.cost)),
  )(path);

  return R.ifElse(
    R.pipe(R.prop('ids'), R.head, R.equals(root)),
    R.always(newPath),
    walkPath(root, edges),
  )(newPath);
});

function getPaths(edges) {
  let xs = R.pluck('x', edges);
  let ys = R.pluck('y', edges);
  let root = R.find((x) => !R.includes(x, ys), xs);

  return R.pipe(
    R.map(R.append(R.__, [])),
    R.map(R.assoc('ids', R.__, {})),
    R.map(R.assoc('cost', 0)),
    R.map(walkPath(root, edges)),
  )(ys);
}

function dijkstra(graph) {
  return solveGraph(R.add, graph);
}

module.exports = {
  dijkstra,
  getPaths,
  prim,
};
