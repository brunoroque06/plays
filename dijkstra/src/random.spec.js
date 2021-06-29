let random = require('./random');

it('int', () => {
  const value = random.getInt(0, 10);

  expect(value).toBeLessThanOrEqual(10);
  expect(value).toBeGreaterThanOrEqual(0);
});

it('int multiple', () => {
  let values = random.getIntMultiple(0, 10, 5);

  expect(values.length).toBe(5);
  values.forEach((v) => {
    expect(v).toBeLessThanOrEqual(10);
    expect(v).toBeGreaterThanOrEqual(0);
  });
});
