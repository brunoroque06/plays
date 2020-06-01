const graph = require('./src/graph');
const random = require('./src/random');
const routing = require('./src/routing');

const g = graph.createGraph(random.getInt, {
  nVertices: 10,
  density: 50,
  minEdgeCost: 1,
  maxEdgeCost: 100,
});

const prim = routing.prim(g);
const primPaths = routing.getPaths(prim.edges);

console.log('# Prim');
console.log(prim);
console.log(primPaths);

const dijk = routing.dijkstra(g);
const dijkPaths = routing.getPaths(dijk.edges);

console.log('# Dijkstra');
console.log(dijk);
console.log(dijkPaths);
