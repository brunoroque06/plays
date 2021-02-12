const R = require('ramda');

const getInt = R.curry((min, max) =>
  Math.round(Math.random() * (max - min) + min),
);

module.exports = { getInt };
