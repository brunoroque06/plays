const random = require('./random');

test('int', () => {
  expect(random.getInt(10)).toBeLessThanOrEqual(10);
});
