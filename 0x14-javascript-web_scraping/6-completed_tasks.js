#!/usr/bin/node
const request = require('request');

request(process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
  }

  const data = JSON.parse(body);
  const users = {};

  for (let i = 0; i < data.length; i++) {
    users[data[i].userId] = 0;
  }

  for (let i = 0; i < data.length; i++) {
    if (data[i].completed) {
      users[data[i].userId] += 1;
    }
  }

  console.log(users);
});
