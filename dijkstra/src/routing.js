const R = require('ramda');

function walkGraph(possibleEdges, vertex, path) {
  return R.pipe(R.append(vertex.edges))(possibleEdges);
}

function getEdges(vertex) {
  const edge = R.assoc('x', vertex.id);
  return R.map((e) => {
    return {
      x: vertex.id,
      y: e.vertex.id,
      cost: e.weight,
      vertex: e.vertex,
    };
  })(vertex.edges);
}

function dijkstra(graph) {
  // const ids = R.pluck('id', graph);

  const edges = getEdges(graph.vertices[0]);

  // const { edges } = graph.vertices[0];

  const cheap = R.reduce(
    (cheapest, edge) =>
      R.unless(
        R.pipe(R.prop('weight'), R.gt(R.prop('weight', edge))),
        R.always(edge),
      )(cheapest),
    edges[0],
    edges,
  );

  const newEdges = R.append(cheap, edges);

  // get edges
  // find min
  // add edge
  // find new edges

  // const paths = R.map(
  //   R.pipe(R.assoc('vertex', R.__, {}), R.assoc('vertex', R.__, {})),
  //   edges,
  // );
  return paths;
}

module.exports = { dijkstra };
