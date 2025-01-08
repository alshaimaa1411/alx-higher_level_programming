#!/usr/bin/node

const args = process.argv.slice(2);
const x = parseInt(args[0]);

if (Number.isInteger(x)) {
  for (let i = 1; i <= x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
