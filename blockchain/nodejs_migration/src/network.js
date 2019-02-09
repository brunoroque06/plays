const Rx = require("rxjs");

module.exports = class BroadcastedBlocks {
  constructor() {
    this.blocks = new Rx.ReplaySubject(32);
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
