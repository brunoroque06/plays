/* eslint no-console: ["error", { allow: ["info"] }] */
let graph = require('./src/graph');
let random = require('./src/random');
let routing = require('./src/routing');

let g = graph.createGraph.bind({
  getInt: random.getInt,
  getIntMultiple: random.getIntMultiple,
})(100, 75, 1, 100);

let prim = routing.prim(g);
let primPaths = routing.getPaths(prim.edges);

console.info('# Prim');
console.info(`Cost: ${prim.cost}`);
// console.info(primPaths);

let dijk = routing.dijkstra(g);
let dijkPaths = routing.getPaths(dijk.edges);

console.info('# Dijkstra');
console.info(`Cost: ${dijk.cost}`);
// console.info(dijkPaths);
