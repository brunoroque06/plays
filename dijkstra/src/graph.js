const R = require('ramda');

const calculateNumberEdges = R.curry((nVertices, density) =>
  R.pipe(
    R.subtract(R.__, 1),
    R.multiply(nVertices),
    R.divide(R.__, 2),
    R.subtract(R.__, nVertices - 1),
    R.multiply(density / 100),
    R.add(nVertices - 1),
    Math.round,
  )(nVertices),
);

function createEdgePool(nVertices) {
  const lowerEdges = (id) => R.pipe(R.range(0), R.map(R.pair(id)))(id);
  return R.chain(lowerEdges, R.range(1, nVertices));
}

const groupEdgePool = R.pipe(
  R.groupWith(R.eqBy(R.head)),
  R.map((p) => R.assoc('pool', p, {})),
  R.map(R.assoc('edges', [])),
);

const pickEdges = R.curry((getInt, nEdges, edges) => {
  const pick = R.curry((idx, e) =>
    R.pipe(
      R.assoc('edges', R.append(R.nth(idx, e.pool), e.edges)),
      R.assoc('pool', R.remove(idx, 1, e.pool)),
    )({}),
  );
  return R.unless(
    R.pipe(R.prop('edges'), R.length, R.equals(nEdges)),
    R.pipe(
      pick(getInt(0, R.length(edges.pool) - 1)),
      pickEdges(getInt, nEdges),
    ),
  )(edges);
});

const joinEdges = (edges) =>
  R.pipe(
    R.assoc('edges', R.unnest(R.pluck('edges', edges))),
    R.assoc('pool', R.unnest(R.pluck('pool', edges))),
  )({});

const createEdges = R.curry((getInt, nVertices, nEdges) =>
  R.pipe(
    createEdgePool,
    groupEdgePool,
    R.map(pickEdges(getInt, 1)),
    joinEdges,
    pickEdges(getInt, nEdges),
    R.prop('edges'),
  )(nVertices),
);

const weightEdges = R.curry((getInt, { minEdgeCost, maxEdgeCost }, vertices) =>
  R.map((v) =>
    R.pipe(
      R.assoc('source', R.head(v)),
      R.assoc('target', R.last(v)),
      R.assoc('weight', getInt(minEdgeCost, maxEdgeCost)),
    )({}),
  )(vertices),
);

const createVertices = R.pipe(
  R.range(0),
  R.map(R.assoc('id', R.__, {})),
  R.map(R.assoc('edges', [])),
);

const createVertex = R.curry((id, edges) => {
  return { id, edges };
});

const mapToGraph = R.curry((nVertices, edges) => {
  const getTargets = R.curry((id, eds) => {
    return R.map((e) => {
      return {
        id: R.when(R.equals(id), R.always(e.source))(e.target),
        weight: e.weight,
      };
    })(eds);
  });

  const mapToVertex = R.curry((eds, id) =>
    R.pipe(
      R.filter((e) => R.equals(e.source, id) || R.equals(e.target, id)),
      getTargets(id),
      createVertex(id),
    )(eds),
  );
  return R.pipe(R.range(0), R.map(mapToVertex(edges)))(nVertices);
});

// const mapToGraph = R.curry((nVertices, weightedEdges) => {
//   const getEdges = R.curry((vertex, edges) =>
//     R.filter(
//       (e) => R.equals(e.source, vertex.id) || R.equals(e.target, vertex.id),
//     )(edges),
//   );
//   const addEdges = R.curry((edges, vertex) =>
//     R.pipe(
//       getEdges(vertex),
//       // R.reduce((a, b) => {
//       //   a.edges = R.append(a.edges, b.source);
//       //   return a;
//       // }, vertex),
//       R.always(vertex),
//     )(edges),
//   );
//   return R.pipe(createVertices, R.map(addEdges(weightedEdges)))(nVertices);
// });

const createGraph = R.curry(
  (getInt, { nVertices, density, minEdgeCost, maxEdgeCost }) => {
    return R.pipe(
      calculateNumberEdges(nVertices),
      createEdges(getInt, nVertices),
      weightEdges(getInt, { minEdgeCost, maxEdgeCost }),
      mapToGraph(nVertices),
    )(density);
  },
);

module.exports = {
  calculateNumberEdges,
  createEdgePool,
  createEdges,
  createGraph,
};
