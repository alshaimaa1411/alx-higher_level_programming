#!/usr/bin/node

let List = require('./100-data').list;

let map1 = List.map((x) => x * List.indexOf(x));
console.log(map1);
