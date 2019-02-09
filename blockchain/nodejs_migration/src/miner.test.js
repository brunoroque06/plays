const Miner = require("./miner");
const Rx = require("rxjs");

test("When miner mines and retires, then it subscribes and unsubscribes", () => {
  const unconfirmedData = Rx.empty();
  const broadcastedBlocks = Rx.empty();
  const miner = new Miner(
    undefined,
    undefined,
    unconfirmedData,
    undefined,
    undefined,
    undefined,
    broadcastedBlocks
  );

  miner.mine();
  expect(miner.unconfirmedDataSubscription).not.toBeUndefined();
  expect(miner.broadcastedBlocksSubscription).not.toBeUndefined();

  miner.retire();
  expect(miner.unconfirmedDataSubscription).toBeUndefined();
  expect(miner.broadcastedBlocksSubscription).toBeUndefined();
});

test("Given data is not in Blockchain, when miner receives it, then miner creates hashed block", done => {
  const lastBlock = { data: "" };
  const blockchain = {
    doesBlockExist: _ => false,
    getLast: () => lastBlock,
    push: () => {}
  };
  const unconfirmedData = new Rx.ReplaySubject(1);
  const nextHashedBlock = { data: "" };
  const createNextHashedBlock = (_, __) => nextHashedBlock;
  const proofOfWork = _ => true;
  const broadcastedBlocks = new Rx.ReplaySubject(1);
  const miner = new Miner(
    undefined,
    blockchain,
    unconfirmedData,
    createNextHashedBlock,
    proofOfWork,
    undefined,
    broadcastedBlocks
  );

  miner.mine();

  broadcastedBlocks.forEach(hashedBlock => {
    expect(hashedBlock).toBe(nextHashedBlock);
    done();
  });
  unconfirmedData.next(1);
});

test("When miner receives new hash block, then miner inserts it into blockchain", done => {
  const nextHashedBlock = { block: { data: 0 } };
  const blockchain = {
    doesBlockExist: () => false,
    push: hashedBlock => {
      expect(hashedBlock).toBe(nextHashedBlock);
      done();
    }
  };
  const unconfirmedData = new Rx.ReplaySubject(1);
  const isHashBlockValid = _ => true;
  const broadcastedBlocks = new Rx.ReplaySubject(1);
  const miner = new Miner(
    undefined,
    blockchain,
    unconfirmedData,
    undefined,
    undefined,
    isHashBlockValid,
    broadcastedBlocks
  );

  miner.mine();

  broadcastedBlocks.next(nextHashedBlock);
});
