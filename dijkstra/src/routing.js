const R = require('ramda');

function getCheapestEdge(edges) {
  return R.reduce(
    (cheapest, edge) =>
      R.unless(
        R.pipe(R.prop('cost'), R.gt(R.prop('cost', edge))),
        R.always(edge),
      )(cheapest),
    edges[0],
    edges,
  );
}

function getEdges(vertex) {
  return R.map((e) => {
    return {
      x: vertex.id,
      y: e.vertex.id,
      cost: e.weight,
      vertex: e.vertex,
    };
  })(vertex.edges);
}

const walkGraph = R.curry((path, visited, edges) => {
  const cheapest = getCheapestEdge(edges);
  const newVisited = R.append(cheapest.y, visited);
  const newEdges = R.pipe(
    getEdges,
    R.append(R.__, edges),
    R.flatten,
    R.filter((e) => !R.includes(e.y, newVisited)),
  )(cheapest.vertex);
  const newPath = R.append(cheapest, path);

  return R.ifElse(
    R.isEmpty,
    R.always(newPath),
    walkGraph(newPath, newVisited),
  )(newEdges);
});

function prim(graph) {
  return R.pipe(
    walkGraph(R.__, [graph.vertices[0].id], getEdges(graph.vertices[0])),
    R.assoc('edges', R.__, {}),
    (p) => R.assoc('cost', R.pipe(R.pluck('cost'), R.sum)(p.edges), p),
  )([]);
}

const walkPath = R.curry((root, edges, path) => {
  const edge = R.find((e) => e.y === R.head(path.ids), edges);
  const newPath = R.pipe(
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
  const xs = R.pluck('x', edges);
  const ys = R.pluck('y', edges);
  const root = R.find((x) => !R.includes(x, ys), xs);
  return R.pipe(
    R.map(R.append(R.__, [])),
    R.map(R.assoc('ids', R.__, {})),
    R.map(R.assoc('cost', 0)),
    R.map(walkPath(root, edges)),
  )(ys);
}

module.exports = { getPaths, prim };
