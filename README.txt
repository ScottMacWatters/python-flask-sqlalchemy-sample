Simple Python app which saves IPs of visitors to a database, then displays the number of visitors. 

This app is intended to provide a jumping off point for educational purposes. 


To push to Heroku, run the following:

heroku create
heroku addons:create heroku-postgresql:hobby-dev
git push heroku master