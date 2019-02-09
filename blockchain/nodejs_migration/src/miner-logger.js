exports.mining = id => console.info(`${id} starting to mine...`);

exports.alreadyMining = id => console.warn(`${id} is already mining!`);

exports.minedBlock = (id, blockchain) =>
  console.info(
    `${id} successfully mined block: [${blockchain.getBlocksData()}]`
  );

exports.receivedHashedBlock = (id, hashedBlock) =>
  console.info(`${id} received block: ${hashedBlock.block.data}`);

exports.retiring = id => console.info(`${id} retiring!`);
