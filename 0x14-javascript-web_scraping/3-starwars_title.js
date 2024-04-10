#!/usr/bin/node
const request = require('request');

// Extract the movie ID from command-line arguments
const movieId = process.argv[2];

// Construct the URL for the Star Wars API endpoint
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Status Code:', response.statusCode);
  } else {
    const movieData = JSON.parse(body);
    console.log(movieData.title);
  }
});
