exports.mining = id => console.info(`${id} starting to mine...`);

exports.alreadyMining = id => console.warn(`${id} is already mining!`);

exports.minedBlock = (id, blockchain) =>
  console.info(`${id} successfully mined: [${blockchain.getBlocksData()}]`);

exports.receivedHashedBlock = (id, blockchain) =>
  console.info(`${id} received/added block: [${blockchain.getBlocksData()}]`);

exports.retiring = id => console.info(`${id} retiring!`);
