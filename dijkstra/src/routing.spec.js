let routing = require('./routing');

it('dijkstra', () => {
  let graph = {
    edges: [
      { vertices: ['c', 'b'], weight: 2 },
      { vertices: ['d', 'b'], weight: 10 },
      { vertices: ['c', 'b'], weight: 2 },
      { vertices: ['d', 'c'], weight: 5 },
      { vertices: ['c', 'a'], weight: 3 },
      { vertices: ['a', 'b'], weight: 2 },
    ],
    vertices: [{ id: 'a' }, { id: 'b' }, { id: 'c' }, { id: 'd' }],
  };

  let dijk = routing.dijkstra(graph);

  expect(dijk.cost).toBe(13);
  expect(dijk.vertices.get('b').cost).toBe(2);
  expect(dijk.vertices.get('c').cost).toBe(3);
  expect(dijk.vertices.get('d').cost).toBe(8);
});

it('prim', () => {
  let graph = {
    edges: [
      { vertices: ['b', 'a'], weight: 2 },
      { vertices: ['c', 'a'], weight: 3 },
      { vertices: ['c', 'b'], weight: 2 },
    ],
    vertices: [{ id: 'a' }, { id: 'b' }, { id: 'c' }],
  };

  let prim = routing.prim(graph);

  expect(prim.cost).toBe(4);

  expect(prim.edges[0].vertices).toEqual(['b', 'a']);
  expect(prim.edges[0].weight).toBe(2);
  expect(prim.edges[1].vertices).toEqual(['c', 'b']);
  expect(prim.edges[1].weight).toBe(2);
});
