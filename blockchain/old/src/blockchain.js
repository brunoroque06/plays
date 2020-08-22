const Block = require("./block");

module.exports = class Blockchain {
  constructor() {
    this.hashedBlocks = [Block.createGenesisHashedBlock()];
  }

  push(hashedBlock) {
    this.hashedBlocks.push(hashedBlock);
  }

  getLast() {
    return this.hashedBlocks[this.hashedBlocks.length - 1];
  }

  doesBlockExist(data) {
    const index = this.hashedBlocks.findIndex(
      hashedBlock => hashedBlock.block.data === data
    );
    return index > -1;
  }

  getBlocksData() {
    return this.hashedBlocks.map(hashedBlock => hashedBlock.block.data);
  }
};
