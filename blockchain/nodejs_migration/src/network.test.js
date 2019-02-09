const BroadcastedBlocks = require("./network");

test("Messages are delivered in order", done => {
  const blocks = new BroadcastedBlocks();

  blocks.broadcast(1);
  blocks.broadcast(2);
  blocks.close();

  let block = 1;
  blocks.get().subscribe({
    next: b => expect(b).toBe(block++),
    complete: () => done()
  });
});

test("Every subscriber receives the same messages", done => {
  const blocks = new BroadcastedBlocks();

  blocks.broadcast(1);
  blocks.close();

  blocks.get().subscribe(b => {
    expect(b).toBe(1);
    blocks.get().subscribe(b => {
      expect(b).toBe(1);
      done();
    });
  });
});
