const R = require('ramda');

export const getInt = R.curry((min, max) =>
  Math.round(Math.random() * (max - min) + min),
);

export function getNumber(num) {
  return num;
}
