const Blockchain = require("./blockchain");
const Blocks = require("./blocks");
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
  Blocks.createNextHashedBlock,
  proofOfWork,
  Blocks.isHashedBlockValid,
  broadcastedBlocks
);

const thorin = new Miner(
  "Thorin",
  new Blockchain(),
  unconfirmedData,
  Blocks.createNextHashedBlock,
  proofOfWork,
  Blocks.isHashedBlockValid,
  broadcastedBlocks
);

gimli.mine();
thorin.mine();
