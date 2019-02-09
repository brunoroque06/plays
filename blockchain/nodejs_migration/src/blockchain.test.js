const Blockchain = require("./blockchain");

test("When initializing Blockchain, then it contains a Genesis block", () => {
  const blockchain = new Blockchain();
  expect(blockchain.getLast()).not.toBeUndefined();
});

test("When 2 blocks are added, then Blockchain contains 3 blocks", () => {
  const blockchain = new Blockchain();
  const block0 = { data: "0" };
  const block1 = { data: "1" };

  blockchain.push(block0);
  blockchain.push(block1);

  expect(blockchain.hashedBlocks[1]).toBe(block0);
  expect(blockchain.hashedBlocks[2]).toBe(block1);
});

test("When searching for non existing block, then false", () => {
  const blockchain = new Blockchain();
  const block = { block: { data: "0" } };

  blockchain.push(block);
  const doesBlockExist = blockchain.doesBlockExist("1");

  expect(doesBlockExist).toBeFalsy();
});

test("When searching for existing block, then true", () => {
  const blockchain = new Blockchain();
  const block0 = { block: { data: "0" } };
  const block1 = { block: { data: "1" } };

  blockchain.push(block0);
  blockchain.push(block1);

  const doesBlockExist = blockchain.doesBlockExist("1");

  expect(doesBlockExist).toBeTruthy();
});

test("When getting last block, then right block is returned", () => {
  const blockchain = new Blockchain();
  const block0 = { block: { data: "0" } };
  const block1 = { block: { data: "1" } };

  blockchain.push(block0);
  blockchain.push(block1);
  const lastBlock = blockchain.getLast();

  expect(lastBlock).toBe(block1);
});
