#!/usr/bin/node
// get request status

const req = require('request');
const URL = process.argv[2];
req.get(URL, function (error, response) {
  if (error) {
    console.log(error);
  } else {
    console.log('code:' + ' ' + response.statusCode);
  }
});
