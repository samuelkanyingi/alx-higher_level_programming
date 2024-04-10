#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }
  request.get(apiUrl, (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      const movie = JSON.parse(body);
      const characters = movie.characters;
      for (const character of characters) {
        request.get(character, (error, response, body) => {
          if (error) {
            console.log(error);
          } else {
            const character = JSON.parse(body);
            console.log(character.name);
          }
        });
      }
    }
  });
});
