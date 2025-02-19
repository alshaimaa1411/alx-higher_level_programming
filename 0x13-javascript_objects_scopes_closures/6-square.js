#!/usr/bin/node

const Square4 = require('./5-square');

class Square extends Square4 {
  charPrint(c){
    if (c === undefined){
      c = 'X'
    }
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let a = 0; a < this.width; a++) {
        row += c;
      }
      console.log(row);
    }
  }
}
module.exports = Square;
