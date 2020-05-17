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
  const pick = R.curry((idx, e) => {
    return R.pipe(
      R.assoc('edges', R.append(R.nth(idx, e.pool), e.edges)),
      R.assoc('pool', R.remove(idx, 1, e.pool)),
    )({});
  });
  return R.unless(
    R.pipe(R.prop('edges'), R.length, R.equals(nEdges)),
    R.pipe(
      pick(getInt(0, R.length(edges.pool) - 1)),
      pickEdges(getInt, nEdges),
    ),
  )(edges);
});

const joinEdges = (edges) => {
  return R.pipe(
    R.assoc('edges', R.unnest(R.pluck('edges', edges))),
    R.assoc('pool', R.unnest(R.pluck('pool', edges))),
  )({});
};

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

// const createGraph = R.curry(
//   (getInt, { nVertices, density, minEdgeCost, maxEdgeCost }) => {
//     return R.pipe();
//   },
// );

module.exports = {
  calculateNumberEdges,
  createEdgePool,
  createEdges,
  // createGraph,
};
