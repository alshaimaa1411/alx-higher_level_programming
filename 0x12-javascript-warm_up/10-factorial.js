#!/usr/bin/node

const args = process.argv.slice(2);
const x = parseInt(args[0]);

function factorial (a) {
    if (a <= 1 || isNaN(a)) {
      return 1;
  } 
    return a * factorial(a - 1);
  return a * factorial(a-1)
}

console.log(factorial(Number(x)));

