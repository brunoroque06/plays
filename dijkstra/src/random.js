let R = require('ramda');

function getInt(min, max) {
  return Math.round(Math.random() * (max - min) + min);
}

function getInts(min, max, n) {
  return R.range(min, max)
    .sort(() => Math.random() - Math.random())
    .slice(0, n);
}

module.exports = {
  getInt,
  getInts,
};
