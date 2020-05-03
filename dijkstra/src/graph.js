const R = require('ramda');

function calculateNumberEdges(nVer, density) {
  return Math.round(
    nVer - 1 + (density / 100) * ((nVer * (nVer - 1)) / 2 - (nVer - 1)),
  );
}

function createNode(id) {
  return { id, edges: [] };
}

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

function createGraph(nodes) {
  return { nodes, root: nodes[0] };
}

function generateConnectedGraph(getRandomInt) {
  return (numNodes, maxEdgeCost) =>
    R.pipe(
      R.range(0, numNodes).map((i) => createNode(i)),
      // connectNodes(getRandomInt, maxEdgeCost),
      createGraph,
    );
}

module.exports = {
  calculateNumberEdges,
  generateConnectedGraph,
};
