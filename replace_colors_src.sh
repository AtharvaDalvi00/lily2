#!/bin/bash
for file in src/*.tsx; do
  sed -i 's/emerald/sky/g' "$file"
  sed -i 's/teal/sky/g' "$file"
  
  sed -i 's/indigo/blue/g' "$file"
  sed -i 's/rose/blue/g' "$file"
  sed -i 's/red/blue/g' "$file"
  sed -i 's/orange/blue/g' "$file"
  sed -i 's/amber/blue/g' "$file"
  sed -i 's/green/sky/g' "$file"
  sed -i 's/purple/blue/g' "$file"
  sed -i 's/pink/sky/g' "$file"
  sed -i 's/cyan/sky/g' "$file"
  sed -i 's/fuchsia/blue/g' "$file"
  sed -i 's/violet/blue/g' "$file"
done
