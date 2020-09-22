#!/usr/bin/node
const SSquare = require('./5-square');

class Square extends SSquare {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      console.log(`${c === undefined ? 'X' : c}`.repeat(this.width));
    }
  }
}

module.exports = Square;
