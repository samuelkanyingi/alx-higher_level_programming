#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get(url, function (response) {
  if (response.statusCode === 200) {
    console.log('code: ', response.statusCode);
  } else {
    console.log('code: ', response.statusCode);
  }
}
);
