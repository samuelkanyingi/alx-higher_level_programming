#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
request(url, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  }
  const movie = JSON.parse(body);
  const characters = movie.characters;
  for (const character of characters) {
    request.get(character, (error, response, body) => {
      if (error) {
        console.log(error);
      } else {
        const movieName = JSON.parse(body);
        console.log(movieName.name);
      }
    });
  }
});
