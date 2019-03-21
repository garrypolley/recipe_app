# Recipe App

This is code for a simple recipe app. It helps me keep track of my personal recipies. One day I may
open up the running version of the site for others to host their recipes too.

## Run the code

1. `docker-compose build`
1. `docker-compose run recipe_app python ./manage.py migrate`
1. On windows wait for popup to "share" the drive
1. `docker-compose up`
1. App running on http://localhost:8000

## Building the app

1. `docker build . -t garrypolley/recipe-app:1.1.1`
1. `docker push garrypolley/recipe-app:1.1.1`
