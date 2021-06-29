let serial = require('./serial');

it('map to string', () => {
  expect(serial.toString(0)).toBe('a');
  expect(serial.toString(10)).toBe('k');
  expect(serial.toString(26)).toBe('ba');
  expect(serial.toString(28)).toBe('bc');
  expect(serial.toString(52)).toBe('ca');
  expect(serial.toString(55)).toBe('cd');
});

it('map to integer', () => {
  expect(serial.toInt('a')).toBe(0);
  expect(serial.toInt('s')).toBe(18);
  expect(serial.toInt('bd')).toBe(29);
  expect(serial.toInt('ct')).toBe(71);
});
