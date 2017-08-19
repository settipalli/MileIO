# MileIO

A miles logging application written in Python Flask that allows a customer to log his travel miles in a Google Spreadsheet.

# Project Structure

    ├── Procfile
    ├── README.md
    ├── __init__.py
    ├── requirements.txt
    ├── routes.py
    ├── static
    │   ├── README.md
    │   ├── css
    │   ├── img
    │   │   ├── README.md
    │   │   └── screenshots
    │   └── js
    └── templates
        ├── README.md
        └── layout.html

**routes.py**

Contains the applications main code.

**requirements.txt**

Generated using `pip freeze` command. Contains the list of python packages that are required to be pre-installed for the application to execute without errors.

This file is also required for a successful heroku deployment.

**Procfile**

Contains a list of commands that inform heroku what to execute when the application is deployed so as to start the application.

**static**

The application static files are stored in this folder.

**templates**

The application's HTML files are stored in this folder.

# Heroku deployment workflow

1. Install heroku toolbelt. Follow the steps outlined at: https://devcenter.heroku.com/articles/heroku-cli
2. Install `gunicorn`
3. Create requirements.txt using the command `pip freeze > requirements.txt`  
4. Create `Procfile` with the below contents:

        web: gunicorn routes:app
    
5. Create a heroku app: `heroku create <appname>`
6. Generate an API key for the project through `https://console.developers.google.com`
7. Save the API key as the `GOOGLE_API_KEY` config (environment) variable using the command: `heroku config:set GOOGLE_API_KEY=<key>`
8. Set the value of the `MODE` config (environment) variable as 'production' (without quotes) using the command: `heroku config:set MODE=production` and verify that the config variables are set appropriately using the command: `heroku config`
9. Push to heroku git repository: `git push heroku master`
10. Verify the deployment: `heroku open`

# Tools and references utilized

1. Generate favicons: https://realfavicongenerator.net

2. Terms and conditions reference: https://topnonprofits.com/terms-of-service/, available under the [Creative Commons Sharealike](http://creativecommons.org/licenses/by-sa/3.0/) license.

3. Privacy Policy reference: https://topnonprofits.com/privacy-policy/, available under the [Creative Commons Sharealike](http://creativecommons.org/licenses/by-sa/3.0/) license.
