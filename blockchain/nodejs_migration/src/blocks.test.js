const blocks = require("./blocks");

test("Genesis block creation", () => {
  const genesis = blocks.createGenesisBlock();

  expect(genesis.index).toEqual(0);
  expect(genesis.previousHash).toEqual(undefined);
  expect(genesis.data).toEqual("Genesis");
  expect(genesis.nonce).toEqual(0);
});

test("Next block creation", () => {
  const previousBlock = {
    index: 0,
    hash: "hash"
  };
  const data = "I am data";
  const block = blocks.createNextBlock(previousBlock, data);

  expect(block.index).toEqual(1);
  expect(block.previousHash).toEqual(previousBlock.hash);
  expect(block.data).toEqual(data);
  expect(block.nonce).toEqual(0);
});

test("Hash block", () => {
  const block = { data: "I am a block" };

  const hashedBlock = blocks.hashBlock(block);

  expect(hashedBlock.block).toEqual(block);
  expect(hashedBlock.hash).not.toEqual(undefined);
});
