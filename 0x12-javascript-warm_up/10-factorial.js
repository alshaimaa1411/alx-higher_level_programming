#!/usr/bin/node

const args = process.argv.slice(2);
const x = parseInt(args[0]);

function factorial (a) {
    let x = a;
    if (a === NaN){
        console.log(1);
    } else {
        factorial(a * a-1)
    }
}