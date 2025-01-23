#!/usr/bin/node

const args = process.argv.slice(2);
const x = parseInt(args[2]);

exports.addMeMaybe = function (number, theFunction) {
   return theFunction(number + x);
};
