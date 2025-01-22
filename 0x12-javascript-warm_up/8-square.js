#!/usr/bin/node

const args = process.argv.slice(2);
const x = parseInt(args[0]);

if (Number.isInteger(x)) {
  for (let i = 1; i <= x; i++) {
    for (let a = 1; a <=x; a++) {
      console.log('X');
    }
  }
} else {
  console.log('Missing size');
}
