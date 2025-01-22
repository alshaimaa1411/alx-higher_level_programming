#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
    const arr = process.argv.silice(2).map(Number);
    arr.sort((a, b) => b - a);
    console.log(arr[1]);
}
