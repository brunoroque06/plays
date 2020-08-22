const hash = require("object-hash");
const nonceMaxValue = 10000;

exports.createGenesisHashedBlock = () =>
  hashBlock(createBlock(0, new Date(), undefined, "Genesis", 0));

hashBlock = block => {
  return { block, hash: hash(block) };
};

function createBlock(index, timestamp, previousHash, data, nonce) {
  return {
    index,
    timestamp,
    previousHash,
    data,
    nonce
  };
}

exports.createNextHashedBlock = (previousBlock, data) => {
  const nextBlock = createNextBlock(previousBlock, data);
  nextBlock.nonce = getRandomNonce();
  return hashBlock(nextBlock);
};

getRandomNonce = () => Math.floor(Math.random() * nonceMaxValue);

createNextBlock = (previousBlock, data) =>
  createBlock(previousBlock.index + 1, new Date(), previousBlock.hash, data, 0);

exports.isHashedBlockValid = hashedBlock =>
  hashedBlock.hash === hash(hashedBlock.block);
