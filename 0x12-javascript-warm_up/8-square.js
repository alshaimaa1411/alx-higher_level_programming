#!/usr/bin/node

const args = process.argv.slice(2);
const x = parseInt(args[0]);

if (Number.isInteger(x)) {
  for (let i = 0; i < x; i++) {
    let z = '';
    for (let a = 0; a < x; a++) {
    z += 'X';
    }
  console.log(z);
  }
} else {
  console.log('Missing size');
}
