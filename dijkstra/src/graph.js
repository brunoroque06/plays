const R = require('ramda');

function calculateNumberEdges(nVertices, density) {
  return Math.round(
    nVertices -
      1 +
      (density / 100) * ((nVertices * (nVertices - 1)) / 2 - (nVertices - 1)),
  );
}

function createEdgePool(nVertices) {
  const higherIdEdges = (id) =>
    R.pipe(R.range(R.__, nVertices), R.map(R.pair(id)))(id + 1);
  return R.chain(higherIdEdges, R.range(0, nVertices));
}

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
};
