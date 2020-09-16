#!/usr/bin/node

if ((process.argv.length - 2) === 0 || (process.argv.length - 2) === 1) {
  console.log('0');
} else {
  const array = [];
  process.argv.forEach((item, i) => {
    if (i > 1) {
      array.push(Number(item));
    }
    console.log(Math.max(...array));
  });
}
