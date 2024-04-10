#!/usr/bin/node
const request = require('request');
const apiUrl = 'https://jsonplaceholder.typicode.com/todos';

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  }

  const todos = JSON.parse(body);
  const completedTasksByUserId = {};

  todos.forEach((todo) => {
    if (todo.completed) {
      if (!completedTasksByUserId[todo.userId]) {
        completedTasksByUserId[todo.userId] = 1;
      } else {
        completedTasksByUserId[todo.userId] += 1;
      }
    }
  });

  console.log(completedTasksByUserId);
});
