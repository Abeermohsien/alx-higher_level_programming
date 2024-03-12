#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let n = 0; n < this.height; n++) {
      let space = '';
      for (let m = 0; m < this.width; m++) {
        space += c;
      }
      console.log(space);
    }
  }
}

module.exports = Square;
