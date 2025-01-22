#!/usr/bin/node

const args = process.argv.slice(2);
const a = parseInt(args[0]);
const b = parseInt(args[1]);

function add(a, b){
 const x = a + b;
 console.log(x);
}
