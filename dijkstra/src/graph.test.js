const graph = require('./graph');

test('create graph with 1 node', () => {
  const g = graph.generateConnectedGraph(1);

  expect(g.numberNodes).toBe(1);
  expect(g.numberEdges).toBe(0);
  expect(g.root.id).toBe(0);
  expect(g.root.edges).toEqual([]);
});
