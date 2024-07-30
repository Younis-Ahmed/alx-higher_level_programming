#!/usr/bin/node
const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], { encoding: 'utf8' }, err => {
  if (err) console.log(err);
});
