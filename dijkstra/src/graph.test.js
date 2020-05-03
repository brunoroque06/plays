const graph = require('./graph');

test('number of edges', () => {
  expect(graph.calculateNumberEdges(3, 0)).toBe(2);
  expect(graph.calculateNumberEdges(4, 0)).toBe(3);
  expect(graph.calculateNumberEdges(4, 30)).toBe(4);
  expect(graph.calculateNumberEdges(4, 100)).toBe(6);
});

// test('create graph with 1 node', () => {
//   const g = graph.generateConnectedGraph(1, 0);

//   expect(g.root.id).toBe(0);
//   expect(g.root.edges).toEqual([]);
//   expect(g.nodes.length).toBe(1);
// });

// test('create graph with 2 nodes', () => {
//   const g = graph.generateConnectedGraph(2, 0);

//   expect(g.root.id).toBe(0);
//   expect(g.root.edges[0].id).toEqual(1);
//   expect(g.root.edges[0].edges[0].id).toEqual(0);
//   expect(g.nodes).toBe(2);
// });

// test('create graph with 3 nodes', () => {
//   const g = graph.generateConnectedGraph(3, 0);

//   expect(g.numberNodes).toBe(3);
//   expect(g.root.id).toBe(0);
//   expect(g.root.edges[0].id).toEqual(1);
//   expect(g.root.edges[0].edges[0].id).toEqual(0);
// });
