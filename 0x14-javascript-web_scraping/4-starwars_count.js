#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Status code:', response.statusCode);
    return;
  }

  try {
    const results = JSON.parse(body).results;
    const count = results.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0);
    console.log(count);
  } catch (parseError) {
    console.error('Parsing error:', parseError);
  }
});

