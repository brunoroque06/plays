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

// test('create graph with 0 density', () => {
//   const getInt = (min, max) => {
//     if (max < 5) return min;
//     return max;
//   };

//   const gra = graph.createGraph(getInt, {
//     nVertices: 4,
//     density: 0,
//     minEdgeCost: 0,
//     maxEdgeCost: 10,
//   });

//   const v0 = gra.vertices[0];
//   const v1 = gra.vertices[1];
//   const v2 = gra.vertices[2];
//   const v3 = gra.vertices[3];

//   expect(v0.id).toBe(0);
//   expect(v0.edges[0].vertex).toEqual(v1);
//   expect(v0.edges[0].cost).toBe(10);
//   expect(v0.edges[1].vertex).toEqual(v2);
//   expect(v0.edges[1].cost).toBe(10);
//   expect(v0.edges[2].vertex).toEqual(v3);
//   expect(v0.edges[2].cost).toBe(10);

//   expect(v1.id).toBe(1);
//   expect(v1.edges[0].vertex).toEqual(v0);
//   expect(v1.edges[0].cost).toBe(10);

//   expect(v2.id).toBe(2);
//   expect(v2.edges[0].vertex).toEqual(v0);
//   expect(v2.edges[0].cost).toBe(10);

//   expect(v3.id).toBe(2);
//   expect(v3.edges[0].vertex).toEqual(v0);
//   expect(v3.edges[0].cost).toBe(10);
// });
