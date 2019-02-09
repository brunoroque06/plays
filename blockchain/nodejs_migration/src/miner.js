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
      console.info(`${this.id} starting to mine...`);
      this.subscribeUnconfirmedData();
      this.subscribeBroadcastedBlocks();
    } else {
      console.warn(`${this.id} is already mining!`);
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
        this.broadcastedBlocks.next(nextHashedBlock);
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
    console.info(
      `${this.id} received the following block: ${JSON.stringify(hashedBlock)}`
    );
    if (
      !this.blockchain.doesBlockExist(hashedBlock.block.data) &
      this.isHashedBlockValid(hashedBlock)
    ) {
      this.blockchain.push(hashedBlock);
    }
  }

  retire() {
    console.info(`Miner ${this.id} retiring!`);
    this.unconfirmedDataSubscription.unsubscribe();
    this.unconfirmedDataSubscription = undefined;
    this.broadcastedBlocksSubscription.unsubscribe();
    this.broadcastedBlocksSubscription = undefined;
  }
};
