#!/bin/bash
for file in components/*.tsx pages/*.tsx; do
  sed -i 's/requiblue/required/g' "$file"
  sed -i 's/Requiblue/Required/g' "$file"
  sed -i 's/hundblue/hundred/g' "$file"
  sed -i 's/Hundblue/Hundred/g' "$file"
  sed -i 's/cblue/cred/g' "$file"
  sed -i 's/shablue/shared/g' "$file"
  sed -i 's/blueirect/redirect/g' "$file"
  sed -i 's/blueuce/reduce/g' "$file"
done
