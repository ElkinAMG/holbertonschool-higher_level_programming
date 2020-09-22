#!/usr/bin/node
const request = require('request');
const chapter = process.argv[2];

request(`https://swapi-api.hbtn.io/api/films/${chapter}`, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  console.log(JSON.parse(body).title);
});
