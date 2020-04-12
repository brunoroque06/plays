const graph = require('./graph');

test('White to play in initial position', () => {
  const conGraph = graph.generateConnectedGraph();
  expect(conGraph).toBe([]);
});
