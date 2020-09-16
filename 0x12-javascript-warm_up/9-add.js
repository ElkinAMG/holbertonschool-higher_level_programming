#!/usr/bin/node

const numberOne = Number(process.argv[2]);
const numberTwo = Number(process.argv[3]);

function add (a, b) {
  return a + b;
}

console.log(add(numberOne, numberTwo));
