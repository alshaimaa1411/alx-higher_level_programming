#!/usr/bin/node

const args = process.argv.slice(2);
const x = parseInt(args[0]);

function factorial (a) {
  if (a === NaN){
    return 1;
  } 
  if (a <= 1) {
    return 1;
  } 
  return a * factorial(a-1)
}

factorial(Number(x));