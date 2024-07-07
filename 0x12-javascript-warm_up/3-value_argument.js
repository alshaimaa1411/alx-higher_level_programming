#!/usr/bin/node
const x = process.argv.length;
let a = process.argv[2];
if (x === 2) {
	  console.log('No argument');
} else {
	console.log(a);
}
