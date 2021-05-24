let R = require('ramda');

const abc = 'abcdefghijklmnopqrstuvwxyz'.split('');

function divide(dividend) {
  return {
    quotient: Math.floor(R.divide(dividend, R.length(abc))),
    remainder: R.modulo(dividend, R.length(abc)),
  };
}

let toCharInts = R.curry((chars, dividend) =>
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

let toChars = R.pipe(R.map(R.nth(R.__, abc)));

let toString = R.pipe(toCharInts([]), toChars, R.reduce(R.concat, ''));

let sumIndexes = R.curry((factor, acc) => {
  const part = abc.length ** acc.index * factor;
  return {
    sum: R.add(acc.sum, part),
    index: R.inc(acc.index),
  };
});

let toInt = R.pipe(
  R.split(''),
  R.map((l) => R.findIndex(R.equals(l), abc)),
  R.reduceRight(sumIndexes, { sum: 0, index: 0 }),
  (s) => s.sum,
);

module.exports = { toInt, toString };
