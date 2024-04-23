#!/usr/bin/node
// prints title of star wars 

const req = require('request');
const URL = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

req.get(URL, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const content = JSON.parse(body);
    console.log(content.title);
  }
});
