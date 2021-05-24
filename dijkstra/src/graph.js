let R = require('ramda');
let serial = require('./serial');

function calculateNumberEdges(nVertices, density) {
  const d =
    (density / 100) * ((nVertices * (nVertices - 1)) / 2 - nVertices + 1);
  return nVertices - 1 + Math.round(d);
}

function createEdges(nVertices, nEdges) {
  const aEdgesPerVertices = Math.ceil(nEdges / nVertices) + 1;

  return R.range(1, nVertices)
    .map((v) =>
      this.getIntMultiple(0, v, aEdgesPerVertices).map((vd) => [v, vd]),
    )
    .reduce(R.concat);
}

function createGraph(nVertices, density, minEdgeCost, maxEdgeCost) {
  const nEdges = calculateNumberEdges(nVertices, density);
  let edges = createEdges.bind(this)(nVertices, nEdges);

  let vertices = R.range(0, nVertices).map((v) => ({
    id: serial.toString(v),
    edges: [],
  }));

  edges.forEach((e) => {
    const weight = this.getInt(minEdgeCost, maxEdgeCost);
    vertices[e[0]].edges.push({ vertex: vertices[e[1]], weight });
    vertices[e[1]].edges.push({ vertex: vertices[e[0]], weight });
  });

  return { vertices };
}

module.exports = {
  calculateNumberEdges,
  createEdges,
  createGraph,
};
