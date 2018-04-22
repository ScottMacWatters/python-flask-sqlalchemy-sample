Simple Python app which saves IPs of visitors to a database, then displays the number of visitors. 

This app is intended to provide a jumping off point for educational purposes. 


To push to Heroku, run the following commands:

heroku create
heroku addons:create heroku-postgresql:hobby-dev
git push heroku master

These commands create a new Heroku project, add Postgres (free) to that project, then push this git repository into that heroku project and start the application. 