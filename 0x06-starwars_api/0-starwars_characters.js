#!/usr/bin/node

const request = require('request');

const baseUrl = 'https://swapi-api.alx-tools.com/api/';

/**
 * Retrieves and prints the characters of a Star Wars movie.
 * @param {number} movieId - The ID of the Star Wars movie.
 */
function getMovieCharacters(movieId) {
  const filmUrl = `${baseUrl}films/${movieId}/`;

  request(filmUrl, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    } else {
      const filmData = JSON.parse(body);
      const charactersUrls = filmData.characters;

      charactersUrls.forEach((characterUrl) => {
        request(characterUrl, (charError, charResponse, charBody) => {
          if (charError) {
            console.error('Error:', charError);
          } else {
            const characterData = JSON.parse(charBody);
            console.log(characterData.name);
          }
        });
      });
    }
  });
}

if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
getMovieCharacters(movieId);
