const Blockchain = require("./blockchain");
const Blocks = require("./blocks");
const Miner = require("./miner");
const ProofOfWork = require("./proof-of-work");
const Rx = require("rxjs");

const bufferSize = 16;
const unconfirmedData = new Rx.ReplaySubject(bufferSize);
const broadcastedBlocks = new Rx.ReplaySubject(bufferSize);

const proofOfWork = ProofOfWork.prove(3, 100);

const gimli = new Miner(
  "Gimli",
  new Blockchain(),
  unconfirmedData,
  Blocks.createNextHashedBlock,
  proofOfWork,
  Blocks.isHashedBlockValid,
  broadcastedBlocks
);

gimli.mine();

unconfirmedData.next("I");
unconfirmedData.next("am");
unconfirmedData.next("mining");
