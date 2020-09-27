/* eslint no-console: ["error", { allow: ["info"] }] */
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

console.info('# Prim');
console.info(prim);
console.info(primPaths);

const dijk = routing.dijkstra(g);
const dijkPaths = routing.getPaths(dijk.edges);

console.info('# Dijkstra');
console.info(dijk);
console.info(dijkPaths);
