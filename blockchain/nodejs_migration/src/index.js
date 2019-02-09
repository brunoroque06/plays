function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function animate() {
  for (let i = 0; i < 10; i++) {
    console.log(`Hello async: ${i}`);
    await sleep(100);
  }
}

// animate();

const Fifo = require("./fifo");
const unconfirmedData = new Fifo();

const BroadcastedBlocks = require("./broadcasted-blocks");
const broadcastedBlocks = new BroadcastedBlocks();

const Miner = require("./miner");
const miner = new Miner(unconfirmedData, broadcastedBlocks);

unconfirmedData.add("data");
unconfirmedData.add(18);
