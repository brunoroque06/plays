let random = require('./random');

test('int', () => {
  const value = random.getInt(0, 10);

  expect(value).toBeLessThanOrEqual(10);
  expect(value).toBeGreaterThanOrEqual(0);
});

test('int multiple', () => {
  let values = random.getIntMultiple(0, 10, 5);

  expect(values).toHaveLength(5);
  values.forEach((v) => {
    expect(v).toBeLessThanOrEqual(10);
    expect(v).toBeGreaterThanOrEqual(0);
  });
});
