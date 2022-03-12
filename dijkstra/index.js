/* eslint no-console: ["error", { allow: ["info"] }] */
let graph = require('./src/graph');
let random = require('./src/random');
let routing = require('./src/routing');

let g = graph.createGraph.bind({
  getInt: random.getInt,
  getInts: random.getInts,
})(20, 50, 1, 100);

let prim = routing.prim(g);

console.info('# Prim');
console.info(prim.edges);
console.info(prim.cost);

let dijk = routing.dijkstra(g);

console.info('# Dijkstra');
console.info(dijk.vertices);
console.info(dijk.cost);
