const graph = require('./graph');

test('number of edges', () => {
  expect(graph.calculateNumberEdges(3, 0)).toBe(2);
  expect(graph.calculateNumberEdges(4, 0)).toBe(3);
  expect(graph.calculateNumberEdges(4, 30)).toBe(4);
  expect(graph.calculateNumberEdges(4, 100)).toBe(6);
});

test('create edge pool', () => {
  const edges = graph.createEdgePool(4);
  expect(edges[0]).toEqual([1, 0]);
  expect(edges[1]).toEqual([2, 0]);
  expect(edges[2]).toEqual([2, 1]);
  expect(edges[3]).toEqual([3, 0]);
  expect(edges[4]).toEqual([3, 1]);
  expect(edges[5]).toEqual([3, 2]);
});

test('create edges with 0 density', () => {
  const getInt = (n) => n;
  const edges = graph.createEdges(getInt, 4, 3);
  expect(edges.length).toBe(3);
  expect(edges[0]).toEqual([1, 0]);
  expect(edges[1]).toEqual([2, 0]);
  expect(edges[2]).toEqual([3, 0]);
});

test('create edges with higher density', () => {
  const getInt = (n) => n;
  const edges = graph.createEdges(getInt, 4, 5);
  expect(edges.length).toBe(5);
  expect(edges[0]).toEqual([1, 0]);
  expect(edges[1]).toEqual([2, 0]);
  expect(edges[2]).toEqual([3, 0]);
  expect(edges[3]).toEqual([2, 1]);
  expect(edges[4]).toEqual([3, 1]);
});

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
