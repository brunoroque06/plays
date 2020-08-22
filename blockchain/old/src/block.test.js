const Block = require("./block");
const hash = require("object-hash");

test("Genesis block creation", () => {
  const genesis = Block.createGenesisHashedBlock();

  expect(genesis.block.index).toEqual(0);
  expect(genesis.block.previousHash).toEqual(undefined);
  expect(genesis.block.data).toEqual("Genesis");
  expect(genesis.block.nonce).toEqual(0);
  expect(genesis.hash).not.toBeUndefined();
});

test("Given a block, when creating next hashed block, then it is populated correctly", () => {
  const previousBlock = {
    index: 0,
    hash: "hash"
  };
  const data = "I am data";
  const hashedBlock = Block.createNextHashedBlock(previousBlock, data);

  expect(hashedBlock.block.index).toEqual(1);
  expect(hashedBlock.block.previousHash).toEqual(previousBlock.hash);
  expect(hashedBlock.block.data).toEqual(data);
  expect(hashedBlock.block.nonce >= 0).toBeTruthy();
  expect(hashedBlock.hash).not.toBeUndefined();
});

test("Given hash is not consistent with block, when validating hashed block, then false", () => {
  const hashedBlock = { block: { data: 0 }, hash: "123" };
  const isHashedBlockValid = Block.isHashedBlockValid(hashedBlock);
  expect(isHashedBlockValid).toBeFalsy();
});

test("Given hash is consistent with block, when validating hashed block, then true", () => {
  const block = { data: 0 };
  const hashedBlock = { block, hash: hash(block) };
  const isHashedBlockValid = Block.isHashedBlockValid(hashedBlock);
  expect(isHashedBlockValid).toBeTruthy();
});
