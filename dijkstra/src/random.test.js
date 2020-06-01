const random = require('./random');

test('int', () => {
  const value = random.getInt(0)(10);
  expect(value).toBeLessThanOrEqual(10);
  expect(value).toBeGreaterThanOrEqual(0);
});
