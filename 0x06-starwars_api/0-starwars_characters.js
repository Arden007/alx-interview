#!/usr/bin/node
/**
    A script that prints all characters of a Star Wars movie:
*/

// Check if the correct number of arguments is provided
if (process.argv.length !== 3) {
  console.error("Usage: ./0-starwars_characters.js <movie_id>");
  process.exit(1);
}

const request = require("request");

const baseUrl = "https://swapi-api.alx-tools.com/api/";

/**
 * Retrieves and prints the characters of a Star Wars movie.
 * @param {number} movieId - The ID of the Star Wars movie.
 */
function getMovieCharacters(movieId) {
  // Construct the URL for the specified movie
  const filmUrl = `${baseUrl}films/${movieId}/`;

  // Send a request to the SWAPI to get movie data
  request(filmUrl, (error, response, body) => {
    if (error) {
      console.error("Error:", error);
    } else {
      // Parse the response body into JSON
      const filmData = JSON.parse(body);
      // Extract the URLs of the characters from the movie data
      const charactersUrls = filmData.characters;

      // For each character URL, send a request to get character data
      charactersUrls.forEach((characterUrl) => {
        request(characterUrl, (charError, charResponse, charBody) => {
          if (charError) {
            console.error("Error:", charError);
          } else {
            // Parse the character data and print the character name
            const characterData = JSON.parse(charBody);
            console.log(characterData.name);
          }
        });
      });
    }
  });
}

// Retrieve movie ID from command line arguments and call the function
const movieId = process.argv[2];
getMovieCharacters(movieId);
