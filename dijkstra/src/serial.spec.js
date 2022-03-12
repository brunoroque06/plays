let serial = require('./serial');

it('map to string', () => {
  expect(serial.toString(10)).toBe('k');
  expect(serial.toString(52)).toBe('ca');
});

it('map to integer', () => {
  expect(serial.toInt('a')).toBe(0);
  expect(serial.toInt('ct')).toBe(71);
});
