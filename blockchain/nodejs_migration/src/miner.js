minerLogger = require("./miner-logger");

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
      this.subscribeUnconfirmedData();
      this.subscribeBroadcastedBlocks();
    } else {
      minerLogger.mining(this.id);
    }
  }

  subscribeUnconfirmedData() {
    this.unconfirmedDataSubscription = this.unconfirmedData.subscribe(data =>
      this.processUnconfirmedData(data)
    );
  }

  processUnconfirmedData(data) {
    if (!this.blockchain.doesBlockExist(data)) {
      const lastBlock = this.blockchain.getLast();
      const nextHashedBlock = this.createNextHashedBlock(lastBlock, data);
      if (this.proofOfWork(nextHashedBlock.hash)) {
        this.blockchain.push(nextHashedBlock);
        this.broadcastedBlocks.next(nextHashedBlock);
        minerLogger.minedBlock(this.id, this.blockchain);
      } else {
        this.processUnconfirmedData(data);
      }
    }
  }

  subscribeBroadcastedBlocks() {
    this.broadcastedBlocksSubscription = this.broadcastedBlocks.subscribe(
      hashedBlock => this.processBroadcastedBlocks(hashedBlock)
    );
  }

  processBroadcastedBlocks(hashedBlock) {
    minerLogger.receivedHashedBlock(this.id, hashedBlock);
    if (
      !this.blockchain.doesBlockExist(hashedBlock.block.data) &
      this.isHashedBlockValid(hashedBlock)
    ) {
      this.blockchain.push(hashedBlock);
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
