const minerLogger = require("./miner-logger");
const RxOperators = require("rxjs/operators");

module.exports = class Miner {
  constructor(
    id,
    blockchain,
    unconfirmedData,
    createNextHashedBlock,
    proofOfWork,
    isHashedBlockValid,
    broadcastedBlocks
  ) {
    this.id = id;
    this.blockchain = blockchain;
    this.unconfirmedData = unconfirmedData;
    this.createNextHashedBlock = createNextHashedBlock;
    this.proofOfWork = proofOfWork;
    this.isHashedBlockValid = isHashedBlockValid;
    this.broadcastedBlocks = broadcastedBlocks;

    this.unconfirmedDataSubscription = undefined;
    this.broadcastedBlocksSubscription = undefined;
  }

  mine() {
    if (!this.unconfirmedDataSubscription) {
      minerLogger.mining(this.id);
      this.subscribeBroadcastedBlocks();
      this.subscribeUnconfirmedData();
    } else {
      minerLogger.mining(this.id);
    }
  }

  subscribeUnconfirmedData() {
    this.unconfirmedDataSubscription = this.unconfirmedData
      .pipe(RxOperators.concatMap(data => this.processUnconfirmedData(data)))
      .subscribe();
  }

  async processUnconfirmedData(data) {
    console.log(`${this.id} got ${data}`);
    const lastBlock = this.blockchain.getLast();
    while (!this.blockchain.doesBlockExist(data)) {
      this.tryToMineNextBlock(lastBlock, data);
    }
  }

  tryToMineNextBlock(lastBlock, data) {
    const nextHashedBlock = this.createNextHashedBlock(lastBlock, data);
    if (this.proofOfWork(nextHashedBlock.hash)) {
      this.blockchain.push(nextHashedBlock);
      this.broadcastedBlocks.next(nextHashedBlock);
      minerLogger.minedBlock(this.id, this.blockchain);
    }
  }

  subscribeBroadcastedBlocks() {
    this.broadcastedBlocksSubscription = this.broadcastedBlocks.subscribe(
      hashedBlock => this.processBroadcastedBlocks(hashedBlock)
    );
  }

  processBroadcastedBlocks(hashedBlock) {
    if (
      !this.blockchain.doesBlockExist(hashedBlock.block.data) &
      this.isHashedBlockValid(hashedBlock)
    ) {
      this.blockchain.push(hashedBlock);
      minerLogger.receivedHashedBlock(this.id, this.blockchain);
    }
  }

  retire() {
    minerLogger.retiring(this.id);
    this.unconfirmedDataSubscription.unsubscribe();
    this.unconfirmedDataSubscription = undefined;
    this.broadcastedBlocksSubscription.unsubscribe();
    this.broadcastedBlocksSubscription = undefined;
  }
};
