const random = require('./random');

test('int', () => {
  expect(random.getInt(0)(10)).toBeLessThanOrEqual(10);
});
