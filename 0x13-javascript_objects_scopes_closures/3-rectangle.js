#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let n = 0; n < this.height; n++) {
      let space = '';
      for (let j = 0; j < this.width; j++) {
        space += 'X';
      }
      console.log(space);
    }
  }
}

module.exports = Rectangle;
