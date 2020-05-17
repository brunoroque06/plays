const R = require('ramda');

function calculateNumberEdges(nVertices, density) {
  return Math.round(
    nVertices -
      1 +
      (density / 100) * ((nVertices * (nVertices - 1)) / 2 - (nVertices - 1)),
  );
}

function createEdgePool(nVertices) {
  const lowerEdges = (id) => R.pipe(R.range(0), R.map(R.pair(id)))(id);
  return R.chain(lowerEdges, R.range(1, nVertices));
}

const pickEdge = R.curry((getInt, pool) => {
  const idx = getInt(0, pool.length - 1);
  return { edge: pool[idx], pool: R.remove(idx, 1, pool) };
});

function joinEdges(edges) {
  return R.pipe(
    R.assoc('edges', R.pluck('edge', edges)),
    R.assoc('pool', R.pluck('pool', edges)),
  )({});
}

function createEdges(getInt, nVertices, nEdges) {
  return R.pipe(
    createEdgePool,
    R.groupWith(R.eqBy(R.head)),
    R.map(pickEdge(getInt)),
    joinEdges,
    R.prop('edges'),
  )(nVertices);
}

// function pickEdges(nVertices, nEdges, pool) {}
// const generateEdges = R.curry((getRandomInt, nVertices, nEdges) => {
//   return [];
// });

// function createNode(id) {
//   return { id, edges: [] };
// }

// function createEdge(id, cost) {
//   return { id, cost };
// }

// function connectNodes(getRandomInt, maxEdgeCost) {
//   return (nodes) => {
//     // R.append()
//     const sup = [];
//     nodes[0] = {};

//     nodes.forEach((n) => {
//       const id = getRandomInt(n.id);
//       const cost = getRandomInt(maxEdgeCost);
//       const edge = createEdge(id, cost);
//       n.edges.push(edge);
//       nodes[id].edges.push(edge);
//     });
//     return nodes;
//   };
// }

// function createGraph(nodes) {
//   return { nodes, root: nodes[0] };
// }
// const createEdges = R.curry((getRandomInt, nVertices, nEdges) => {});

// function createGraph(getRandomInt) {
//   return (nVertices, density, maxEdgeCost) =>
//     R.pipe(
//       R.always(calculateNumberEdges(nVertices, density)),
//       createEdges(getRandomInt, nVertices),
//       R.range(0, nVertices).map((i) => createNode(i)),
//       // connectNodes(getRandomInt, maxEdgeCost),
//       // createGraph,
//     );
// }

module.exports = {
  calculateNumberEdges,
  createEdgePool,
  createEdges,
};
