#!/usr/bin/node
// number of moves that wedge present
const req = require('request');
let n = 0;

req.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const content = JSON.parse(body);
    content.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(18)) {
          n += 1;
        }
      });
    });
    console.log(n);
  }
});
