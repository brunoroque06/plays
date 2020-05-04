const R = require('ramda');

// Math.round(Math.random() * (max - min) + min)
const getInt = R.curry((min, max) =>
  R.pipe(
    R.subtract(min),
    R.multiply(Math.random()),
    R.add(min),
    Math.round,
  )(max),
);

module.exports = {
  getInt,
};
