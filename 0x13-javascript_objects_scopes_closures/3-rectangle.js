#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    for (let i = 0; i < this.height; i++) {
        let row = '';
        for (let a = 0; a < this.width; a++) {
            row += 'X';
        }
        console.log(row);
    }
  }
}
  //module.exports = Rectangle;
  const r1 = new Rectangle (2, 3);
  r1.print();