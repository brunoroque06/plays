const serial = require('./serial');

test('map to string', () => {
  // expect(serial.mapToString(0)).toBe('a');
  // expect(serial.mapToString(10)).toBe('k');
  expect(serial.toString(26)).toBe('aa');
  expect(serial.toString(28)).toBe('ac');
  // expect(serial.mapToString(51)).toBe('ba');
  // expect(serial.mapToString(54)).toBe('bd');
});
