/* eslint no-console: ["error", { allow: ["info"] }] */
let graph = require('./src/graph');
let random = require('./src/random');
let routing = require('./src/routing');

let g = graph.createGraph(random.getInt, {
  nVertices: 100,
  density: 75,
  minEdgeCost: 1,
  maxEdgeCost: 100,
});

let prim = routing.prim(g);
let primPaths = routing.getPaths(prim.edges);

console.info('# Prim');
console.info(prim);
console.info(primPaths);

let dijk = routing.dijkstra(g);
let dijkPaths = routing.getPaths(dijk.edges);

console.info('# Dijkstra');
console.info(dijk);
console.info(dijkPaths);
