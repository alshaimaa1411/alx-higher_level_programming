#!/usr/bin/node

const args = process.argv.slice(2);

if (args[0] == null){
    console.log('No argument');
}
else {
    let x = parseInt(args[0]);
    if (Number.isInteger(x)){
        console.log('My number: ' + x)
    }
    else{
        console.log('No argument');
    }
}