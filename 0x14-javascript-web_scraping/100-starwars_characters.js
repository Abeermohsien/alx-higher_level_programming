#!/usr/bin/node

const req = require('request');
const id = process.argv[2];
const URL = `https://swapi-api.alx-tools.com/api/films/${id}`;

req.get(URL, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const content = JSON.parse(body);
    const characters = content.characters;
    // log cobsole for chara;
    for (const character of characters) {
      req.get(character, (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          const names = JSON.parse(body);
          console.log(names.name);
        }
      });
    }
  }
});
