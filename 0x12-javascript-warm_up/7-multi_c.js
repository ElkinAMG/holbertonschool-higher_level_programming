#!/usr/bin/node
let x = process.argv[1];
if (isNaN(x)) console.log('Missing number of occurrences');
else {
  for (; x > 0; x--) console.log('C is fun');
}
