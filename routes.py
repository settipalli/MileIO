from os import environ as env
from flask import Flask, render_template, request, session, redirect, url_for, abort
from flask_mail import Mail, Message
from flask_security import Security, SQLAlchemyUserDatastore, login_required, login_user, current_user
from requests import HTTPError
from requests_oauthlib import OAuth2Session
import ujson as json
from models import db, User, Role
from config import Config, Auth

# helper method
get_from_env = lambda key: env[key] if key in env else ''

app = Flask(__name__)
app.config.from_object(Config)
mail = Mail(app)
db.init_app(app)

# setup flask-security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# get a handle for the logger
log = app.logger


@app.route('/')
@login_required
def index():
    log.debug('rendering index.html')
    return render_template('index.html')


@app.route('/terms')
def terms():
    log.debug('rendering terms.html')
    return render_template('terms.html')


@app.route('/privacy')
def privacy():
    log.debug('rendering privacy.html')
    return render_template('privacy.html')


@app.route('/about')
def about():
    log.debug('rendering about.html')
    return render_template('about.html')


# helper routines

# create a fresh copy of the DB tables (DB should be present)
def init_db():
    with app.app_context():
        # SQLAlchemy now knows what the 'current' app is while within this block
        # therefore, you can now run:
        db.drop_all()
        db.create_all()
        # create a test user
        user_datastore.create_user(email=Config.ADMIN_MAIL_ID, password=Config.ADMIN_MAIL_PASSWORD)
        db.session.commit()
        log.info('Database created.')


if __name__ == '__main__':
    if 'MODE' in env and env['MODE'] == 'production':
        app.run()
    else:
        from werkzeug.serving import make_ssl_devcert

        make_ssl_devcert('./ssl', host='mileio.com')
        app.run(debug=True, ssl_context=('./ssl.crt', './ssl.key'))
