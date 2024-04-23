#!/usr/bin/node
// get content of webpage and store it in afile 

const req = require('request');
const fs = require('fs');

req.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(process.argv[3], body, 'utf-8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
