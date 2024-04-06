#!/usr/bin/env sh

set -e

npm run build

cd dist

cp index.html 404.html

git init 
git add .
git commit -m "deploy to gitpage"

git push -f gh-pages

cd -
