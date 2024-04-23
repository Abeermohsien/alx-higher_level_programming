#!/usr/bin/node
// compute snum of tasks completed by user id

const req = require('request');

req.get(process.argv[2], { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const completedtask = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (!completedtask[todo.userId]) {
        completedtask[todo.userId] = 1;
      } else {
        completedtask[todo.userId] += 1;
      }
    }
  });
  console.log(completedtask);
});
