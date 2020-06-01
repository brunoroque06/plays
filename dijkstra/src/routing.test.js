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
});

test('get vertices paths', () => {
  const edges = [
    { x: 'a', y: 'b', cost: 2 },
    { x: 'b', y: 'd', cost: 1 },
    { x: 'a', y: 'c', cost: 2 },
  ];

  const paths = routing.getPaths(edges);

  expect(paths[0].cost).toBe(2);
  expect(paths[0].ids).toStrictEqual(['a', 'b']);
  expect(paths[1].cost).toBe(3);
  expect(paths[1].ids).toStrictEqual(['a', 'b', 'd']);
  expect(paths[2].cost).toBe(2);
  expect(paths[2].ids).toStrictEqual(['a', 'c']);
});

test('dijkstra', () => {
  const v0 = { id: 'a', edges: [] };
  const v1 = { id: 'b', edges: [] };
  const v2 = { id: 'c', edges: [] };

  connectVertices(v0, v1, 2);
  connectVertices(v1, v2, 2);
  connectVertices(v0, v2, 3);

  const graph = { vertices: [v0, v1, v2] };

  const dijk = routing.dijkstra(graph);

  expect(dijk.cost).toBe(5);
  expect(dijk.edges[0].x).toBe('a');
  expect(dijk.edges[0].y).toBe('b');
  expect(dijk.edges[0].cost).toBe(2);
  expect(dijk.edges[1].x).toBe('a');
  expect(dijk.edges[1].y).toBe('c');
  expect(dijk.edges[1].cost).toBe(3);
});
