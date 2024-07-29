#!/usr/bin/node
const request = require('request');
const fs = require('fs');

request(process.argv[2], (err, resp, body) => {
  if (err) {
    return err;
  }

  if (resp.statusCode !== 200) {
    return resp.statusCode;
  }

  fs.writeFile(process.argv[3], body, { encoding: 'utf-8' }, err => {
    if (err) {
      return err;
    }
  });
});
