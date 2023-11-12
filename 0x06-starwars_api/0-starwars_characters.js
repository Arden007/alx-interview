#!/usr/bin/node
/**
 * A script that prints all characters of a Star Wars movie.
 */

const request = require('request');

/**
 * Retrieves and prints the characters of a Star Wars movie.
 * @param {number} movieId - The ID of the Star Wars movie.
 */
async function getMovieCharacters(movieId) {
  const baseUrl = 'https://swapi-api.hbtn.io/api/';
  const filmUrl = `${baseUrl}films/${movieId}/`;

  try {
    // Send a request to the SWAPI to get movie data
    const filmData = await makeRequest(filmUrl);

    // Extract the URLs of the characters from the movie data
    const charactersUrls = filmData.characters;

    // For each character URL, send a request to get character data
    for (const characterUrl of charactersUrls) {
      const characterData = await makeRequest(characterUrl);
      console.log(characterData.name);
    }
  } catch (error) {
    console.error('Error:', error);
  }
}

/**
 * Makes an HTTP request and returns a Promise.
 * @param {string} url - The URL to make the request to.
 * @returns {Promise} - A promise that resolves with the parsed JSON response.
 */
function makeRequest(url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const data = JSON.parse(body);
        resolve(data);
      }
    });
  });
}

// Retrieve movie ID from command line arguments and call the function
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./refactored-starwars_characters.js <movie_id>');
  process.exit(1);
}

getMovieCharacters(movieId);
