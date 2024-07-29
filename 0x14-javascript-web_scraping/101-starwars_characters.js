#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];
const filmUrl = `https://swapi-api.hbtn.io/api/films/${filmId}`;

request(filmUrl, (error, response, body) => {
  if (!error) {
    const characterUrls = JSON.parse(body).characters;
    let index = 0;

    const processNextCharacter = () => {
      if (index < characterUrls.length) {
        const characterUrl = characterUrls[index];
        request(characterUrl, (error, response, body) => {
          if (!error) {
            const characterData = JSON.parse(body);
            const characterName = characterData.name;
            console.log(characterName);
          }

          index++;
          processNextCharacter();
        });
      }
    };

    processNextCharacter();
  }
});
