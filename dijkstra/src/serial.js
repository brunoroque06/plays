const R = require('ramda');

const abc = 'abcdefghijklmnopqrstuvwxyz';

function divide(dividend) {
  return {
    quotient: Math.floor(R.divide(dividend, R.length(abc))),
    remainder: R.modulo(dividend, R.length(abc)),
  };
}

const toCharInts = R.curry((chars, dividend) =>
  R.pipe(
    divide,
    R.ifElse(
      (division) => R.equals(division.quotient, 0),
      (division) => R.prepend(division.remainder, chars),
      (division) =>
        toCharInts(R.prepend(division.remainder, chars), division.quotient),
    ),
  )(dividend),
);

const toChars = R.pipe(R.map(R.nth(R.__, abc)));

const toString = R.pipe(toCharInts([]), toChars, R.reduce(R.concat, ''));

module.exports = {
  toString,
};
