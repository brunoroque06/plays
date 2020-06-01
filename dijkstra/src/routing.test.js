const routing = require('./routing');

/* eslint-disable */
function connectVertices(v0, v1, weight) {
  v0.edges.push({ vertex: v1, weight });
  v1.edges.push({ vertex: v0, weight });
}

/* eslint-disable */

test('prim', () => {
  const v0 = { id: 'a', edges: [] };
  const v1 = { id: 'b', edges: [] };
  const v2 = { id: 'c', edges: [] };

  connectVertices(v0, v1, 2);
  connectVertices(v1, v2, 2);
  connectVertices(v0, v2, 3);

  const graph = { vertices: [v0, v1, v2] };

  const prim = routing.prim(graph);

  expect(prim.cost).toBe(4);
  expect(prim.edges[0].x).toBe('a');
  expect(prim.edges[0].y).toBe('b');
  expect(prim.edges[0].cost).toBe(2);
  expect(prim.edges[1].x).toBe('b');
  expect(prim.edges[1].y).toBe('c');
  expect(prim.edges[1].cost).toBe(2);
  // expect(dijkstra.paths[0].cost).toBe(2);
  // expect(dijkstra.paths[0].value).toBe(['a', 'b']);
  // expect(dijkstra.paths[1].cost).toBe(3);
  // expect(dijkstra.paths[1].value).toBe(['a', 'c']);
});
