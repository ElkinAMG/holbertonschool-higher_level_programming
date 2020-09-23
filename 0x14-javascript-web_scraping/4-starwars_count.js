#!/usr/bin/node
const request = require('request');
let counter = 0;
const character = 'https://swapi-api.hbtn.io/api/people/18/';

request(process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
  }

  const films = JSON.parse(body).results;

  for (let x = 0; x < films.length; x++) {
    for (let y = 0; y < films[x].characters.length; y++) {
      if (films[x].characters[y] === character) {
        counter += 1;
      }
    }
  }

  console.log(counter);
});
