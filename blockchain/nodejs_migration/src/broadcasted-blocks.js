const Rx = require("rxjs");

module.exports = class BroadcastedBlocks {
  constructor(bufferSize = 32) {
    this.blocks = new Rx.ReplaySubject(bufferSize);
  }

  broadcast(block) {
    this.blocks.next(block);
  }

  get() {
    return this.blocks;
  }

  close() {
    this.blocks.complete();
  }
};
