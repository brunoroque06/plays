const hash = require("object-hash");

exports.createGenesisBlock = () =>
  createBlock(0, new Date(), undefined, "Genesis", 0);

function createBlock(index, timestamp, previousHash, data, nonce) {
  return {
    index,
    timestamp,
    previousHash,
    data,
    nonce
  };
}

exports.createNextBlock = (previousBlock, data) =>
  createBlock(previousBlock.index + 1, new Date(), previousBlock.hash, data, 0);

exports.hashBlock = block => {
  return { block, hash: hash(block) };
};
