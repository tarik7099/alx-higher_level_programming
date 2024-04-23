#!/usr/bin/node

const fs = require('fs');

// Extract command line arguments
const [, , filePath, content] = process.argv;

// Write the content to the file
fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    // If an error occurred during writing, print the error object
    console.error(err);
  } else {
    console.log(`Content has been written to ${filePath}`);
  }
});
