#!/usr/bin/node

let number = Number(process.argv[2]);

if (isNaN(number)) number = 'Not a number';
console.log(`My number: ${number}`);
