// Rules
// - immutability
// - declarative (no loops, etc)
// - return objects from functions
// - control exceptions by returning [error, result]

// const req = name => {
//   throw new Error(`The value ${name} is required.`);
// };
// const doStuff = ( stuff = req('stuff') ) => {
//   ...
// }
const game = require('./src/game');

const result = game.playGame();

console.log(result);

// const increasePrice = (item, increaseBy) => {
//   // never ever do this
//   item.price += increaseBy;

//   return item;
// };

// const oldItem = { price: 10 };
// const newItem = increasePrice(oldItem, 3);

// // prints newItem.price 13
// console.log('newItem.price', newItem.price);

// // prints oldItem.price 13
// // unexpected?
// console.log('oldItem.price', oldItem.price);

// const obj = new Object();
