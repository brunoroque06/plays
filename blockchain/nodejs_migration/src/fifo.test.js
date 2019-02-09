const Fifo = require("./fifo");

test("Fifo returns elements in the right order", () => {
  const fifo = new Fifo();
  const first = "first";
  const second = 2;

  fifo.add(first);
  fifo.add(second);

  expect(fifo.get()).toBe(first);
  expect(fifo.get()).toBe(second);
});
