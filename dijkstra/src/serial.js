const R = require('ramda');

const abc = 'abcdefghijklmnopqrstuvwxyz';

const toCharInts = R.curry((chars, remainder) =>
  R.ifElse(
    R.lt(R.__, R.length(abc)),
    R.append(R.__, chars),
    R.pipe(R.modulo(R.__, R.length(abc)), (newRemainder) =>
      toCharInts(R.append(newRemainder, chars), newRemainder),
    ),
  )(remainder),
);

const toChars = R.pipe(R.map(R.nth(R.__, abc)));

const toString = R.pipe(toCharInts([]), toChars, R.reduce(R.concat, ''));

module.exports = {
  toString,
};
