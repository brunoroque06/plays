const Blockchain = require("./blockchain");
const Block = require("./block");
const Miner = require("./miner");
const ProofOfWork = require("./proof-of-work");
const Rx = require("rxjs");

const bufferSize = 16;
const unconfirmedData = Rx.of("I", "am", "mining", Rx.asyncScheduler);
const broadcastedBlocks = new Rx.ReplaySubject(bufferSize);

const proofOfWork = ProofOfWork.prove(4);

const gimli = new Miner(
  "Gimli",
  new Blockchain(),
  unconfirmedData,
  Block.createNextHashedBlock,
  proofOfWork,
  Block.isHashedBlockValid,
  broadcastedBlocks
);

const thorin = new Miner(
  "Thorin",
  new Blockchain(),
  unconfirmedData,
  Block.createNextHashedBlock,
  proofOfWork,
  Block.isHashedBlockValid,
  broadcastedBlocks
);

gimli.mine();
thorin.mine();

thorin.retire();
