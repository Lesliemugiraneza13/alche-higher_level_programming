#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
const wedgeUrl = 'https://swapi-api.alx-tools.com/api/people/18/';

request(url, (err, response, body) => {
  if (!err) {
    const films = JSON.parse(body).results;
    const count = films.filter(
      (film) => film.characters.includes(wedgeUrl)
    ).length;
    console.log(count);
  }
});
