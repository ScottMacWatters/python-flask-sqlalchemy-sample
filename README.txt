Simple Python app which saves IPs of visitors to a database, then displays the number of visitors. 

This app is intended to provide a jumping off point for educational purposes. 

To get this locally, use the following steps:

1. Install Git 
    visit https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

2. Clone this repository to your local machine
    Pick a directory you want to work in, then run
    git clone https://github.com/ScottMacWatters/python-flask-sqlalchemy-sample.git

3. Create a Heroku account (free)
    https://signup.heroku.com

4. Install Heroku CLI
    https://devcenter.heroku.com/articles/heroku-cli

5. Login to HerokuCLI
    Run:
    heroku login
    (provide credentials when prompted)

6. Create a Heroku project:
    heroku create 
    (optionally, you can provide a unique name, but it generates one for you that is pretty easy)

7. Add a Database to your Heroku project
    heroku addons:create heroku-postgresql:hobby-dev

8. Use git to push this code into your heroku project. This will start the project and give you a URL to see the project
    git push heroku master

9. Begin watching the logs to see your traffic
    heroku logs --tail 


Short list:
    * Install Git, Heroku
    * Run the following:
        cd /some/directory/
        heroku login
        git clone https://github.com/ScottMacWatters/python-flask-sqlalchemy-sample.git
        cd python-flask-sqlalchemy-sample/
        heroku create
        heroku addons:create heroku-postgresql:hobby-dev
        git push heroku master
        heroku logs --tail
    * Visit your application in the browser or use curl:
        curl <url> 