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
      for (let m = 0; m < this.width; m++) {
        space += '';
      }
      console.log(space);
    }
  }

  rotate () {
    const mm = this.width;
    this.width = this.height;
    this.height = mm;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }

module.exports = Rectangle
