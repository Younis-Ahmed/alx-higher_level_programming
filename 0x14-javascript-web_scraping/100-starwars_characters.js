#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];
const filmUrl = `https://swapi-api.hbtn.io/api/films/${filmId}`;

request(filmUrl, function (err, resp, body) {
  if (err) {
    console.err(err);
    return;
  }

  const filmData = JSON.parse(body);
  const characters = filmData.characters;

  characters.forEach(function (characterUrl) {
    request(characterUrl, function (err, resp, body) {
      if (err) {
        console.err(err);
        return;
      }

      const characterData = JSON.parse(body);
      const characterName = characterData.name;
      console.log(characterName);
    });
  });
});
