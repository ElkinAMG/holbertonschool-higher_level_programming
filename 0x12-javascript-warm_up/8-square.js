#!/usr/bin/node
const size = Number(process.argv[2]);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let row = 0; row < size; row++) {
    console.log('X'.repeat(size));
  }
}
