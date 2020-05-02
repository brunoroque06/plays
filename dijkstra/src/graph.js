function createNode(id, edges) {
  return { id, edges };
}

function generateConnectedGraph() {
  const root = createNode(0, []);
  return { root, numberNodes: 1, numberEdges: 0 };
}

module.exports = {
  generateConnectedGraph,
};
