#!/bin/bash

# Check if the correct number of arguments is provided
if (( $# < 3 || (($# - 1) % 2 != 0) )); then
  echo "Invalid number of arguments. Usage: $0 <word1> <replace1> [<word2> <replace2> ...] <filename>"
  exit 1
fi

filename="${!#}"  # Get the last argument, which is the filename

# Loop through the pairs of words and replacements
for (( i = 1; i <= $# - 1; i+=2 )); do
  word="${!i}"         # Get the word to be replaced
  replace=$(eval echo "\${$((i+1))}")  # Get the word to replace with

  # Replace standalone occurrences of the word in the file
  sed -i "s/\b${word}\b/${replace}/g" "$filename"
done
