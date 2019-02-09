module.exports = class Fifo {
  constructor() {
    this.queue = [];
  }

  add(data) {
    this.queue.push(data);
  }

  get() {
    return this.queue.shift();
  }
};
