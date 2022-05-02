let random = require('./random');

it('int', () => {
  const value = random.getInt(0, 10);

  expect(value).toBeGreaterThanOrEqual(0);
  expect(value).toBeLessThanOrEqual(10);
});

it('int multiple', () => {
  let values = random.getInts(0, 10, 5);

  expect(values.length).toBe(5);
  values.forEach((v) => {
    expect(v).toBeGreaterThanOrEqual(0);
    expect(v).toBeLessThanOrEqual(10);
  });
});
