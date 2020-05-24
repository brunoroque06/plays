const R = require('ramda');

const abc = 'abcdefghijklmnopqrstuvwxyz'.split('');

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

const sumIndexes = R.curry((factor, acc) => {
  const part = R.length(abc) ** acc.index * factor;
  return { sum: R.add(acc.sum, part), index: R.inc(acc.index) };
});

const toInt = R.pipe(
  R.split(''),
  R.map((l) => R.findIndex(R.equals(l), abc)),
  R.reduceRight(sumIndexes, { sum: 0, index: 0 }),
  R.prop('sum'),
);

module.exports = {
  toInt,
  toString,
};
