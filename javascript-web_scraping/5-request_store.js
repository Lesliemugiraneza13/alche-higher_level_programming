#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const path = process.argv[3];

request(url, (err, response, body) => {
  if (!err) {
    fs.writeFile(path, body, 'utf8', (writeErr) => {
      if (writeErr) {
        console.log(writeErr);
      }
    });
  }
});
